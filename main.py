#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, time
from sys import exit
from font_fredoka_one import FredokaOne
from PIL import Image, ImageDraw, ImageFont
from inky import InkyPHAT
from starlingbank import StarlingAccount
import pathlib
import apikey

path = str(pathlib.Path().absolute())
APIKEY = apikey.api_key
my_account = StarlingAccount(APIKEY)
sleeptime = 60

def percentage(part, whole):
    return 100 * float(part)/float(whole)

inkyphat = InkyPHAT('red')
inkyphat.set_border(inkyphat.RED)
font = ImageFont.truetype(FredokaOne, 22)
small_font = ImageFont.truetype(FredokaOne, 12)
sfont = ImageFont.truetype(path+'/aer.ttf', 10)
fa = ImageFont.truetype(path+"/fa-regular-400.ttf", 60)

while True: 
    my_account.update_account_data()
    my_account.update_balance_data()
    my_account.update_savings_goal_data()
    img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
    draw = ImageDraw.Draw(img)
    target = '£0.00'
    total = my_account.effective_balance
    total = total / 100
    total = '£' + str(total)
    gname = 'Current Account'
    symbol = u""
    w, h = font.getsize(gname)
    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = (inkyphat.HEIGHT / 2) - (h / 2)
    draw.line((0, 30, inkyphat.WIDTH, 30), 2)
    draw.text((x, 3),gname, inkyphat.BLACK, font)
    draw.line((70, 30, 70, 75), 2)       # Vertical line
    draw.text((1, 22), symbol, inkyphat.RED, fa)
    draw.text((75, 33), 'Cleared Funds', inkyphat.BLACK, sfont)
    draw.text((75, 43), total, inkyphat.RED, font)
    draw.line((70, 75, inkyphat.WIDTH, 75), 2)
    inkyphat.set_image(img)
    inkyphat.show()
    time.sleep(sleeptime)
    for uid, goal in my_account.savings_goals.items():
        img = Image.new("P", (inkyphat.WIDTH, inkyphat.HEIGHT))
        draw = ImageDraw.Draw(img)
        target = ''
        total = ''
        funds = ''
        percent = ''
        gname = ''
        gname = goal.name
        gtarget = goal.target_minor_units
        gtotal = goal.total_saved_minor_units
        target = str(round(gtarget / 100))
        target = '£'+ target
        total = str(round(gtotal / 100))
        total = '£' + total
        symbol = u""
        pro_symbol = u""
        percent = str(round(percentage(gtotal, gtarget))) + '%'
        percent_bar_size = percentage(gtotal, gtarget) / 100 * 212
        funds = gname
        w, h = font.getsize(funds)
        x = (inkyphat.WIDTH / 2) - (w / 2)
        y = (inkyphat.HEIGHT / 2) - (h / 2)
        draw.line((0, 30, inkyphat.WIDTH, 30), 2)
        draw.text((x, 3),funds, inkyphat.BLACK, font)
        draw.line((70, 30, 70, 75), 2)       # Vertical line
        draw.text((1, 22), symbol, inkyphat.RED, fa)
        draw.line((150, 30, 150, 75), 2)
        draw.text((75, 33), 'Current Total', inkyphat.BLACK, sfont)
        draw.text((75, 43), total, inkyphat.RED, font)
        draw.text((160, 33), 'Target', inkyphat.BLACK, sfont)
        draw.text((152, 43), target, inkyphat.RED, font)
        draw.line((70, 75, inkyphat.WIDTH, 75), 2)      # Horizontal middle line
        draw.rectangle(((0, 75), (percent_bar_size, 150)), fill=inkyphat.RED, outline=inkyphat.BLACK)
        draw.text((72, 78), percent, inkyphat.BLACK, font)
        inkyphat.set_image(img)
        inkyphat.show()
        time.sleep(sleeptime)


