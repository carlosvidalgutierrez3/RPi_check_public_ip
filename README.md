# Check your server's public IP with Telegram

## To execute the script on boot

Copy telegram-bot.service to the /etc/systemd/system/ directory:

Reload the systemd manager configuration:

'sudo systemctl daemon-reload'

Enable the service to run at boot:

'sudo systemctl enable myscript.service'

Start the service:

'sudo systemctl start myscript.service'
