# Check your server's public IP with Telegram
Use a Telegram bot to easily check the current public IP of your Raspberry Pi (or any server machine)

## To execute the script on boot

Copy telegram-bot.service to the /etc/systemd/system/ directory

Reload the systemd manager configuration:

`sudo systemctl daemon-reload`

Enable the service to run at boot:

`sudo systemctl enable telegram-bot.service`

Start the service:

`sudo systemctl start telegram-bot.service'`
