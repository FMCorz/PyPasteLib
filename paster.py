# -*- coding: utf-8 -*-

def paster(paster, **kwargs):
	classname = '%sPaster' % paster.capitalize()
	mod = __import__('pasters.%s' % paster, fromlist = [ classname ])
	klass = getattr(mod, '%sPaster' % paster.capitalize())
	return klass(**kwargs)
