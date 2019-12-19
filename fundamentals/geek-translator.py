#!/user/bin/python2

# Geek Translator
# Demonstrates using dictionaries
# Written for python 2

# create the dictionary
# six pairs, each called "items"
# each item is made up of a key and a value

geek = {"404": "clueless.From the web error message 404, meaning page not found.",
"Googling": "searching the Internet for background information on a person.",
"Keyboard Plaque" : "the collection of debris found in computer keyboards.",
"Link Rot" : "the process by which web page links become obsolete.",
"Percussive Maintenance" : "the act of striking an electronic device to make it work.",
"Uninstalled" : "being fired. Especially popular during the dot-bomb era."}

# Menu

choice = None
while choice != "0":
	print  \
	"""
	Geek Translator
	0 - Quit
	1 - Look Up a Geek Term
	2 - Add a Geek Term
	3 - Redefine a Geek Term
	4 - Delete a Geek Term
	5 - Show all items
	"""

	choice = raw_input("Choice: ")
	print ""

	# exit
	if choice == "0":
		print "Goodbye."

	# get a definition
	elif choice == "1":
		term = raw_input("What term do you want me to translate?: ")
		if term in geek:
			definition = geek[term]
			print "\n", term, "means", definition
		else:
			print "\nSorry, I don't know", term

	# add a term-definition pair
	# Note: If you assign a value to a dictionary using a key that already 
	# exists, Python replaces the current value without complaint.
	elif choice == "2":
		term = raw_input("What term do you want me to add?: ")
		if term not in geek:
			definition = raw_input("\nWhat's the definition?: ")
			geek[term] = definition
			print "\n", term, "has been added."
		else:
			print "\nThat term already exists! Try redefining it."

	# redefine an existing term
	elif choice == "3":
		term = raw_input("What term do you want me to redefine?: ")
		if term in geek:
			definition = raw_input("What's the new definition?: ")
			geek[term] = definition
			print "\n", term, "has been redefined."
		else:
			print "\nThat term doesn't exist! Try adding it."

	# delete a term-definition pair
	elif choice == "4":
		term = raw_input("What term do you want me to delete?: ")
		if term in geek:
			del geek[term]
			print "\nOkay, I deleted", term
		else:
			print "\nI can't do that!", term, "doesn't exist in the dictionary."

	elif choice == "5":
		print "\nHere are all the items in the dictionary:\n"
		print geek.items()

	# some unknown choice
	else:
		print "\nSorry, but", choice, "isn't a valid choice."
		raw_input("\n\nPress the enter key to exit.")
