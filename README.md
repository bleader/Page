Page
====

Page module helper to generate webpages for cherrypy and other frameworks.

Introduction
------------

The idea behind this module to help the creation of page for frameworks like
cherrypy and alike. To sum up the usage, just create a page inheriting from
this, fill default values for what you want to change, instantiate it, add
content (body of webpage), and .get() the page to pass it to your framework.

Usage
-----

The simplest way to start is to create a class that will inherit from Page
class, and set the various fields you want to customize.

```python
from Page import *

class MyPage(Page):
    _keywords = [ "mypage", "demo", "raccoons" ]
    _description = {
            'en': 'this is the english description of my webpage',
            'fr': 'voici la description en francais de ma page web'
    }
    
# instantiate a page telling the language will ben english, which is the default
# this will set doctype, open <html> tag, create <head> and its content
# close </head>, open <body> 
p = MyPage(lang='fr') # page in french
p = MyPage(lang='en') # page in english
p = MyPage(indent=3)  # used default lang (en), and set indent to 3 spaces, instead of 4

# assume we fill content of body here, we then get the page to pass
# it to the framework, for demo print it here.
print(p.get())
```

This will result in this:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        
        <title>title</title>
        
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="keywords" content="" />
        <meta name="description" content="No description" />
        <link rel="stylesheet" type="text/css" href="/index.css" />
        
    </head>
    
    <body>
    </body>
</html>
```

Provided
--------

Here are the values you can set and their default values:

- _doctype = "html"  -- Define the !<DOCTYPE %s> field
- _lang = "en"  -- language of the page, for <html lang=%s> field
- _title = "title"  -- <title>
- _content = "text/html"  -- content type of the page
- _charset = "utf-8"  -- charset used for the webpage
- _keywords = []  -- list of keywords
- _description = { 'en': "No description" }  -- dict of page description, the one matching the lang
  set in when instantiating your class.
- _css = "/index.css"  -- link to the css, only one supported for now
- _additionnal_headers = []  -- list of full custom lines to be added in the <head>

And here are the methods that can be used on your class to fill the webpage:


- indent(): Indent text that will be inserted with the insertion methods and the amount of spaces
            defined by the instance.
- deindent(): Remove a level of indent to insertion methods
- add(line, newline=True): Add an indented line with current indentation
    - line:    The line to be added
    - newline: Defines if newline is to be inserted, default to true
- app(str): Append a string to the current line, mostly useful after using the add plus
            newline=False to finish a started line
- opn(line, newline=True): Used to open an html tag, adding a line containing the tag, and indenting
                           the following text so it reflect the opened tag in the indentation.
- cls(line, newline=True): Used to close a html tag, deindenting the text, then adding a line
                           normally containing the closing tag.
- get(): Close </body> and </html>, and returns the page as it is

