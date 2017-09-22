from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import requests as r
import names
import time
import getpass
import sys
from pygame import mixer
from selenium.common.exceptions import NoSuchElementException
import string
def type(text, id):
	i = 0
	field = driver.find_element_by_id(id)
	letters = list(text)
	while i < len(text):
		randnum = random.random()
		time.sleep(randnum)
		field.send_keys(letters[i])
		i = i + 1
def click(id):
	field = driver.find_element_by_class_name(id)
	field.click()
def clickid(id):
	field = driver.find_element_by_id(id)
	field.click()
def xpath(xpath):
	field = driver.find_element_by_xpath(xpath)
	field.click()
def getpagetype():
	field = driver.find_element_by_id("session-state")
	pagetype = field.get_attribute("data-state")
	return pagetype
def exists(id):
	try:
		driver.find_element_by_class_name(id)
	except NoSuchElementException:
		return False
	return True
def gen():
	i = 0
	stringcrew = ""
	while i < 3:
		letter = random.choice(string.letters)
		stringcrew = stringcrew + letter
		i = i + 0
	return stringcrew 
mixer.init()
mixer.music.load("full.mp3")
mixer.music.play(-1)

#We grab all of the user's data upfront so as to streamline the process
f = open("logo.txt", "r")
contents = f.read()
print(contents)
f.close()
config = {}
with open("config.txt", "r+") as f:
	for setting in f:
		setting = setting.split(":")
		config[setting[0]] = setting[1]
times = ["5 min.","10 min.","15 min.","20 min.","25 min.","30 min.","35 min.","45 min.","60 min."]
k0nfig = raw_input("Would you like to use your last session of user: " + config["username"] + ", session length of " + times[int(config["seslen"])] + ", and level of " + config["level"] + "? \n Press y for yes and n to change.")
if k0nfig == "y":
	crewcrew = int(raw_input("How often would you like the bot to be correct? Please enter a percent without the sign"))
	if len(str(crewcrew)) > 2:
		print("Percent is 2 digits or less.")
		sys.exit(0)
	print("Attempting to log in user: " + config["username"])
	driver = webdriver.PhantomJS(executable_path="phantomjs")
	driver.get("https://membean.com/login")
	#We use the "type" method to fake humanness
	type(config["username"],"user_username")
	type(config["password"], "user_password")
	#and the click method as well
	click("btn-secondary")
	time.sleep(3)
	#Checking if the user has been redirected to the dashboard,
	#an indicator that the user has been logged in correctly
	if driver.current_url != "http://membean.com/dashboard":
		print("Login attempt has failed. Please try again.")
		sys.exit(0)
	else:
		print("Login attempt was successful! Leave your computer's lid open and let's get crackin.")
	#Can't currently find a working exploit for finding the right answer, and the CSS bug was patched
	#currently we load a dictionary file from quizlet, even if that only has around 50-60% accuracy that is much better
	print("Currently loading file for your level")
	dictionary = {}
	with open("level"+str(config["level"][0])+".txt","r+") as f:
		for line in f:
			line_parts = line.split(":")
			dictionary[line_parts[0]] = line_parts[1]
	print("Dictionary file has been loaded")
	time.sleep(random.random())

	#Starting a new training session with the time length that the user specified earlier.
	driver.get("http://membean.com/training_sessions/new")
	time.sleep(random.randrange(1,3))
	try:
		xpath("//input[@value='" + times[int(config["seslen"])] + "']")
	except NoSuchElementException:
		print("Skipped session length page entirely.")
	while True:
		crewlang = random.randrange(5,25) + random.random()
		time.sleep(crewlang)
		if random.randrange(1,99) < crewcrew:
			if getpagetype() == "restudy":
				print("Attempting restudy page.")
				time.sleep(random.random())
				click("answer")
				time.sleep(random.random())
				clickid("next-btn")
				time.sleep(3)
			elif getpagetype() == "new_word":
				print("Attempting new word page.")
				time.sleep(random.random())
				click("answer")
				time.sleep(random.random())
				clickid("next-btn")
				time.sleep(3)
			else:
				if exists("letter-wrapper"):
					driver.execute_script("crew = document.createElement('P'); clozecrew = document.createTextNode(cloze_answer_txt); crew.appendChild(clozecrew); document.body.appendChild(crew); crew.setAttribute('id', 'crewlang')")
					print("Attempting cloze question.")
					cloze_field = driver.find_element_by_id("crewlang")
					cloze_txt = cloze_field.text
					cloze_txt = cloze_txt[1:4]
					driver.execute_script("delete crew; delete clozecrew; elem = document.getElementById('crewlang'); elem.parentNode.removeChild(elem);")
					type(cloze_txt,"choice")
				else:
					print("Attempting quiz question.")
					time.sleep(random.random())
					driver.execute_script("racrew = document.getElementById('pass__event'); racrew.setAttribute('type', 'submit');")
					handle = driver.find_element_by_id("pass__event")
					clickid("pass__event")
					time.sleep(3)
				if getpagetype() == "new_word":
					print("Attempting new word page.")
					time.sleep(random.random())
					click("answer")
					time.sleep(random.random())
					clickid("next-btn")
					time.sleep(3)

		else:
			if getpagetype() == "restudy":
				print("Attempting restudy page.")
				time.sleep(random.random())
				click("answer")
				time.sleep(random.random())
				clickid("next-btn")
				time.sleep(3)
			elif getpagetype() == "new_word":
				print("Attempting new word page.")
				time.sleep(random.random())
				click("answer")
				time.sleep(random.random())
				clickid("next-btn")
				time.sleep(3)
			else:
				clickid("notsure")
				time.sleep(3)
