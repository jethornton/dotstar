#!/usr/bin/env python3
import time
from adafruit_dotstar import DotStar

MOSI = 11
SCK = 10
LEDS = 10

string = DotStar(MOSI, SCK, LEDS)
rgb = [0,0,0]

# Sunrise
print('Dawn')
for brightness in range(255):
	time.sleep(0.05)
	#print(f"brightness {brightness}")
	for color in range(3):
		rgb[color] += 1
		for led in range(10):
			string[led] = (rgb)
			#print(f"led {led} red {rgb[0]} green {rgb[1]} blue {rgb[2]}")
print('Sunrise')
time.sleep(10)
print('Sunset')
# Sunset
for brightness in range(255):
	time.sleep(0.05)
	#print(f"brightness {brightness}")
	for color in range(3):
		rgb[color] -= 1
		for led in range(10):
			string[led] = (rgb)
			#print(f"led {led} red {rgb[0]} green {rgb[1]} blue {rgb[2]}")
print('Dusk')

string.fill((0, 0, 0))
