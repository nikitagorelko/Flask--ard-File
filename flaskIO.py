# -*- coding: utf-8 -*-

from flask import render_template

class FlaskIO:
    def __init__(self, request):
        self.form = request.form

    def Input(self, item):
        return self.form.get(item)

    def Output(self, item):
        return render_template('form.tpl', it=item)