python3 -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
chmod +x get-phonebook.sh
echo "*/30 * * * * /home/pi/kurt/get-phonebook.sh" | sudo tee -a /etc/crontab
sudo cp -f kurt.service /lib/systemd/system/kurt.service
sudo chmod 644 /lib/systemd/system/kurt.service
sudo systemctl daemon-reload
sudo systemctl enable kurt.service

