#!/bin/bash

isInt="^[0-9]+$"

checkInput(){
  chunk=$1
  while ! [[ "$chunk" =~ $isInt ]] || [[ $chunk -lt 1 ]] || [[ $chunk -gt 33 ]]
  do
    if ! [[ "$chunk" =~ $isInt ]]; then
      echo "Invalid input! Your input not a whole number. "
    elif [ $chunk -lt 1 ]; then
      echo "Invalid input! Your input is less than 1. "
    elif [ $chunk -gt 33 ]; then
      echo "Invalid input! Your input is larger than 33. "
    fi
    read -p "Please input a whole number between 1 and 33: " chunk
  done
  return $chunk
}
procChunk(){
  chunk=$1
  if [ ${#chunk} -lt 2 ]; then
    chunk="0$chunk"
  fi
  chunk="C$chunk"
  outputDir="collationChunks/$chunk/output"
  # Run collate.py
  echo "+-------This starts the Python processing of the collation chunk $chunk-------+"
  cd python-collation
  python3 collate.py $chunk
  cd ..
  # Check if simple output file is generated
  if [ ! -f "$outputDir/Collation_$chunk-partway.xml" ]; then
    echo "Collation_$chunk-partway.xml DOES NOT exist!"
    exit 1
  else
    echo "Collation_$chunk-partway.xml is generated!"
  fi
  sleep 2
  # Run Saxon to post-process collations
  echo "+-------This starts the xslt post-Processing of the collation chunk $chunk-------+"
  java -jar xslt/SaxonHE12-0J/saxon-he-12.0.jar -xsl:xslt/postProcessing.xsl -s:$outputDir/collation_$chunk-partway.xml -o:$outputDir/Collation_$chunk-complete.xml
  # Check if simple output file is generated
  if [ ! -f "$outputDir/Collation_$chunk-complete.xml" ]; then
    echo "Oops! Collation_$chunk-complete.xml DOES NOT exist!"
    # exit 1
  else
    echo "Yeah! Collation_$chunk-complete.xml is created. "
    echo "The collation processing is COMPLETE!"
  fi
}

echo "Welcome to the Frankenstein Collation Station!"
read -p "Are you working with ONLY ONE collation chunk? Enter [y/n]: " opt
while [[ $opt =~ $isInt ]]
do
  echo "Invalid input! Your input is an integer."
  read -p "Are you working with ONLY ONE collation chunk? Enter [y/n]: " opt
done
if [[ $opt == "Y" ]] || [[ $opt == "y" ]]; then
  read -p "Enter only the whole number of the chunk between 1 and 33: " chunk
  checkInput $chunk
  chunk=$?
  # Process chunk
  procChunk $chunk
else # If multiple chunks, then...
  echo "Enter the range of the collation chunks to output (whole numbers between 1 and 33)"
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
