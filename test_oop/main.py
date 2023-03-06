class Button:
    type = "Кнопка"

    # атрибут экземпляра
    def __init__(self, text, link):
        self.text = text
        self.link = link





#создаем экземпляр класса
home = Button("Домой", '/home')
catalog_msc = Button("Каталог товаров в Москве", '/msk/catalog')

# получаем доступ к атрибутам класса
print("home - {}".format(home.__class__.type))
print("catalog_msc тоже {}".format(catalog_msc.__class__.type))

# получаем достууп к атрибутам экземпляра
print("Кнопка \"{}\" имеет ссылку \"{}\"".format(home.text, home.link))
print("Кнопка \"{}\" имеет ссылку \"{}\"".format(catalog_msc.text, catalog_msc.link))




