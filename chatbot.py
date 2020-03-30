import aiml, os, csv, sys
from io import StringIO
import subprocess

# Tasks Left
# Connect to the internet to get trends for subjects.
# Store the conversations in flat file (Need Help)
# Make both subject and prof work (Done)

# class Logger(object):
#     def __init__(self):
#         self.terminal = sys.stdout
#         self.log = open("conv.txt", "a")

#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)  

#     def flush(self):
#         sys.stdout.flush()   

# sys.stdout = Logger()

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

user_msg = ''
norman_msg = ''

print("\nNorman: Hi! My name is Norman!")

while True:
	# Process the input. LowerCase it, remove punctuation.
	string = input("User: ")
	string = string.lower()
	string = Punctuation(string)
	# f.write("User: " + string)
	# f.write("\n")
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
	elif subject != '' and prof != '': # working
		subject = subject.split()[0]
		prof = prof.split()[0]
		# print(subject, prof)
		os.system("python3 SQL/sql_s_p.py " + subject + " " + prof)
	else: 
		print(kernel.respond(string))





