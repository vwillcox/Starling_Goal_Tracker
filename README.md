# Track your Starling Bank Goals
Using a Raspberry Pi, a Pimoroni inkyPHAT and some python you can track your savings!

# Using this code
You will need to install the unofficial Python Library for Starling

* pip install starlingbank

or

* sudo pip install starlingbank

or

sudo pip3 install starlingbank


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


