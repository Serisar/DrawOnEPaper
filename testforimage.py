#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import requests
import logging
import drawer
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)


drawer.drawing()

try:
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()


    logging.info("3.read bmp file")
    Himage = Image.open('image_with_weather.bmp')
    epd.display(epd.getbuffer(Himage))
    time.sleep(20)


    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
