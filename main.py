#!/usr/bin/env python
from PIL import Image
import pytesseract
import os
import time


def image_read():
    """Function for reading 3 images from disk"""
    target_dir = "/home/adam/Dropbox/puls_ruffier/Adam"
    os.chdir(target_dir)
    all_files = os.listdir(target_dir)
    return all_files


def image_sort(image_list):
    """Function that sort list of images based on modification date"""
    image_dict = {}
    s_list = []
# getting timestamp from file
    for item in image_list:
        t = os.path.getmtime(item)
        x = time.strftime('%Y%m%d%H%M', time.gmtime(t))
        image_dict[x] = item
# sort dictionary based on timestamp and creation new sorted list of files names
    for item in sorted(image_dict):
        s_list.append(image_dict[item])

    return s_list


def image_extract(image_file):
    """Function that extract number from image"""
    image = Image.open(image_file)
    width, height = image.size
    left = 0
    top = 200
    right = width  # / 2
    bottom = height - 700  # / 2
    image = image.crop((left, top, right, bottom))
    value = (pytesseract.image_to_string(image))
    value = int(value[:-7])
    return value

def ruffier_index(squats_result):
    index = 0
    return index

loaded_image_list = image_read()
sorted_dictionary = image_sort(loaded_image_list)
print sorted_dictionary
first_image = image_extract(sorted_dictionary[0])
print first_image
