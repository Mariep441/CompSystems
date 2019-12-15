#!/bin/bash

while true
do

  #run the python script to detect if the button have been pressed
  python button.py

  #use arecord to record the word to be translated in a format that can be used by google speech recognition
  arecord --device=hw:1,0 -d 2 --format S16_LE --rate 44100 -c1 word.wav

  echo "Converting Speech to Text..."

  #send the voice record to the Google cloud to have it a text file
  gcloud ml speech recognize  word.wav  --language-code='fr-CA'>file.txt

  #extract the word from the text file received from the Google cloud
  echo "You Said:"
  value=`cat file.txt`
  echo "$value"
  word=$(echo $value | sed -n -e 's/^.*"transcript": "//p'| sed 's/\" } ] } ] }//')

  echo "$word"

  #Export word to be ale to use it in the next python script
  export word

  #run the python script to send words to wia and to the dbserver
  python script.py

  echo "completed"

done



