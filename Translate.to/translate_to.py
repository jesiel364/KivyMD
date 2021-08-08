from kivymd.app import MDApp
from kivy.core.window import Window
from translate import Translator
from time import sleep

Window.size = 300, 500

class translate_to(MDApp):
	def __init__(self, **kwargs):
		super(translate_to, self).__init__(**kwargs)
		pass

	def trans(self):
		self.root.ids.spin.active = True
		
		print('Status: Rodando...')
		txt = self.root.ids.txt.text
		label = self.root.ids.label
		en = self.root.ids.en
		pt = self.root.ids.pt


		try:
			s = Translator(from_lang = 'pt-br', to_lang = 'english')
			res = s.translate(txt)
			print(res)
			label.text = res
		except Exception as e:
			print(e)
			label.text = 'Não foi possivel traduzir o texto'

		self.root.ids.spin.active = False

	def save_text(self):
		label = self.root.ids.label.text

		try:
			with open('file.txt', 'w') as f:
				f.write(label)
				f.close()
				print('Arquivo \"file.txt\" salvo!')
		except Exception as e:
			print(e)
			print('Ñão foi possivel salvar o arquivo')


translate_to().run()