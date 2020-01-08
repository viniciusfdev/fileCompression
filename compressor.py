# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:14:36 2020

@author: vinicius
"""

#diminui se o tamanho da img mantendo o aspect ratio
#compress the img

from PIL import Image
import os, zlib, sys, time, base64

from pathlib import Path

def compress_img(nm_file):
    img = Image.open(nm_file)
    nm_file, ext = str(nm_file).split('.')
    actual_width, actual_height = img.size
    img = img.resize((int(actual_width/4), int(actual_height/4)), Image.ANTIALIAS)
    img.save('{}_cp.{}'.format(nm_file, ext), optimize=True, quality=90)
    img.close()

def compress_file(nm_file):
    file = nm_file.lower()
    file = open(file, 'rb').read()
    compressed = zlib.compress(file, 9)
    out_file = script_location / 'cp_{}'.format(nm_file.lower())
    out_file = open(out_file, 'wb')
    out_file.write(compressed)
    out_file.close()
    
script_location = Path(__file__).absolute().parent
nm_file = script_location / 'IMG_1.jpg'
compress_img(nm_file)