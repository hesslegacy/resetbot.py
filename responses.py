import random
import os
import time



def handle_responses(message) -> str:
		p_message = mesage.lower()

		if p_message == '$hello':
			return 'Hey there!'

		if p_message =='?resetdf'
			killdfbot = 
			startdfbot =
			os.system(killdfbot)
			time.sleep(1)
			os.system(startdfbot)
			return 'StepBro should be restarted.'

		if p_message =='?resettdt'
			killtdtbot =
			starttdtbot =
			os.system(killtdtbot)
			time.sleep(1)
			os.system(starttdtbot)
			return 'TDTBot should be restarted.'

		if p_message == '$roll d2':
			return str(random.randint(1,2))

		if p_message == '$roll d4':
			return str(random.randint(1,4))

		if p_message == '$roll d6':
			return str(random.randint(1,6))
				
		if p_message == '$roll d8':
			return str(random.randint(1,8))	

		if p_message == '$roll d10':
			return str(random.randint(1,10))

		if p_message == '$roll d12':
			return str(random.randint(1,12))
				
		if p_message == '$roll d20':
			return str(random.randint(1,20))	

		if p_message == '$roll d100':
			return str(random.randint(1,100))	

		if p_message == '$help':
			return """
'''
This is a simple bot, 
used to do not a lot. 
If you'd like to roll
a die, you can say hi.

$roll d2
$roll d4
$roll d6
$roll d8
$roll d10
$roll d12
$roll d20
$roll d100
'''
				"""


