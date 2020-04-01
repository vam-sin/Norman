# Libraries
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty 
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from aiml import Kernel
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

class CustomWidget(Widget):
    kernel = Kernel()
    kernel.learn("chatbot.xml")
    kernel.respond("load aiml b")
    last_name_text_input = ObjectProperty()
    norman_response_text_input = ObjectProperty()
    norman_msg = ''
    user_msg = StringProperty('')
    subject = ''
    prof = ''

    def clear_text(self):
        self.last_name_text_input.text = ''

    def submit_message(self):
        self.user_msg = self.last_name_text_input.text
        # print("User: " + self.user_msg)

    def chat(self):
        # while True:
        # Process the input. LowerCase it, remove punctuation.
        self.user_msg = self.user_msg.lower()
        self.user_msg = Punctuation(self.user_msg)
        # f.write("User: " + string)
        # f.write("\n")
        # Get parameters
        subject = self.kernel.getPredicate('subject')
        # ppp is the prof parameter (LOL)
        prof = self.kernel.getPredicate('ppp')

        # print("Parameters: " + subject + " " + prof)

        # Suggest random (Working)
        if subject == 'none' and prof == 'none':
            sub, pro = choice(list(handouts.items()))
            self.norman_msg = "Norman: Try " + str(sub) + " offered by " + "Prof. " + str(pro)
            self.norman_response_text_input.text = self.norman_msg
        elif subject == 'none' and prof != '':  # Working
            subs = []
            profs = []
            for k in handouts:
                a = handouts[k].lower()
                if prof in a:
                    profs.append(handouts[k])
                    subs.append(k)
            if len(subs) == 0:
                self.norman_msg = "Norman: I couldn't find any courses with that preferences."
                self.norman_response_text_input.text = self.norman_msg
            else:
                self.norman_msg = "Norman: You could try the following courses: \n"
                for i in range(len(subs)):
                    self.norman_msg += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
                self.norman_response_text_input.text = self.norman_msg
        elif subject != '' and prof == 'none':  # Working
            profs = []
            subs = []
            for k in handouts:
                a = k.lower()
                if subject in a:
                    profs.append(handouts[k])
                    subs.append(k)
            if len(subs) == 0:
                self.norman_msg = "Norman: I couldn't find any courses with that preferences."
                self.norman_response_text_input.text = self.norman_msg
            else:
                self.norman_msg = "Norman: You could try the following courses: \n"
                for i in range(len(subs)):
                    self.norman_msg += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
                self.norman_response_text_input.text = self.norman_msg
        elif subject != '' and prof != '':  # working
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
            # print(subject, prof)
            if len(subs) == 0:
                self.norman_msg = "Norman: I couldn't find any courses with that preferences."
                self.norman_response_text_input.text = self.norman_msg
            else:
                self.norman_msg = "Norman: You could try the following courses: \n"
                for i in range(len(subs)):
                    self.norman_msg += str(subs[i]) + " offered by " + "Prof. " + str(profs[i]) + ". \n"
                self.norman_response_text_input.text = self.norman_msg
        else:
            self.norman_msg = self.kernel.respond(self.user_msg)
            self.norman_response_text_input.text = self.norman_msg
            # print("Norman: " + norman_msg)


class CustomWidgetApp(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical', spacing=10)
        self.CustomWidget = CustomWidget()
        # self.CustomWidget.chat()
        self.box.add_widget(self.CustomWidget)

        return self.box


if __name__ == "__main__":
    CustomWidgetApp().run()
