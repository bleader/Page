""" Helper class to help generate webpages """

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

    p = Page()        # instantiate
    p.opn("<div>")    # open tag: insert and indent following insertions
    p.add("content")  # add content
    p.cls("</div>")   # close tag: deindent and insert closing tag
    p.get()           # close body and html tags

    """

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

    def __init__(self, lang='en', indent=4):
        # content of the page
        self._line = []

        # indent status and count per indent
        self._indent = ""
        self._indent_count = indent

        # set instance language
        self._lang = lang

    def indent(self):
        """indent text that will be inserted with the insertion methods"""
        self._line.append(self._indent_count)

    def deindent(self):
        """Remove a level of indent to insertion methods"""
        self._line.append(-self._indent_count)

    def add(self, line, newline=True):
        """Add an indented line with current indentation
           @param line      The line to be added
           @param newline   Defines if newline is to be inserted
        """
        if newline:
            self._line.append(line + "\n")
        else:
            self._line.append(line)

    def app(self, line):
        """Append a string to the current line, mostly useful after add and
           newline=False use, to finish a given line.
        """
        self._line[-1] = self._line[-1] + line

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

    def head(self):
        """ Prepare header for the page """
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
        self.add('<meta name="description" content="%s" />' %
                 (self._description[self._lang]))

        # stylesheet
        if self._css != None:
            self.add('<link rel="stylesheet" type="text/css" href="%s" />' %
                     (self._css))

        # additionnal headers
        for header in self._additionnal_headers:
            self.add("%s" % (header)) 
        
        self.add('')
        self.cls("</head>")
        self.add('')
        self.opn("<body>")

    def get(self):
        """Return the current page text"""
        page = ""
        tmp = self._line
        self._line = []
        self.head()
        self._line = self._line + tmp
        self.cls("</body>")
        self.cls("</html>")

        indent = ""
        # now we have to generate text from lines
        for line in self._line:
            if isinstance(line, int):
                if line > 0:
                    i = 0
                    while i < line:
                        indent = indent + " "
                        i = i + 1
                else:
                    indent = indent[:line]
            else:
                page = page + indent
                page = page + line
        self._line = []
        return page.strip()
