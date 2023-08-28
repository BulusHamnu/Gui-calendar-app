import kivy
import calendar
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import ActionBar, ActionView,ActionPrevious, ActionButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout


class cal_screen (BoxLayout) :
    def __init__ (self,**kwargs) :
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.action_bar = ActionBar()
        self.action_view = ActionView()
        self.action_previous = ActionPrevious(title = 'My Calendar', with_previous = False)
        self.action_button1 = ActionButton (text = '2023', on_press = self.change_year2023)
        self.action_button2 = ActionButton (text = '2024', on_press = self.change_year2024)
        self.action_button3 = ActionButton (text = '2025', on_press = self.change_year2025 )
        
        self.action_view.add_widget(self.action_previous)
        self.action_view.add_widget (self.action_button1)
        self.action_view.add_widget (self.action_button2)
        self.action_view.add_widget(self.action_button3)
        self.action_bar.add_widget(self.action_view)
            
        self.cal_view = ScrollView (size_hint = (1,1), size = (self.width, self.height))
        self.add_widget(self.action_bar)
        self.add_widget(self.cal_view)
        self.layout = GridLayout (cols = 1,size_hint_y = 0.9, spacing = 5 )
        self.cal_view.add_widget(self.layout)
        self.month = 1
        self.yy = 2022
    
        self.add_content()
    def add_content(self) :
        for num in range (1,13) :
            cal = calendar.TextCalendar().formatmonth (self.yy,self.month)
            textnote = Label (text = cal, font_size = 50, size_hint_y=None, height=(600))
            self.layout.add_widget(textnote)
            self.month += 1
    def change_year2023 (self, instance):
            self.yy = 2023
            self.month = 1
            self.layout.clear_widgets()
            self.add_content()
    def change_year2024 (self, instance) :
            self.yy = 2024
            self.month = 1
            self.layout.clear_widgets()
            self.add_content()
    def change_year2025 (self, instance) :
            self.yy = 2025
            self.month = 1
            self.layout.clear_widgets()
            self.add_content()    

class Mycalendarapp (App) :
    def build (self):
        return cal_screen()

if __name__ == "__main__" :
    Mycalendarapp().run()