#!/usr/bin/python

import os
from subprocess import call

# Language Translator
from googletrans import Translator  # Import Translator module from googletrans package

translator = Translator() # Create object of Translator.

translated = translator.translate(os.environ['word'], src='fr', dest='en') # Pass both source and destination

translation = translated.text

# Source language auto detect by google trans
# By default destination language is English
print(" Source Language:" + translated.src)

print(" Translated string:" + translated.text)

call(["espeak","-s140 -ven+18 -z",translated.text])

