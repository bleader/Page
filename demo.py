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

    def footer(self):
        self.opn("<div><h2>footer</h2>")
        self.add("footer")
        self.cls('</div>')

    def menu(self):
        self.opn('<div><h1>Menu</h1>')
        self.add('<a href="/toto">toto</a>', newline=False)
        self.app(' -- ')
        self.app('<a href="/tutu">tutu</a>\n')
        self.cls('</div>')

    def toto(self):
        self.menu()
        self.opn("<div><h2>body</h2>")
        self.add("toto")
        self.cls('</div>')
        self.footer()
        return self.get()

    def tutu(self):
        self.menu()
        self.opn("<div><h2>body</h2>")
        self.add("tutu")
        self.cls('</div>')
        self.footer()
        return self.get()

    def index(self):
        return self.toto()

    index.exposed = True
    toto.exposed = True
    tutu.exposed = True

root = ExamplePage("fr")
root.fr = ExamplePage("fr")
root.en = ExamplePage("en")
cherrypy.quickstart(root, '/', config=None)
