# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:14:27 2022

@author: Bars
"""
from dataclasses import dataclass
import os, sys, re, codecs, binascii, pickle


from flask import Flask, g, request


app = Flask(__name__)
if __name__ == '__main__':
    from company import Company
else:
    from .company import Company

def GetCompany():
    if 'company' not in g:
        g.company = Company()
    return g.company

@app.route("/")
def companyindex():
    return GetCompany().ShowCompany()

@app.route("/showform/<int:id>")
def showform(id):
    return GetCompany().ShowForm(id)

@app.route("/delete/<int:id>")
def deleteitem(id):
    return GetCompany().Delete(id)

@app.route("/add", methods=['POST'])
def add():
    project = request.form.get('current_project')
    subordinates = request.form.get('current_subordinates')
    if project == '' and subordinates == 0:
        return GetCompany().Add(0)
    elif subordinates == '':
        return GetCompany().Add(1)
    else:
        return GetCompany().Add(2)
        
@app.teardown_appcontext
def teardown_book(ctx):
    GetCompany().storage.Store()

if __name__ == "__main__":
    app.run(debug=True)