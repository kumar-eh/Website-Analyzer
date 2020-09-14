#Importing package for Gui warning box , url check
from tkinter import * 
from tkinter.messagebox import *
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer
import requests
from nltk.tokenize import RegexpTokenizer
import re
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.util import ngrams
from collections import Counter
import itertools
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import csv
from tkinter.ttk import Progressbar
import time
from tkinter.filedialog import askopenfile
import os
from tld import get_fld

global stemmed
def userText(event):
    e.delete(0 , END)
    usercheck = TRUE


def displaylinks():
    global linkasbc
    for listitem in linksabc:
        linkframe.insert(1,listitem)

def Tagcloud():
    global stemmed
    reader_ob = csv.reader(stemmed) 
    reader_contents = list(reader_ob) 
    text = "" 
    for row in reader_contents : 
            for word in row :  
                    text = text + " " + word                   
    our_mask = np.array(Image.open('coudmask.png'))
    tagcloud = WordCloud(background_color="white", mask = our_mask , max_words=20).generate(text)
    plt.imshow(tagcloud)
    plt.tight_layout(pad = 3)
    plt.margins(x=0, y=0)
    plt.axis('off')
    plt.show()



    
#To check if its a valid url and extracting links
def UrlCheck(e):
        links = []
        texts = []
        global stemmed
        global linksabc
        result = urlparse(e)
        a = all([result.scheme, result.netloc, result.path])
        if(a == True):
            suffix = '/'
            if(e.endswith(suffix)):
                e = e[:len(e)-len(suffix)]
          
            page = requests.get(e)    
            data = page.text
            soup = BeautifulSoup(data , features="html.parser")

            for link in soup.find_all('a'):
                text = soup.find_all(text=True)
                links.append(link.get('href'))

            linksabc = list(dict.fromkeys(links))
            l2.config(text = len(linksabc))

            a = len(get_fld(e))
            l7.config(text = a)
            
            html_page = page.content
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)
            output = ''
            blacklist = ['[document]','noscript','header','html','meta','head', 'input','script','style' ,'li' , 'b' , 'href' , 'div' , 'th']
            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)
            res = len(output.split())
            l4.config(text = res)

            tokens = word_tokenize(output)  #splitting
            # convert to lower case
            tokens = [w.lower() for w in tokens]
            # remove punctuation from each word
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in tokens]
            # remove remaining tokens that are not alphabetic
            words = [word for word in stripped if word.isalpha()]
            # filter out stop words
            stop_words = set(stopwords.words('english'))
            words = [w for w in words if not w in stop_words]

            porter = PorterStemmer()
            stemmed = [porter.stem(word) for word in words]

            res = [key for key, value in Counter(stemmed).most_common()]
            key1.config(text = res[0])
            key2.config(text = res[1])
            key3.config(text = res[2])
            key4.config(text = res[3])
            key5.config(text = res[4])
            key6.config(text = res[5])
            key7.config(text = res[6])
            key8.config(text = res[7])
            key9.config(text = res[8])

            
        else:
            print(showwarning("Alert" , "No such website or url exists"))
#For gui
root = Tk()
usercheck = FALSE

root.title("Website Analyzer")

c = Canvas(root , width = 750 , height = 700 , bg = "#052378")
c.pack()

p= PhotoImage(file="finallogo.png" , width = 190 , height = 80)
bglabel=Label(c, image=p)
bglabel.place(relx = 0.5 , rely = 0.01 , anchor = 'n')


#Frame which contains Entry widget and Enter button
f = Frame(c , bg = '#052378')  
f.place(relx = 0.53 , rely=0.17, relheight = 0.10, relwidth = 0.8, anchor= 'n')

l = Label(f , text = "*Start with http or https" , bg = "#052378" , fg = "white")
l.place(relx = 0.39 , rely = 0.76)


#Widget which lets user enter the url
e = Entry(f , bg = '#66fcf1')
e.insert(0, "Enter url here")
e.bind("<Button>", userText)
e.place(relx = 0.05 , rely = 0.5 , relheight = 0.6 , relwidth = 0.6 , anchor = 'w')


