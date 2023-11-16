
import tkinter as tk
import requests 
from bs4  import BeautifulSoup

# Scrape the Web 
url = 'http://www.cnn.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.findAll('span', class_='container__headline-text')

def print_news():
    num_list = 0
    for headline in headlines:
        num_list += 1
        print(f"{num_list} >>>{headline.text.strip()} \n")
       
         
class CNN_NewsApp:
    def __init__(self,root):
        self.root = root
        self.root.title("CNN News Headlines, Jesus please continue to take care of Your Children")
        self.root.geometry('400x300')

        #create a scrollbar 
        scrollbar =tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Create a Listbox and link it to the Scrollbar
        self.listbox = tk.Listbox(root, yscrollcommand= scrollbar.set, width=375)
        self.listbox.pack(side=tk.LEFT, fill =tk.BOTH)
        scrollbar.config(command=self.listbox.yview)

        #Display CNN Headlines 
        self.print_news()
        #functions

    def print_news(self):
        num_list = 0
        for headline in headlines:
            num_list += 1
            #print(f"{num_list} >>>{headline.text.strip()} \n")
            self.listbox.insert(tk.END,f"{num_list} >>>{headline.text.strip()} \n" )

if __name__ =="__main__":
    root = tk.Tk()
    app = CNN_NewsApp(root)
    root.mainloop()