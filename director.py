# -*- coding: utf-8 -*-

from dataclasses import dataclass
from manager import Manager

@dataclass
class Director(Manager):
    current_subordinates: int = 0
    
    def Input(self, io):
        Manager.Input(self, io)
        self.current_subordinates = io.Input('current_subordinates')

        