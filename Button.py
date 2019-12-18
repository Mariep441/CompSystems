#!/usr/bin/env python

import time

from wia import Wia
from sense_hat import SenseHat
sense = SenseHat()

wia = Wia()
wia.access_token ="d_sk_xxxxxxxxxxxxxxxxxxxxxx"


while True:
  for event in sense.stick.get_events():
      if event.action == "pressed":
          sense.show_letter("R")
          wia.Event.publish(name="button",data="start recording")
          time.sleep(0.5)
          sense.clear()
          exit()
False

exit()
