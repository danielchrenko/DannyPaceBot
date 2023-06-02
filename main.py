# By Daniel Chrenko
# Latest edit June 1st 2023

# WIP

import requests
# need this for the run api

import time
# for delayed calls

import keyboard
# for testing

def main():

	while True:
		pass
	


def on_key_press(event):
	''' on key press function, where event is the key '''
	
	if event.name == 'c':
		call_api()



def call_api():

	print("Making API call")
		
	# response = requests.get('https://therun.gg/api/games/Minecraft: Java Edition')
	# response = requests.get('https://therun.gg/api/users/meebie')
	# response = requests.get('https://therun.gg/api/live/meebie')
	
	response = requests.get('wss://fh76djw1t9.execute-api.eu-west-1.amazonaws.com/prod?username=meebie')
	
	# print(response.status_code)
	# print(response.content)
	
	print("\n")
	
	print(response.content)
	
	# data = response.json()
	
	#  print(value)
	

		
keyboard.on_press(on_key_press)

main()
