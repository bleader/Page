class Page:
    """ Page class
    This class is meant to be an abstract class to help generate webpage in
    cherrypy (or other frameworks), by helping creating:
    - header filled at instantiation
    - body filling helpers
    - block indentation
    - default indentation is 4 spaces

    Example Usage
    -------------

    import Page

    p = Page()        # creates and fill the header open body tag
    p.opn("<div>")    # open tag: insert and indent following insertions
    p.add("content")  # add content
    p.cls("</div>")   # close tag: deindent and insert closing tag
    p.get()           # close body and html tags

    """

    # content of the page
    _page = ""

    # indent status and count per indent
    _indent = ""
    _indent_count = 4

    # header
    _doctype = "html"
    _lang = "en"
    _title = "title"
    _content = "text/html"
    _charset = "utf-8"
    _keywords = []
    _description = { 'en': "No description" }
    _css = "/index.css"
    _additionnal_headers = []

    def indent(self):
        """indent text that will be inserted with the insertion methods"""
        i = 0
        while i < self._indent_count:
            self._indent = self._indent + " "
            i = i + 1

    def deindent(self):
        """Remove a level of indent to insertion methods"""
        self._indent = self._indent[:-self._indent_count]

    def add(self, line, newline=True):
        """Add an indented line with current indentation
           @param line      The line to be added
           @param newline   Defines if newline is to be inserted
        """
        self._page = self._page + self._indent + line
        if newline:
            self._page = self._page + "\n"

    def app(self, str):
        """Append a string to the current line, mostly useful after add and
           newline=False use, to finish a given line.
        """
        self._page = self._page + str

    def opn(self, line, newline=True):
        """Used to open an html tag, adding a line containing the tag, and
           indenting the following text so it reflect the opened tag in the
           indentation.
        """
        self.add(line, newline)
        self.indent()

    def cls(self, line, newline=True):
        """Used to close a html tag, deindenting the text, then adding a line
           normally containing the closing tag.
        """
        self.deindent()
        self.add(line, newline)

    def get(self):
        """Return the current page text"""
        self.cls("</body>")
        self.cls("</html>")
        return self._page

    def __init__(self, lang="en", indent=4):
        """ Prepare header for the page """
        self._lang = lang
        self._indent_count = indent
        self.add("<!DOCTYPE %s>" % (self._doctype))
        self.opn('<html lang="%s">' % (self._lang))
        self.opn("<head>")
        self.add('')
        self.add("<title>%s</title>" % (self._title))
        self.add('')
        self.add('<meta http-equiv="Content-Type" content="%s; charset=%s"/>' %
                 (self._content, self._charset))

        # adding keywords
        self.add('<meta name="keywords" content="', newline=False)
        start = True
        for k in self._keywords:
            if start == False:
                self.app(', ') 
            else:
                start = False
            self.app('%s' % (k))
        self.app('" />\n')

        # add description
        self.add('<meta name="description" content="%s" />' % (self._description[self._lang]))

        # stylesheet
        if self._css != None:
            self.add('<link rel="stylesheet" type="text/css" href="%s" />' % (self._css))

        # additionnal headers
        for h in self._additionnal_headers:
            self.add("%s" % (h))
        
        self.add('')
        self.cls("</head>")
        self.add('')
        self.opn("<body>")
