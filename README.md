PyPasteLib
==========

A Python library to format and paste text.

Usage
-----

Simply create an instance of the paster, add the texts, set its options and paste! 
If a paster does not support an option, the option will be ignored.

### Paste on gist

    from PyPasteLib import Paster
    paster = Paster('gist')
    paster.add('<?php phpinfo(); ?>', identifier='file.php')
    paster.add('import os', syntax='python')
    paster.add('I love blue cheese \o/', syntax='text')
    paster.syntax('php')
    paster.ttl(60 * 24 * 365)       # Is ignored by Gist
    print paster.paste()

Returns [https://gist.github.com/4714518](https://gist.github.com/4714518)

### Paste on pastebin

The only change to make is adding the API key to the constructor.

    paster = Paster('pastebin', settings={'apikey': 'XXX'})
    [...]

Returns [http://pastebin.com/4p6bHMac](http://pastebin.com/4p6bHMac)

Pasters supported
-----------------

- [Code Vault](http://cdv.lt)
- [gist](https://gist.github.com/)
- [Hey! Paste it](http://www.heypasteit.com/)
- [KDE](http://paste.kde.org)
- [Mozilla](http://pastebin.mozilla.org)
- [Paste2.org](http://paste2.org)
- [PasteBay](http://pastebay.net)
- [pastebin](http://pastebin.com)
- [Pastee](https://pastee.org)
- [Pastie](https://pastie.org)
- [Slexy](https://slexy.org)
- [SnipSource](http://snipsource.com)
- [Ubuntu](http://paste.ubuntu.com)

API
---

In a nutshell, here are a few details on how to use the library. Please explore the class BasePaster for better understanding.

### Paster(type, **kwargs)

Use this function to return a Paster object. The keyword arguments can be one of the options (described below).

### Paster.add(text, identifier=None, syntax=None)

This is the second most import method, it adds the text to be pasted. You can call this method multiple times before proceeding to the paste, if the paster handles it multiple files will be created, if not then a single file will contain all the text buffered.

- text: The content to paste. It should either be a unicode or a UTF-8 encoded string;
- identifier: The file name of the file, or separator name;
- syntax: If the paster supports it, the syntax of the file.

### Paster.paste()

The most important method, which will format the content, paste it online and return the URL.

### Options

Each of the following can be set in the constructor, or using their dedicated methods. They can be set for any paster, but only apply when the paster can support it.

- description: The description of the paste;
- password: The password required to access the paste;
- poster: The name of the author of the paste;
- private: Whether or not the paste should be private;
- setting: Used to pass extra value to the paster. The constructor keyword is _settings_ and expects a dict;
- syntax: The global syntax of the paste;
- ttl: The number of minutes the paste should be valid for, will be rounded at the closest higher value (or infinite).

Write your own pasters
----------------------

Write your own pasters using the base class BasePaster. The only method that you aboslutely have to extend is paste() which should return the URL (or whatever you want to return) of the formatted text. If you have to send an HTTP request to a server, use the method httpRequest() defined in the base class.

There are some values which need to be converted depending on the paster. For example _ttl_ is stored in minutes, but the paster might expect a value in days. If you need to change those values, you should declare functions such as prepare_ttl() or prepare_private(), and call them while building your request in paste().

You have to define what syntaxes codes your paster accepts, this is done in the class variable _syntaxes_. As the names are not always the same from one paster to another, the base class defines prepare_syntax() which tries to match the user defined syntax with one of the syntaxes your paster expects. For example, your user sets the syntax 'cpp' but your paster expects 'c++', the magic will happen and prepare_syntax() will return 'c++'.

Disclaimer
----------

PyPasteLib authors cannot be make responsible for any use of the library. It has been developed for fun, and should not serve evil purposes! You don't want to see captcha codes coming, do you?

License
-------

Licensed under the [MIT License](http://www.opensource.org/licenses/mit-license.php)