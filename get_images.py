
from easygui import *
import sys
import os
import wget
import webbrowser
import re
from bs4 import BeautifulSoup
from datetime import date


imagem_hoje = "imagem-do-dia.jpg"

if os.path.exists(imagem_hoje):
    os.remove(imagem_hoje)
else:
    print("")

filepath1 = "image.json"

if os.path.exists(filepath1):
    os.remove(filepath1)
else:
    print("")

url = "https://apod.nasa.gov/apod/"
hoje = date.today()
hoje_formatado = hoje.strftime('%Y %B %d')

filename = wget.download(url, out="image.json")

with open("image.json", "r") as f:

    for lines in f:
        html =  f.read()

    soup = BeautifulSoup(html, "html.parser")

    imagem_do_dia = url+soup.find(text=re.compile(hoje_formatado)).previous.find('img').attrs['src']

    # print(soup.find(text=re.compile(hoje_formatado)).previous.find('img').attrs['src'])

    filename1 = wget.download(
            imagem_do_dia, out=imagem_hoje
        )
