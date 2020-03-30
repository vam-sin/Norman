# Libraries
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
import aiml
import os
import csv
import sys
from io import StringIO


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
    kernel = aiml.Kernel()
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
        print("User: " + self.user_msg)

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
            os.system("python3 SQL/sql_snone_pnone.py")
        elif subject == 'none' and prof != '':  # Working
            os.system("python3 SQL/sql_snone_p.py " + prof)
        elif subject != '' and prof == 'none':  # Working
            os.system("python3 SQL/sql_s_pnone.py " + subject)
        elif subject != '' and prof != '':  # working
            subject = subject.split()[0]
            prof = prof.split()[0]
            # print(subject, prof)
            os.system("python3 SQL/sql_s_p.py " + subject + " " + prof)
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
