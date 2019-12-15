# CompSystems

⦁	 Short project description.
My family and I moved to Luxembourg recently and my children are now learning Luxembourgish and German at school. I want to turn my Raspberry Pi into a voice recognition German to English translator. * As I do not speak German myself, for testing purpose, the project translates French (French-Canadian) to English.

After pressing the sensorHat, the recording will start for 5 seconds. An "R" is displayed on the Raspberry Pi right after the button is pressed and disappeared to let the user know the recording has started.  This creates a .wav file with the required specifications to be sent to the Google Speech-to-text API. Once the audio file is converted to text, it is then sent to Google translate. eSpeak renders the English translation.

Lightweight messaging  Using the Flow in Wia, an email is sent after the word reached the web application. Doing so, it is possible to see how the spelling of the word we are attempting to translate.

Finally, the words, translations and time stamp are published via a MQTT broker. The webserver acts as the subscriber receiving the data and sending them to the dbserver, where they are store into a SQL database.

## Tools, Technologies and Equipment
Equipment, Software: 
⦁	Raspberry Pi 3b+
⦁	SenseHat,
⦁	Jabra SPEAK 510 USB
⦁	eSpeak
⦁	Cloud MQTT Broker
⦁	VirtualBox / Vagrant / webserver & dbserver (per lab week7)
⦁	Google Cloud Platform (Google text-to-speech API & Google Translate)
⦁	Wia  
