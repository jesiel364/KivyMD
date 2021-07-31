from kivymd.app import MDApp

class Mini(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_pallete = 'Dark_Blue'
	
Mini().run()