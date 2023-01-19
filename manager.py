# -*- coding: utf-8 -*-

from dataclasses import dataclass
from employee import Employee

@dataclass
class Manager(Employee):
    current_project: str = ""
    department: str = ""
     
    def Input(self, io):
        Employee.Input(self, io)
        self.current_project = io.Input('current_project')
        self.department = io.Input('department')
        