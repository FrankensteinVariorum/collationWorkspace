#!/bin/bash

#### create or remove output folders
#for i in $(seq -w 01 33)
#do
#  outputDir="collationChunks/C$i/output"
##  mkdir $outputDir; touch "$outputDir/Readme.md"
##  rm -r $outputDir
#done

isInt="^[0-9]+$"

checkInput(){
  chunk=$1
  while ! [[ "$chunk" =~ $isInt ]] || [[ $chunk -lt 1 ]] || [[ $chunk -gt 33 ]]
  do
    read -p "Please input an integer between 1 and 33: " chunk
  done
  return $chunk
}
procChunk(){
  chunk=$1
  outputDir="collationChunks/$chunk/output"
  if [ ${#chunk} -lt 2 ]; then
    chunk="0$chunk"
  fi
  chunk="C$chunk"
  outputDir="collationChunks/$chunk/output"
  # Run collate.py
  echo "+-------Simply process the chunk $chunk-------+"
  python3 python-collation/collate.py $chunk
  # Check if simple output file is generated
  if [ ! -f "$outputDir/Collation_$chunk-partway.xml" ]; then
    echo "Collation_$chunk-partway.xml NOT exist!"
  # exit 1
  else
    echo "Collation_$chunk-partway.xml is generated!"
  fi
  # Run Saxon to post-process collations
  echo "+-------Post-process the collation $chunk-------+"
  java -jar xslt/SaxonHE12-0J/saxon-he-12.0.jar -xsl:xslt/postProcessing.xsl -s:$outputDir/collation_$chunk-partway.xml -o:$outputDir/Collation_$chunk-complete.xml
  # Check if simple output file is generated
  if [ ! -f "$outputDir/Collation_$chunk-complete.xml" ]; then
    echo "Collation_$chunk-complete.xml NOT exist!"
    exit 1
  else
    echo "Collation_$chunk-complete.xml is generated!"
  fi
}

read -p "Only one collation chunk? Enter [y/n]: " opt
if [[ $opt == "Y" ]] || [[ $opt == "y" ]]; then
  read -p "Enter the num of the chunk: " chunk
  checkInput $chunk
  chunk=$?
  # Process chunk
  procChunk $chunk
else # If multiple chunks, then...
  echo Enter the range of the collation to output:
  read -p "From: " start
  checkInput $start
  start=$?
  read -p "To: " end
  checkInput $end
  end=$?
  # Process chunks
  for chunk in $(seq $start $end)
  do
    procChunk $chunk
  done
fi
