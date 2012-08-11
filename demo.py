#!/usr/bin/env python2

import cherrypy
from Page import *

class ExamplePage(Page):
    _keywords = [ "ExamplePage", "test", "demo", "raccoons" ]
    _description = {
        'en': 'This is a complet example of cherrypy page using the Page module',
        'fr': 'Ceci est un exemple complet de page cherrypy utilisant le module Page'
    }
    _title = 'ExamplePage Demo (this will show in your brouwser title bar)'
    _css = None

    def get(self):
        self.footer()
        return Page.get(self)

    def __init__(self, lang='en'):
        Page.__init__(self, lang=lang)
        self.menu()

    def footer(self):
        self.opn("<div>")
        self.add("footer")
        self.cls('</div>')

    def menu(self):
        self.opn('<div>')
        self.add('<a href="/toto">toto</a>', newline=False)
        self.app(' -- ')
        self.app('<a href="/tutu">tutu</a>')
        self.cls('</div>')

class ExampleServer():
    lang = 'en'
    def __init__(self, lang='en'):
        self.lang = lang

    def toto(self):
        pg = ExamplePage(self.lang)
        pg.opn("<div>")
        pg.add("toto")
        pg.cls('</div>')
        return pg.get()

    def tutu(self):
        pg = ExamplePage(self.lang)
        pg.opn("<div>")
        pg.add("tutu")
        pg.cls('</div>')
        return pg.get()

    def index(self):
        return self.toto()

    index.exposed = True
    toto.exposed = True
    tutu.exposed = True

root = ExampleServer("fr")
root.fr = ExampleServer("fr")
root.en = ExampleServer("en")
cherrypy.quickstart(root, '/', config=None)
