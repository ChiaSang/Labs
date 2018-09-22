#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:30:48 2018
@author: ChiaS
"""

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()