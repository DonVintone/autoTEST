class Input:


    def __init__(self, Loc):
        self.Loc = Loc

search = Input('input#search')

print(search.Loc)


class Button:


    def __init__(self, Loc):
        self.Loc = Loc

search = Button('input#Button')

print(Button.Loc)


class Title:


    def __init__(self, Loc):
        self.Loc = Loc

search = Title('input#Title')

print(search.Loc)