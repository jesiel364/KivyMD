from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

class menulateral(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_pallete = 'BlueGray'

		menu_items = [{
		'viewclass': 'OneLineListItem',
		'text': 'Abrir',
		'on_release': lambda x= 'deu certo': self.menu_callback()
		},
		{'viewclass': 'OneLineListItem',
		'text': 'Novo',
		'on_release': lambda x= '': self.novo()
		}]
		self.menu = MDDropdownMenu(
			items= menu_items,
			width_mult = 3)

	def callback(self, button):
		self.menu.caller = button
		self.menu.open()

	def menu_callback(self):
		self.root.ids.my_label.text = 'Você Pressionou Abrir'
		self.menu.dismiss()
		Snackbar(text = 'Abrindo...').open()

	def novo(self):
		self.root.ids.my_label.text = 'Você Pressionou Novo'
		self.menu.dismiss()
		Snackbar(text = 'Criando...').open()

menulateral().run()