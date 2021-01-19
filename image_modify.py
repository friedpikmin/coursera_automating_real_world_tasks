#!/usr/bin/env python3
from PIL import Image
import os, sys

old_dir = os.path.expanduser('~') + '/images/'
new_dir = '/opt/icons/'
for image in os.listdir(old_dir):
  if '.' not in image[0]:
    correct_img = Image.open(old_dir + image)
    correct_img.rotate(90).resize((128,128)).convert("RGB").save(new_dir + image, "JPEG")
    correct_img.close()
