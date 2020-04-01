# Libraries
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import aiml
from random import choice

# dataset
handouts = {
 'Deep Learning': 'N L Bhanu Murthy',
 'Reinforcement Learning': 'Paresh Saxena',
 'Artificial Intelligence': 'Jabez J Christopher',
 'Parallel Computing': 'Geethakumari',
 'Cloud Computing': 'Suvadip Batyabyal',
 'Information Retrieval': 'Aruna Malapati',
 'Machine Learning': 'Lov Kumar'
}

# Functions
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

# creating the flask app 
app = Flask(__name__) 
api = Api(app) 

class Hello(Resource): 
	# GET request
	def get(self): 

		return jsonify({'Norman': 'Hi! My name is Norman!'}) 

	# POST request 
	def post(self): 
		data = request.get_json()

		return jsonify({'data': data}), 201

class chatbot(Resource):
	def get(self, user_msg):
		# Replace whitespaces with %20
		user_msg = user_msg.lower()
		user_msg = Punctuation(user_msg)
		# Get parameters
		subject = kernel.getPredicate('subject')
		prof = kernel.getPredicate('ppp') # ppp is the prof parameter (LOL)s

		if subject == 'none' and prof == 'none': # Suggest random (Working)
			sub, pro = choice(list(handouts.items()))
			response = "Norman: Try " + str(sub) + " offered by " + "Prof. " + str(pro)
			return response
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
				return response
			else:
				response = "Norman: You could try the following courses: \n"
				for i in range(len(subs)):
					response += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
					return response
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
				return response
			else:
				response = "Norman: You could try the following courses: \n"
				for i in range(len(subs)):
					response += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
				return response
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
				return response
			else:
				response = "Norman: You could try the following courses: \n"
				for i in range(len(subs)):
					response += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
				return response
		else: 
			return kernel.respond(user_msg)

# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(chatbot, '/chat/<user_msg>')


# driver function 
if __name__ == '__main__': 
	# Create the kernel and learn AIML files
	kernel = aiml.Kernel()
	kernel.learn("chatbot.xml")
	kernel.respond("load aiml b")

	# Run Flask app
	app.run(host = '192.168.1.7', debug = True) 
