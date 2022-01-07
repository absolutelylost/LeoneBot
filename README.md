# LeoneBot
LeoneBot prototype to work for the MAE discord server

once we have a folder that we want to use as our home, run git commands to initialize
-----------------------------------------------------
echo "# DiscordBots1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:absolutelylost/DiscordBots1.git
git push -u origin main
-----------------------------------------------------
…or push an existing repository from the command line
-----------------------------------------------------
git remote add origin git@github.com:absolutelylost/DiscordBots1.git
git branch -M main
git push -u origin main

Needed to install discord.js through CMD
	* npm discord.js


starting project
	* npm init - starts node project 
		- fill in infomration asked
		- entry point is the main file. 
			- can be named anything.
code . -opens vs code in directory using that
	code present

* be sure to create (main file name).js
-----------------------------------------------------
		ADD BOT
-----------------------------------------------------
go to discord.com/developers/applications
	* we need to create a discord application through portal
	* after creating, convert to a bot uising the Bot tab
	* to add to own discord sever 
		* discordapi.com/permissions.html
			* this is a calculator to generate url
			* insert client id
-----------------------------------------------------
-----------------------------------------------------

To send a message to specific channel

const channel = <client>.channels.cache.get('<id>');
channel.send('<content>');
To send a message to a specific user in DM

const user = <client>.users.cache.get('<id>');
user.send('<content>');

-----------------------------------------------------
-----------------------------------------------------

PERMISSIONS - 
	check code on permissions to send specific 
	commands for upper level roles

-----------------------------------------------------
-----------------------------------------------------


RUNNING BOT - 
	py main.py or python main.py

-----------------------------------------------------
-----------------------------------------------------

