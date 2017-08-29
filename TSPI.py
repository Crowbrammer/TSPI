from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class TSPILayout(BoxLayout):
    pass

class SciQListLayout(GridLayout):
    """docstring for SciQListLayout."""
    def __init__(self, **kwargs):
        super(SciQListLayout, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))
        # newButton = []
        # for x in range (len (dbVals)):
        #      newButton.append(Button (text = "Blah"))
        #      self.addWidget()
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            self.add_widget(btn)

class SciQScrollView(ScrollView):
    """docstring for SciQScrollView."""
    def __init__(self, **kwargs):
        super(SciQScrollView, self).__init__(**kwargs)
        self.add_widget(SciQListLayout(cols=1, spacing=10, size_hint_y=None))



class TSPIApp(App):
    def build(self):
        return SciQScrollView()


if __name__ == '__main__':
    TSPIApp().run()

def hypothesis(arg):
    """
    IF I* invoke bind on SciQListLayout via "self" THEN it will add the traits
    to the instance
    IF I* add the GridLayout to the ScrollView and call it for the app THEN the
    buttons will show and be scrollable
    IF I* call the SciQListLayout with the cols I* want and spacing and size_hint_y
    THEN the screen will work
    IF I* run the program as is THEN the screen will show a 100 scrollable but-
    tons.
    IF I* change "layout" to "self" THEN the screen will show a 100 scrollable but-
    tons.
    IF I* change "layout" to "self" THEN the screen will show a 100 scrollable but-
    tons.

    IF I* read the ScrollView doc THEN I* will understand how to add the GridLayout
    via Python
    IF I* add the SciQListLayout under the SciQScrollView in Kivy Lang THEN the
    program should work
    IF I* change addWidget to add_widget THEN everything in the SciQScrollView
    should work (IT WORKS)
    IF I* create a screen manager and set that as the root THEN I* will be able to
    switch between SciGrid and and SciList in the same app instance
    IF THEN

    """
    pass
