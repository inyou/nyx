#!/usr/bin/python
# coding: utf8
import pickle
class analyser():
    def __init__(self):
        self.tab=[]
    def add_qr(self,q,r):
        self.tab.append([q,r])
    def find(self,q):
        for i in self.tab:
            if i[0]==q:
                return i[1]
        return -1
    def charge(self,s):
        with open(s, 'r') as fichier:
            mon_pickler = pickle.Unpickler(fichier)
            self.tab=mon_pickler.load()
        
    def save(self,s):
        with open(s, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            pickle.dump(self.tab,fichier)#,pickle.HIGHEST_PROTOCOL)
    def affiche(self):
        print self.tab