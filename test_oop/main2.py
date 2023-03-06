class Button:
    type = "Кнопка"

    # атрибут экземпляра
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc




    def click(self):
        return "Клик по локатору - {}".format(self.loc)


# создаем экземпляр класса
home = Button("Домой", '/home', 'html>div>button#home')

# вызываемметод экземпляра
print(home.click())