elif k0nfig == "n":
	#run up the boys, you can bet your life on it
	user = raw_input("What is your username? \n")
	if user == "" or user == " ":
		print("Please enter a username.")
		sys.exit(0)
	upass = getpass.getpass("What is your password? \n")
	if upass == "" or upass == " ":
		print("Please enter a password.")
		sys.exit(0)
	seslen = int(raw_input("How long would you like your session to be? \n 1. 5 minutes \n 2. 10 minutes \n 3. 15 minutes \n 4. 20 minutes \n 5. 25 minutes \n 6. 30 minutes \n 7. 35 minutes \n 8. 45 minutes \n 9. 1 hour \n Please input a number 1-9: "))

	#Just a little bit of validation
	if seslen > 9 or seslen < 1:
		print("You must choose a number between 1 and 9")
		sys.exit(0)
	level = int(raw_input("What is your level?"))

	if level > 5 or level < 1:
		print("You must use a level between 1 and 5")
		sys.exit(0)
	crew = int(seslen) - 1
	sesh = times[int(seslen) - 1]
	crewcrew = int(raw_input("How often would you like the bot to be correct? Please enter a percent without the sign"))
	if len(str(crewcrew)) > 2:
		print("Percent is 2 digits or less.")
		sys.exit(0)
	#Opening up the browser and logging the user in
	authcrew = {"username":user, "password":upass}
	print("Attempting to log in user: " + authcrew["username"])
	driver = webdriver.PhantomJS(executable_path="phantomjs")
	driver.get("https://membean.com/login")
	#We use the "type" method to fake humanness
	type(user,"user_username")
	type(upass, "user_password")
	#and the click method as well
	click("btn-secondary")
	time.sleep(3)
	#Checking if the user has been redirected to the dashboard,
	#an indicator that the user has been logged in correctly
	if driver.current_url != "http://membean.com/dashboard":
		print("Login attempt has failed. Please try again.")
		sys.exit(0)
	else:
		crewfig = open("config.txt", "w")
		crewfig.write("username:"+user+"\n")
		crewfig.write("password:"+upass+"\n")
		crewfig.write("level:"+str(level)+"\n")
		crewfig.write("seslen:"+str(crew))
		crewfig.close()
		print("Login attempt was successful! Leave your computer's lid open and let's get crackin.")
	#Can't currently find a working exploit for finding the right answer, and the CSS bug was patched
	#currently we load a dictionary file from quizlet, even if that only has around 50-60% accuracy that is much better
		print("Currently loading file for your level")
		dictionary = {}
		with open("level"+str(level)+".txt","r+") as f:
			for line in f:
				line_parts = line.split(":")
				dictionary[line_parts[0]] = line_parts[1]
		print("Dictionary file has been loaded")
		time.sleep(random.random())

		#Starting a new training session with the time length that the user specified earlier.
		driver.get("http://membean.com/training_sessions/new")
		time.sleep(random.randrange(1,3))
		try:
			xpath("//input[@value='" + sesh + "']")
		except NoSuchElementException:
			print("Skipped session length page entirely.")
		while True:
			crewlang = random.randrange(5,25) + random.random()
			time.sleep(crewlang)
			if random.randrange(1,99) < crewcrew:
				if getpagetype() == "restudy":
					time.sleep(random.random())
					click("answer")
					time.sleep(random.random())
					clickid("next-btn")
					time.sleep(3)
				else:
					if exists("letter-wrapper"):
						driver.execute_script("crew = document.createElement('P'); clozecrew = document.createTextNode(cloze_answer_txt); crew.appendChild(clozecrew); document.body.appendChild(crew); crew.setAttribute('id', 'crewlang')")
						print("Attempting cloze question.")
						cloze_field = driver.find_element_by_id("crewlang")
						cloze_txt = cloze_field.text
						cloze_txt = cloze_txt[1:4]
						driver.execute_script("delete crew; delete clozecrew; elem = document.getElementById('crewlang'); elem.parentNode.removeChild(elem);")
						type(cloze_txt,"choice")
					else:
						print("Attempting quiz question.")
						time.sleep(random.random())
						driver.execute_script("racrew = document.getElementById('pass__event'); racrew.setAttribute('type', 'submit');")
						handle = driver.find_element_by_id("pass__event")
						clickid("pass__event")
						time.sleep(3)
			else:
				if getpagetype() == "restudy":
					time.sleep(random.random())
					click("answer")
					time.sleep(random.random())
					clickid("next-btn")
					time.sleep(3)
				else:
					clickid("notsure")
					time.sleep(3)


else:
	print("Please choose y or n!")
	sys.exit(0)
