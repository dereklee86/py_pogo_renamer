#!/bin/env python

import os
import math
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

try:
	for idx, section in enumerate(config.sections()):
		print(idx, "-", section)

	selection = input("select device: ")

	device_name = config.sections()[int(selection)]
except:
	print("invalid device selection")
	exit()

print (device_name)

def percent_to_pixel(x,y):
	return str(math.floor(x/100 * 1920)) + " " + str(math.floor(y/100 * 2200))

def send_tap(x, y):
	os.system("echo adb shell input tap " + percent_to_pixel(x,y))

def send_tap_abs(x, y):
	os.system("adb shell input tap " + str(x) + " " + str(y))
	time.sleep(float(config[device_name]['sleep']))

def send_paste():
	os.system("adb shell input keyevent 279")
	time.sleep(float(config[device_name]['sleep']))

def send_swipe():
	os.system("adb shell input swipe 933 1180 100 1380 200")
	time.sleep(float(config[device_name]['sleep']))

# debug dump config
# for key in config[device_name]:
# 	print(key + " = " + config[device_name][key])

while True:

	# menu
	send_tap_abs(config[device_name]['menu_x'],config[device_name]['menu_y'])
	
	# appraise
	send_tap_abs(config[device_name]['appraise_x'],config[device_name]['appraise_y'])

	# appraise proceed center
	send_tap_abs(config[device_name]['appraise_proceed_x'],config[device_name]['appraise_proceed_y'])

	# calcyiv button
	send_tap_abs(config[device_name]['calcy_button_x'],config[device_name]['calcy_button_y'])

	# calyciv clear
	send_tap_abs(config[device_name]['calcy_proceed_x'],config[device_name]['calcy_proceed_y'])

	# appraise proceed center
	send_tap_abs(config[device_name]['appraise_proceed_x'],config[device_name]['appraise_proceed_y'])

	# rename
	send_tap_abs(config[device_name]['rename_x'],config[device_name]['rename_y'])

	# backspace on keyboard
	send_tap_abs(config[device_name]['backspace_x'],config[device_name]['backspace_y'])

	send_paste()

	# ok on input
	send_tap_abs(config[device_name]['ok_input_x'],config[device_name]['ok_input_y'])

	# ok on rename
	send_tap_abs(config[device_name]['ok_rename_x'],config[device_name]['ok_rename_y'])

	time.sleep(float(config[device_name]['sleep']))

	send_swipe() # next pokemon