import aiml
import mysql.connector

# mySQL connection
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root"
# )

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("chatbot.xml")
kernel.respond("load aiml b")

# parameters
# subject = ''
# prof = ''
# need_help_choosing = False

print("\nNorman: Hi! My name is Norman!\n")

while True:
	# Process the input. LowerCase it, remove punctuation.
    print(kernel.respond(input("User: ")))
    # subject = kernel.getPredicate('subject')
    # prof = kernel.getPredicate('prof')
    # if kerne.getPredicate('need_help_choosing') == 'Alright':
    # 	need_help_choosing = True

    # if need_help_choosing == True:
    	
    # 	need_help_choosing = False
    # # print(subject, prof)

    # if subject != '' and prof != '':
    # 	if subject == 'no' and prof == 'no':
    # 		# Give random subject
    # 		pass
    # 	elif subject == 'no':
    # 		# Choose subjects with that prof
    # 		pass
    # 	elif prof == 'no':
    # 		# choose subjects with that subjects
    # 		pass
    # 	else:
    # 		# choose subjects with that prof
    # 		pass