from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class КалькуляторApp(App):
    def build(self):

        self.number = 0

        self.bl = BoxLayout(orientation='vertical')

        self.bl.add_widget(TextInput(text=str(self.number)))

        return(self.bl)

КалькуляторApp().run()
