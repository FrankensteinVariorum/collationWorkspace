#!/bin/bash

isInt="^[0-9]+$"
Red="\e[0;31m"
Green="\e[0;32m"
Yellow="\e[0;33m"
resetColor="\e[0m"
checkInput(){
  chunk=$1
  while ! [[ "$chunk" =~ $isInt ]] || [[ $chunk -lt 1 ]] || [[ $chunk -gt 33 ]]
  do
    if ! [[ "$chunk" =~ $isInt ]]; then
      echo -e "${Red}Invalid input! Your input not a whole number.${resetColor}"
    elif [ $chunk -lt 1 ]; then
      echo -e "${Red}Invalid input! Your input is less than 1. ${resetColor}"
    elif [ $chunk -gt 33 ]; then
      echo -e "${Red}Invalid input! Your input is larger than 33. ${resetColor}"
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
  preprocDir="collationChunks/$chunk"
  inputDir="$preprocDir/input"
  outputDir="collationChunks/$chunk/output"
  # ebb: batch pre-processing with XSLT here:
  echo -e "${Yellow}+-------This starts the XSLT batch pre-processing of the collation chunk $chunk-------+${resetColor}"
  mkdir $inputDir
  java -jar xslt/SaxonHE12-0J/saxon-he-12.0.jar -xsl:xslt/preProcessing-1.xsl -s:$preprocDir -o:$inputDir
  sleep 2

  echo -e "${Yellow}+-------This starts the XSLT batch pre-processing of the collation chunk $chunk-------+${resetColor}"
  mkdir $inputDir
  java -jar xslt/SaxonHE12-0J/saxon-he-12.0.jar -xsl:xslt/preProcessing-2.xsl -s:$inputDir -o:$inputDir
  sleep 2

  # Run collate.py
  echo -e "${Yellow}+-------This starts the Python processing of the collation chunk $chunk-------+${resetColor}"
  cd python-collation
  # ebb: Diagnostic: let's see what version of python and python3 the shell script is aware of:
  echo "The Python3 version is " 
  python3 --version
  echo "The Python version is " 
  python --version
  python collate.py $chunk
  cd ..
  # Check if simple output file is generated
  if [ ! -f "$outputDir/Collation_$chunk-partway.xml" ]; then
    echo -e "${Red}Collation_$chunk-partway.xml DOES NOT exist!${resetColor}"
    exit 1
  else
    echo -e "${Green}Collation_$chunk-partway.xml is generated!${resetColor}"
  fi
  sleep 2
  # Run Saxon to post-process collations
  echo -e "${Yellow}+-------This starts the xslt post-Processing of the collation chunk $chunk-------+${resetColor}"
  java -jar xslt/SaxonHE12-0J/saxon-he-12.0.jar -xsl:xslt/postProcessing.xsl -s:$outputDir/collation_$chunk-partway.xml -o:$outputDir/Collation_$chunk-complete.xml
  # Check if simple output file is generated
  if [ ! -f "$outputDir/Collation_$chunk-complete.xml" ]; then
    echo -e "${Red}Oops! Collation_$chunk-complete.xml DOES NOT exist!${resetColor}"
    # exit 1
  else
    echo -e "${Green}Yeah! Collation_$chunk-complete.xml is created. ${resetColor}"
    echo -e "${Green}The collation processing is COMPLETE!${resetColor}"
  fi
}

echo -e "${Yellow}Welcome to the Frankenstein Collation Station!${resetColor} "
read -p "Are you working with ONLY ONE collation chunk? Enter [y/n]: " opt
while [[ $opt =~ $isInt ]]
do
  echo -e "${Red}Invalid input! Your input is an integer.${resetColor}"
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
