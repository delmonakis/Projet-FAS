import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
orange =[1,0.5,0,1]
yellow =[1,1,0,1]
green = [0,1,0,1]
turquoise = [0,1,1,1]
blue =  [0,0,1,1]
purple = [0.5,0,1,1]
pink = [1,0,1,1]

def press_callback(obj):
        print("Button pressed")
        if obj.text=='Exit':
                App.get_running_app().stop()

########################################################################
class MyApp(App):
    """
    Horizontally oriented BoxLayout example class
    """

    #----------------------------------------------------------------------
    def build(self):
        """
        Horizontal BoxLayout example
        """
        layout = BoxLayout(padding=10)
        color = [red, orange, yellow, green, turquoise, blue, purple, pink]

        btnred = Button(background_color=color[0])
        btnred.bind(on_press=press_callback)
        btnorange = Button(background_color=color[1])
        btnorange.bind(on_press=press_callback)
        btnyellow = Button(background_color=color[2])
        btnyellow.bind(on_press=press_callback)
        btngreen = Button(background_color=color[3])
        btngreen.bind(on_press=press_callback)
        btnturq = Button(background_color=color[4])
        btnturq.bind(on_press=press_callback)
        btnblue = Button(background_color=color[5])
        btnblue.bind(on_press=press_callback)
        btnpurple = Button(background_color=color[6])
        btnpurple.bind(on_press=press_callback)
        btnpink = Button(background_color=color[7])
        btnpink.bind(on_press=press_callback)
        btnlampe = Button(text="Lampe")
        btnlampe.bind(on_press=press_callback)
        btnexit = Button(text="Exit")
        btnexit.bind(on_press=press_callback)

        layout.add_widget(btnred)
        layout.add_widget(btnorange)
        layout.add_widget(btnyellow)
        layout.add_widget(btngreen)
        layout.add_widget(btnturq)
        layout.add_widget(btnblue)
        layout.add_widget(btnpurple)
        layout.add_widget(btnpink)
        layout.add_widget(btnlampe)
        layout.add_widget(btnexit)

        return layout

########################################################################
#----------------------------------------------------------------------
if __name__ == "__main__":
        MyApp().run()
