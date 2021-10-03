from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.widget import Widget

class _Widget(Widget):
	pass

Window.size = 300,500

class card_app(MDApp):
	def build(self):
		return _Widget()

if __name__ == '__main__':
	card_app().run()