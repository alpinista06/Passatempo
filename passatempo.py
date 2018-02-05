from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scatterlayout import ScatterLayout
from kivy.graphics import *

        
        
class passatempo(GridLayout):
    def __init__(self):
        self.cols = 4
        super(passatempo, self).__init__()
        self.buttons = []
        for indice in range(1,16):
            self.add_widget(Button(text=str(indice)))
        
    def callback(self, instance, value):
        for indice in range(1,16):
            self.buttons[indice].bind(on_press=movimento)

'''
class toque(Button):
    def moveNode(self):
        with touch:
            self.pos=[touch.x-25, touch.y-25]


       #def onTouchMove(self, touch):
       #   if self.collide_point(touch.x, touch.y):
       #       self.pos=[touch.x-25, touch.y-25]
        pass   
'''


class movimento(ScatterLayout):
    def mov(self):
           self.pos=[touch.x-25, touch.y-25]
        
    
    
class passaApp(App):    
    def build(self):    
        return passatempo()  
    

if __name__ == '__main__':  #Essa forma e padrao
    passaApp().run()

    
    
    
            
