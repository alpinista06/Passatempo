from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from random import random
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class passatempo(GridLayout):
    def __init__(self):
        self.cols = 4
        super(passatempo, self).__init__()
        self.buttons = []
        for indice in range(1,16):
            self.buttons.append(Button(text=str(indice)))
        
        for button in self.buttons:
            self.add_widget(Button())
        
    def button_clicado(self, instance, value):
            print('User click on', value)
'''            
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
 '''      
class passaApp(App):    
    def build(self):    
        return passatempo()  
    

if __name__ == '__main__':  #Essa forma e padrao
    passaApp().run()

    
    
    
            
