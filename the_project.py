# -*- coding: utf-8 -*-
from selenium.webdriver import webdriver
from Tkinter import *


CHROME_PATH = r'C:\Users\Administrator\startmenu\Desktop\nand2tetris\chromedriver.exe'


def create_window():
    app = Tk()
    app.title("the name of our project")
    app.geometry("600x300+400+300")
    app.configure(bg="purple")
    lbl = Label(app, text='Please enter the relevant url: ', height=10)
    lbl.pack()
    e = Entry(app)
    e.pack()
    url = e.get()
    app.mainloop()
    return url


def main():
    url = create_window()
    #if the teacher is coming...
    driver = webdriver.Chrome(CHROME_PATH)
    driver.get(url)
    driver.quit()

if __name__ == '__main__':
    main()