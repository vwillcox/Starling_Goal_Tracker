#!/user/bin/env python3

import os, time
from sys import exit
from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont
from inky import InkyPHAT
from starlingbank import StarlingAccount

import apikey

APIKEY = apikey.api_key

my_account = StarlingAccount(APIKEY)


#Fetch Details from Starling Account 
my_account.update_account_data()
my_account.update_balance_data()
my_account.update_savings_goal_data()


inkyphat = InkyPHAT('red')

inkyphat.set_border(inkyphat.RED)

font = ImageFont.truetype(FredokaOne, 22)
small_font = ImageFont.truetype(FredokaOne, 12)
sfont = ImageFont.truetype('/home/vincent/starling/aer.ttf', 10)

# Draw lines to frame the weather data

img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
draw = ImageDraw.Draw(img)

#balance = str(my_account.savings_goals.total_saved_minor_units)
#balance = '£' + balance

for uid, goal in my_account.savings_goals.items():
    gname = goal.name
    gtarget = goal.target_minor_units
    gtotal = goal.total_saved_minor_units

target = str(round(gtarget / 100))
target = '£'+ target

total = str(round(gtotal / 100))
total = '£' + total

funds = gname
w, h = font.getsize(funds)
x = (inkyphat.WIDTH / 2) - (w / 2)
y = (inkyphat.HEIGHT / 2) - (h / 2)


#draw.text((x, y), balance, inkyphat.RED, font)
#Draw title and title line
draw.line((0, 30, inkyphat.WIDTH, 30), 2)
draw.text((x, 3),funds, inkyphat.BLACK, font)

#draw fund image and fund image line
draw.line((70, 30, 70, inkyphat.HEIGHT), 2)       # Vertical line

#draw current total line and text
draw.line((150, 30, 150, 75), 2)
draw.text((75, 33), 'Current Total', inkyphat.BLACK, sfont)
draw.text((75, 43), total, inkyphat.RED, font)
draw.text((160, 33), 'Target', inkyphat.BLACK, sfont)
draw.text((152, 43), target, inkyphat.RED, font)
draw.line((70, 75, inkyphat.WIDTH, 75), 2)      # Horizontal middle line


inkyphat.set_image(img)

inkyphat.show()


