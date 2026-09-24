class Book:
    """Книгите са готини и яки"""
    def __init__(self,title, ganre):
        self.title = title
        self.ganre = ganre
    def show_ganre(self):
        print(self.ganre)

b1 = Book("Под игото", "Исторически роман")
b1.show_ganre()



