#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import os
import time
import ConfigParser
import tweepy


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
# parameters for crop (best fit)
    left = 300
    top = 200
    right = width - 400  # / 2
    bottom = height - 700  # / 2
    image = image.crop((left, top, right, bottom))
# extracting string from image
    value = (pytesseract.image_to_string(image))
# extracting numbers (intigers) from string
    i_value = int(filter(str.isdigit, value))
    return i_value


def ruffier_index(squats_result):
    index = (sum(squats_result) - 200) / 10
    return index


def ruffier_compare(index):
    if index >= 0:
        return "bardzo dobra"
    elif index <= 5:
        return "dobra"
    elif index <= 10:
        return "słaba"
    else:
        return "bardzo słaba"


def status_tweet(status):
    # Loading config.ini
    config = ConfigParser.SafeConfigParser()
    config.read('/home/adam/PycharmProjects/ruffier_test/config.ini')

    # Reading key and token values from config.ini file
    consumer_key = config.get('KEY', 'consumer_key')
    consumer_secret = config.get('KEY', 'consumer_secret')
    access_token = config.get('TOKEN', 'access_token')
    access_token_secret = config.get('TOKEN', 'access_token_secret')

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    # Sample method, used to update a status
    api.update_status('Twoja wydolność organizmu jest %s!' % (status))

loaded_image_list = image_read()
sorted_dictionary = image_sort(loaded_image_list)
extracted_its = []
for item in sorted_dictionary:
    extracted_its.append(image_extract(item))
compared = ruffier_compare(ruffier_index(extracted_its))
print compared
status_tweet(compared)

