import sys
import time
import telepot
import subprocess

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print('chat id: ' + str(chat_id))
	print('command: ' +  command)

	if command == '/getIP':
		bash_script = 'dig +short myip.opendns.com @resolver1.opendns.com'

		# Execute the Bash script and capture the output
		output = subprocess.check_output(bash_script, shell=True, text=True)
		bot.sendMessage(chat_id, 'My public IP is: ' + output)

bot = telepot.Bot(YOUR_BOT_TOKEN)
bot.message_loop(handle)
print('I am listening...')

while 1:
	time.sleep(10)
