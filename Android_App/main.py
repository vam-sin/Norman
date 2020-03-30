# Libraries
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label 
from kivy.properties import ObjectProperty, StringProperty

class CustomWidget(Widget):
    last_name_text_input = ObjectProperty()
    norman_response_text_input = ObjectProperty()
    user_msg = StringProperty('')

    def clear_text(self):
    	self.last_name_text_input.text = ''

    def submit_message(self):
        self.user_msg = self.last_name_text_input.text
        print("User: " + self.user_msg)

    def calculate_response(self):
    	self.norman_response_text_input.text = 'Norman: Hi'
    	print("Norman: ")

class CustomWidgetApp(App):
	def build(self):
		self.box = BoxLayout(orientation = 'vertical', spacing = 10)
		self.CustomWidget = CustomWidget()
		self.box.add_widget(self.CustomWidget)

		return self.box

if __name__ == "__main__":
    CustomWidgetApp().run()