from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

class List(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_pallete = 'BlueGray'

	def on_start(self):
		for i in range(20):
			self.root.ids.container.add_widget(
				OneLineListItem(text=f"Single-line item {i}")
				)

List().run()