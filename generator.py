#from IPython.display import Image as IPYImage
import os
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Meme:
    def __init__(self):
        self._format = self.__class__.__name__.lower() if self.__class__.__name__.lower() != 'meme' else None
        try:
            self.template_path = f"templates/{self._format}.jpg"
            self.image = Image.open(self.template_path)
        except FileNotFoundError:
            self.template_path = None
            self.image = None

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, name: str):
        self._format = name
        self.template_path = f"templates/{self._format.lower()}.jpg"
        self.image = Image.open(self.template_path)

    def reset(self):
        self.image = Image.open(self.template_path)

    def draw(self, text: str, x: int, y: int, font_size: int = 45):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('Roboto-Bold.ttf', size=font_size)
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), text, fill=color, font=font)
        return self.image

    def __str__(self):
        return f"<\"{self._format}\" Meme>"

    def __repr__(self):
        return f"<\"{self._format}\" Meme>"


class BertStrip(Meme):
    def draw_text_1(self, text, font_size=30):
        return self.draw(text, 20, 480, font_size)


class Drake(Meme):
    def __init__(self):
        self._text_1 = ""
        self._text_2 = ""
        super().__init__()

    @property
    def text_1(self):
        return self._text_1

    @text_1.setter
    def text_1(self, text):
        self._text_1 = text
        self.draw_text_1(text)

    @property
    def text_2(self):
        return self._text_2

    @text_2.setter
    def text_2(self, text):
        self._text_2 = text
        self.draw_text_2(text)

    def draw_text_1(self, text, font_size=45):
        return self.draw(text, 335, 20, font_size)

    def draw_text_2(self, text, font_size=45):
        return self.draw(text, 335, 300, font_size)


class ChangeMyMind(Meme):
    def __init__(self):
        self._text_1 = ""
        super().__init__()

    @property
    def text_1(self):
        return self._text_1

    @text_1.setter
    def text_1(self, text):
        self._text_1 = text
        self.draw_text_1(text)

    def draw_text_1(self, text, font_size=45):
        return self.draw(text, 300, 320, font_size)


class ModernProblems(Meme):
    def __init__(self):
        self._text_1 = ""
        super().__init__()

    @property
    def text_1(self):
        return self._text_1

    @text_1.setter
    def text_1(self, text):
        self._text_1 = text
        self.draw_text_1(text)

    def draw_text_1(self, text, font_size=45):
        return self.draw(text, 20, 20, font_size)


class FBIText(Meme):
    def __init__(self):
        self._text_1 = ""
        super().__init__()

    @property
    def text_1(self):
        return self._text_1

    @text_1.setter
    def text_1(self, text):
        self._text_1 = text
        self.draw_text_1(text)

    def draw_text_1(self, text, font_size=35):
        return self.draw(text, 20, 270, font_size)


available_memes = [FBIText, ModernProblems, ChangeMyMind, Drake, BertStrip]


def generate_random_collection(number=30):
    collection = []
    for i in range(0, number):
        random_meme = random.choice(available_memes)
        collection.append(random_meme())

    return collection


my_meme_collection = generate_random_collection()
