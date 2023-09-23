chmod +x get-phonebook.sh
echo */30 * * * * /home/pi/kurt/get-phonebook.sh | sudo tee /etc/crontab
sudo cp -f kurt.service /lib/systemd/system/kurt.service
sudo chmod 644 /lib/systemd/system/kurt.service
sudo systemctl daemon-reload
sudo systemctl enable kurt.service

