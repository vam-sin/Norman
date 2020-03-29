import aiml
import os

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
	prof = kernel.getPredicate('ppp')
	# if prof == '':
	# 	print("BiF")

	print("Parameters: " + subject + " " + prof)

	if subject == 'none' and prof == 'none': # Suggest random (Working)
		os.system("python3 sql_snone_pnone.py")
	elif subject == 'none' and prof != '': # Not working
		os.system("python3 sql_snone_p.py " + prof)
	elif subject != '' and prof == 'none': # Working
		os.system("python3 sql_s_pnone.py " + subject)
	elif subject != '' and prof != '': # Not working
		pass
	else: 
		print(kernel.respond(string))