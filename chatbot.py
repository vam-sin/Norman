import aiml
import os

# Tasks Left
# Connect to the internet to get trends for subjects.
# Make both subject and prof work

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

print("\nNorman: Hi! My name is Norman!\n")

while True:
	# Process the input. LowerCase it, remove punctuation.
	string = input("User: ")
	string = string.lower()
	string = Punctuation(string)

	# Get parameters
	subject = kernel.getPredicate('subject')
	prof = kernel.getPredicate('ppp') # ppp is the prof parameter (LOL)

	# print("Parameters: " + subject + " " + prof)

	if subject == 'none' and prof == 'none': # Suggest random (Working)
		os.system("python3 SQL/sql_snone_pnone.py")
	elif subject == 'none' and prof != '': # Working
		os.system("python3 SQL/sql_snone_p.py " + prof)
	elif subject != '' and prof == 'none': # Working
		os.system("python3 SQL/sql_s_pnone.py " + subject)
	elif subject != '' and prof != '': # Not working
		subject = subject.split()[0]
		prof = prof.split()[0]
		# print(subject, prof)
		os.system("python3 SQL/sql_s_p.py " + subject + " " + prof)
	else: 
		print(kernel.respond(string))