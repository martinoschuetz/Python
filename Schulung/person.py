class Person(object):
# So kann man verhindern dass zur Laufzeit nicht einfach neue Attribute in die Klasse aufgenommen werden.
# Z.B. durch einfache Fehler in der Groß- und Kleinschreibung, z.B. Name vs. name
    __slots__=('__name','__ort','__alter')

    def __init__(self):
#        self.name = "" , Public attribut
        self.__name"", # Privat attribut
		self.__ort = ""
		self.__alter = 0

	def __getAlter(self): return self.__alter
    def __setAlter(self,x):
        if x<1 or x>100:
            print("nein")
            return
        self.__alter=x

    alter property(__getAlter, __setAlter)

    def ausgeben(self):
	    print()
		
if __name_== "__main_":
    p=Persion()
	p.name="bauer"
# wird von der Methode gecheckt.
	p.alter=777777
	p.ausgeben()