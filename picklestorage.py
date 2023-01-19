# -*- coding: utf-8 -*-

import pickle
from employee import Employee
from manager import Manager
from director import Director
 
class PickleStorage:
    def __init__ (self, company):
        self.company = company
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0
             
    def Load(self):
        with open('company.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)
             
    def Store(self):
        with open('company.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)
    
    def GetItem(self, id, member_type = 0):
        if id <= 0:
            if member_type == 0:
                return Employee()
            elif member_type == 1:
                return Manager()
            elif member_type == 2:
                return Director()
        else:
            return self.items[id]
        
    def Add(self, item):
        if item.id <= 0:
            self.maxid += 1;
            item.id = self.maxid
            self.items[item.id] = item
            
    def Delete(self, id):
        del self.items[id]
        
    def GetItems(self):
        for(id, item) in self.items.items():
            yield(item)