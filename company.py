# -*- coding: utf-8 -*-

from flask import render_template
from flask import request
from flaskIO import FlaskIO
from picklestorage import PickleStorage


class Company:
    
    def __init__(self):
        self.storage = PickleStorage(self)
        self.io = FlaskIO(request)
        
    def ShowForm(self, id):
        return self.storage.GetItem(id).Output(self.io)
    
    def ShowCompany(self):
        return render_template('company.tpl', items=self.storage.GetItems())
    
    def Add(self, member_type):
        item = self.storage.GetItem(int(self.io.Input('id')), member_type)
        item.Input(self.io)
        self.storage.Add(item)
        return self.ShowCompany()
    
    def Delete(self, id):
        self.storage.Delete(id)
        return self.ShowCompany()

