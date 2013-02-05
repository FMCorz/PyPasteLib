# -*- coding: utf-8 -*-

"""
PyPasteLib

A Python library to format and paste text.

Copyright (c) 2013 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/PyPasteLib
"""

import pasters


def Paster(paster, **kwargs):
    classname = '%sPaster' % paster.capitalize()
    klass = getattr(pasters, classname)
    return klass(**kwargs)

if __name__ == '__main__':
    types = ['raw']
    for t in types:
        p = Paster(t)
        p.add('''
        <?php
        if (false) {
          // Blah!
        }''', identifier='P H P')

        p.add('''
        if True:
          pass
        sys.exit()
        ''', identifier='P Y T H O N', syntax='py')

        p.add('''
        (function() {
          alert('\o/');
        })()
        ''', identifier='J A V A S C R I P T', syntax='javascript')

        p.add(u'Frédéric\'s unicode string', identifier='Unicode string')
        p.add('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\n' +
            'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\n' +
            'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n' +
            'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\n' +
            'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\n' +
            'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        print p.paste()
