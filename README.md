# Track your Starling Bank Goals
Starling bank have a very handy developer portal, that allows any budding coder write code to look at their own personal Starling Account. Following their guide (https://developer.starlingbank.com/) will #
allow you to setup a development account and then link this to your personal Starling Account.

# Requirements

1. Fully setup and working Raspberry Pi
2. A Starling Bank account
3. A Starling Developer Account (https://developer.starlingbank.com/)
4. Your Starling Development account and Starling Bank account linked
5. A Pimoroni inky pHAT display setup and running on your Raspberry Pi (https://shop.pimoroni.com/products/inky-phat?variant=12549254217811)

# What it does

Once setup and configured, this program will connect to your Starling Developer account, grab your Current Account details and any saving goal details you have setup in your linked
Starling Bank account.

Once it has this information, it will show show one or more of the following

* Current Acount Details
* Goal Details
* A fun icon

It will either show these one or more times, depending on how you run the code.

# Using this code
You will need to install the unofficial Python Library for Starling

* pip install starlingbank

or

* sudo pip install starlingbank

or

* sudo pip3 install starlingbank

Installs the following Library

	https://github.com/Dullage/starlingbank

You will also need to setup a Starling Developer account, link it to your own Starling Bank account and get an API Key

Once you have an API key, create a file called "apikey.py" and put the following in:

api_key = YOUR API KEY

# Running the code
You can specify the following switches

-c / --current : Show you current account balance of your Starling Account

-l / --loop : Loop the code until manually stopped

-t / --time : How long to wait on each screen


for example:

	python3 main.py -c

This will show all the screens, once with the default time of 60 seconds between each screen

	python3 main.py -t 10

This will show just your saving goals with a time delay of 10 seconds between each screen

	python3 main.py -l -t 120

This will loop the Savings goals with 120 seconds between each screen


