import aiml
from random import choice

handouts = {
 'Deep Learning': 'N L Bhanu Murthy',
 'Reinforcement Learning': 'Paresh Saxena',
 'Artificial Intelligence': 'Jabez J Christopher',
 'Parallel Computing': 'Geethakumari',
 'Cloud Computing': 'Suvadip Batyabyal',
 'Information Retrieval': 'Aruna Malapati',
 'Machine Learning': 'Lov Kumar'
}

# Tasks Left
# Build android app (Done)
# Connect to the internet to get trends for subjects.
# Store the conversations in flat file (7/4)
# Make both subject and prof work (Done)

def Punctuation(string): 
  
    # punctuation marks 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
    # traverse the given string and if any punctuation 
    # marks occur replace it with null 
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
  
    # Print string without punctuation 
    return string 

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("chatbot.xml")
kernel.respond("load aiml b")

# parameters
subject = ''
prof = ''

# File
# f = open('conv.txt','a') 
# f.write("\n\n\n")

# user_msg = ''
# norman_msg = ''

print("\nNorman: Hi! My name is Norman!")

while True:
	# Process the input. LowerCase it, remove punctuation.
	string = input("User: ")
	# string = string.lower()
	# print string
	string = Punctuation(string)
	# f.write("User: " + string)
	# f.write("\n")
	# Get parameters
	subject = kernel.getPredicate('subject')
	prof = kernel.getPredicate('ppp') # ppp is the prof parameter (LOL)

	# print("Parameters: " + subject + " " + prof)

	if subject == 'none' and prof == 'none': # Suggest random (Working)
		sub, pro = choice(list(handouts.items()))
		response = "Norman: Try " + str(sub) + " offered by " + "Prof. " + str(pro)
		print(response)
	elif subject == 'none' and prof != '': # Working
		subs = []
		profs = []
		for k in handouts:
			a = handouts[k].lower()
			if prof in a:
				profs.append(handouts[k])
				subs.append(k)
		if len(subs) == 0:
			response = "Norman: I couldn't find any courses with that preferences."
			print(response)
		else:
			response = "Norman: You could try the following courses: \n"
			for i in range(len(subs)):
				response += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
				print(response)
	elif subject != '' and prof == 'none': # Working
		profs = []
		subs = []
		for k in handouts:
			a = k.lower()
			if subject in a:
				profs.append(handouts[k])
				subs.append(k)
		if len(subs) == 0:
			response = "Norman: I couldn't find any courses with that preferences."
			print(response)
		else:
			response = "Norman: You could try the following courses: \n"
			for i in range(len(subs)):
				response += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
				print(response)
	elif subject != '' and prof != '': # working
		subject = subject.split()[0]
		prof = prof.split()[0]
		profs = []
		subs = []

		for k in handouts:
			a = k.lower()
			b = handouts[k].lower()
			if (subject in a) and (prof in b):
				profs.append(handouts[k])
				subs.append(k)
		if len(subs) == 0:
			response = "Norman: I couldn't find any courses with that preferences."
			print(response)
		else:
			response = "Norman: You could try the following courses: \n"
			for i in range(len(subs)):
				response += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
				print(response)
	else: 
		print(kernel.respond(string))





