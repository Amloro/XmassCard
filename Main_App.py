# import kivy
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.graphics.context_instructions import Color
# from kivy.factory import Factory
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView

Window.size = (300, 600)
Window.color = 179, 255, 135, 188


# -----------------------------------------------------Popups-----------------------------------------------------------


class PopupError(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (180, 160)


# ---------------------------------------------------Image-Chooser-------------------------------------------------------


# -------------------------------------------------Windows Manager------------------------------------------------------

class WindowManager(ScreenManager):
    pass


# -----------------------------------------------------Pages------------------------------------------------------------


class MainWindow(Screen):

    def open_popup(self):
        popup_error = PopupError()
        popup_error.open(self)


class Page2(Screen):
    pass


class Page3(Screen):
    pass


class Page4(Screen):
    pass


class P(FloatLayout):  # PopUp Window
    pass


# -----------------------------------------------------SCROLL-----------------------------------------------------------


class ScrollableContent(Screen):
    pass


# -----------------------------------------------------Builder----------------------------------------------------------

kv = Builder.load_file("xmasscard.kv")


class XmassCard2(App):
    Window.clearcolor = (0.1, 0.5, 0.8, 1)

    def apply_scroll_position(self, page_name):
        page = self.root.ids.page_manager.ids[page_name]
        scroll_view = page.ids.scroll_view
        scroll_content = page.ids.scroll_content
        scroll_view.scroll_y = page.scroll_positions.get(page_name, 0)
        scroll_content.height = scroll_content.minimum_height

    def build(self):
        return kv


neuralRandom = XmassCard2()
neuralRandom.run()