#To enter after entering a url
b = Button(f , text = "Submit" , bg = "#66fcf1" , command = lambda : UrlCheck(e.get()))
b.place(relx = 0.7 , rely = 0.2 , relheight = 0.65 , relwidth = 0.2 )


#frame which contains cloud label
cloudframe = Frame(c , bg = "#66fcf1" )  
cloudframe.place(relx = 0.5 , rely=0.30 , relheight = 0.6 , relwidth = 0.8, anchor= 'n')

l1 = Label(cloudframe , text = "Number of distinct links : " , bg = "#66fcf1")
l1.place(relx = 0.01 , rely = 0.05  ,  anchor = 'w')

l2 = Label(cloudframe , bg ="#66fcf1")
l2.place(relx = 0.275 , rely = 0.05 ,relwidth = 0.07 , anchor = 'w')

l3 = Label(cloudframe , text = "Total number of words in the webpage : " , bg = "#66fcf1")
l3.place(relx = 0.01  ,rely = 0.15 , anchor = 'w')

l4 = Label(cloudframe , bg = "#66fcf1")
l4.place(relx = 0.55  ,rely = 0.15 ,relwidth = 0.1 , anchor = 'e')

l5 = Label(cloudframe , text = "Top 09 Key Words" ,  bg ="#66fcf1")
l5.place(relx = 0.85 , rely = 0.05 , anchor = 'e')

l6 = Label(cloudframe , text = "Number of pages at the top level :" , bg  = "#66fcf1")
l6.place(relx= 0.01 , rely = 0.25 , anchor ='w')

l7 = Label(cloudframe , bg = "#66fcf1")
l7.place(relx = 0.38 , rely = 0.25 ,relwidth = 0.1 ,  anchor = 'w')

key1 = Label(cloudframe , bg = "#66fcf1")
key1.place(relx = 0.85 , rely = 0.15 , anchor = 'e')

key2 = Label(cloudframe , bg = "#66fcf1")
key2.place(relx = 0.85 , rely = 0.25 , anchor = 'e')

key3 = Label(cloudframe , bg = "#66fcf1")
key3.place(relx = 0.85 , rely = 0.35 , anchor = 'e')

key4 = Label(cloudframe , bg = "#66fcf1")
key4.place(relx = 0.85 , rely = 0.45 , anchor = 'e')

key5 = Label(cloudframe , bg = "#66fcf1")
key5.place(relx = 0.85 , rely = 0.55 , anchor = 'e')

key6 = Label(cloudframe , bg = "#66fcf1")
key6.place(relx = 0.85 , rely = 0.65 , anchor = 'e')

key7 = Label(cloudframe , bg = "#66fcf1")
key7.place(relx = 0.85 , rely = 0.75 , anchor = 'e')

key8 = Label(cloudframe , bg = "#66fcf1")
key8.place(relx = 0.85 , rely = 0.85 , anchor = 'e')

key9 = Label(cloudframe , bg = "#66fcf1")
key9.place(relx = 0.85 , rely = 0.95 , anchor = 'e')

try:
    wordtag = Button(cloudframe , text = "Generate word cloud " , fg = "#052378" , command = lambda : Tagcloud())
    wordtag.place(relx = 0.03 , rely = 0.35)
except :
    print(showwarning("Alert" , "Enter a url first"))

Displaylinks = Button(cloudframe , text = "Display the links of the website" , fg = "#052378" , command = lambda : displaylinks())
Displaylinks.place(relx = 0.03 , rely = 0.45)

linkframe = Listbox(cloudframe , bg = "#66fcf1")
linkframe.place(relx = 0.03 , rely = 0.75 , relwidth = 0.33 , relheight = 0.4 , anchor = 'w')
scrollbar = Scrollbar(linkframe , bg = "#66fcf1")
scrollbar.pack(side=RIGHT, fill=Y)
linkframe.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = linkframe.yview)

root.mainloop()

