class Input:
    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text

search = Input('input#search')

print(search.Loc)
print(search.text)


class Button:
    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text

search1 = Button('input#search')
print(search1.Loc)
print(search1.text)

class Title:
    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text


search1 = Input('input#search1')
search2 = Button('input#search2')
search3 = Title('input#search3')
search4 = Link('input#search4')



class Link:

    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text

search1 = Input('input#search1')
search2 = Button('input#search2')
search3 = Title('input#search3')
search4 = Link('input#search4')

print(search.Loc)
print(search.text)
print(search.Loc)
print(search.text)