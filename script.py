import requests
from bs4 import BeautifulSoup
import GoogleTrans2020
from googletrans import Translator


# ------------------------------------------------


class sectasy:
    def __init__(self):
        self.oldText = ''
        self.newText = ''
        self.translator = Translator()
        self.track = input("Song name (example: Brennan Savage california): ").replace('-', '').replace('  ', ' ')
        self.transl_ = int(input("Enable Polish translation? ( 1 = ON | 0 = OFF ): "))

        if self.transl_== 1:
            print("\n< Translation included >\n")
        else:
            print("\n< Translation disabled >\n")

        self.track = self.track.replace(' ', '-').replace('&', 'and') + "-lyrics"  # Create link
        self.page = requests.get("https://genius.com/" + self.track)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.MyText = self.soup.select("div[class^='Lyrics__Container']")  # selected element containing text

    def downText(self):
        [s.extract() for s in self.soup(['style', 'script', '[document]', 'head', 'title'])]  # fix syntax
        self.MyText = self.soup.getText()
        fixtext = self.MyText[self.MyText.find("["):self.MyText.find("More on Genius")].strip().find(']')
        if fixtext != -1 and self.MyText[self.MyText.find("["):self.MyText.find("More on Genius")].strip()[
            fixtext + 1] != "\n":
            try:
                self.page = requests.get("https://genius.com/" + self.track)
                self.soup = BeautifulSoup(self.page.content, 'html.parser')
                self.downText()
            except:
                print(self.MyText[self.MyText.find("["):self.MyText.find("More on Genius")].strip() + '\n\n\n')


        else:
            print(self.MyText[self.MyText.find("["):self.MyText.find("More on Genius")].strip() + '\n\n\n')
            self.oldText = self.MyText[self.MyText.find("["):self.MyText.find("More on Genius")].strip()
            if self.transl_ == 1:
                self.translateText()

            # file = open("text.txt", "a+", encoding='utf-8')
            # file.write(self.MyText[self.MyText.find("["):self.MyText.find("More on Genius")].strip())
            # file.close()

    def translateText(self):
        self.newText = self.translator.translate(self.oldText, 'pl').text
        print("Tekst przetłumaczony na język Polski.\n")
        print(self.newText)
        input("ENTER - LEAVE")


genius = sectasy()
genius.downText()
