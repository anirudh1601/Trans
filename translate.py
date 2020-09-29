from googletrans import Translator


class Hello(object):
	def __init__(self,word,lang):
		self.word=word
		self.lang=lang
		self.cursor=Translator(service_urls=["translate.google.com"])

	def __repr__(self):
		translated=self.cursor.translate(self.word,dest=self.lang).text
		return str(translated)



translate=input("enter the text")
lang="tamil"
print(Hello(translate,lang))
