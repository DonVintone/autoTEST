from selenium import webdriver


class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        driver = webdriver.Chrome()
        driver.get(self.url)


home = Page("http://forum.ru-board.com/board.cgi")
home.get()

# home=page