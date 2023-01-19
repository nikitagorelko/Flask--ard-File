# -*- coding: utf-8 -*-

from dataclasses import dataclass
from flaskIO import FlaskIO

@dataclass
class Employee:
    id: int = 0
    name: str = ""
    surname: str = ""
    age: int = 0
        
     
    def Input(self, io):
        self.id = int(io.Input('id'))
        self.name = io.Input('name')
        self.surname = io.Input('surname')
        self.age = int(io.Input('age'))
        
    def Output(self, io):
        return io.Output(self)
