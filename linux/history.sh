sudo apt install build-essential dkms linux-headers-$(uname -r)
sudo apt update
sudo apt upgrade
 
sudo apt install build-essential dkms linux-headers-$(uname -r)


mv sources.list sources.list.original



sudo gedit ./sources.list.save

mv sources.list sources.list.original

vi sources.list

rm sources.list.original

#to do a reboot
sudo systemctl reboot


gedit ./usefull_commands

# terminal history
history

#saving history on history.txt file
history > history.txt
