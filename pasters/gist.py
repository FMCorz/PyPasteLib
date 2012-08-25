# -*- coding: utf-8 -*-

import httplib
import json
from base import BasePaster

class GistPaster(BasePaster):

	_ssl = True
	_method = 'POST'
	_api = 'api.github.com'
	_uri = '/gists'

	def paste(self):
		data = {
			'description': self.description(),
			'public': not self.private(),
			'files': self.prepare()
		}

		data = json.dumps(data)
		headers = { 'Content-Type': 'application/json' }
		(resp, d, h) = self.httpRequest(
				host=self._api,
				uri=self._uri,
				method=self._method,
				ssl=self._ssl,
				headers=headers,
				data=data
			)

		if resp.status == 201:
			data = json.loads(d)
			return data.get('html_url', False)
		else:
			print resp.status, resp.reason
			return False

	def get_filename(self, identifier, syntax = None):
		identifier = str(identifier).replace('/', '_')
		if syntax != None:
			ext = '.' + syntax.lower()
			if not identifier.endswith(ext):
				identifier += ext
		return identifier

	def prepare(self):
		d = {}
		i = 0
		for t in self.texts():
			i += 1
			identifier = t.get('identifier', None) if t.get('identifier', None) != None else i
			identifier = self.get_filename(identifier, self.prepare_syntax(syntax = t.get('syntax', None)))
			d[identifier] = { 'content': str(t.get('text', '')) }
		return d

	syntaxes = [
		'txt',            	# Plain Text
		'as',              	# ActionScript
		'c',          		# C
		'cs',         		# C#
		'cpp',            	# C++
		'lisp',           	# Common Lisp
		'css',            	# CSS
		'diff',           	# Diff
		'el',         		# Emacs Lisp
		'erl',            	# Erlang
		'hs',         		# Haskell
		'html',           	# HTML
		'java',           	# Java
		'js',         		# JavaScript
		'lua',            	# Lua
		'm',          		# Objective-C
		'pl',         		# Perl
		'php',            	# PHP
		'py',         		# Python
		'rb',         		# Ruby
		'scala',          	# Scala
		'scm',            	# Scheme
		'sql',            	# SQL
		'tex',            	# TeX
		'xml',            	# XML
		'adb',            	# Ada
		'cls',            	# Apex
		'applescript',		# AppleScript
		'arc',            	# Arc
		'ino',            	# Arduino
		'asp',            	# ASP
		'asm',            	# Assembly
		'aug',            	# Augeas
		'ahk',            	# AutoHotkey
		'bat',            	# Batchfile
		'befunge',			# Befunge
		'bmx',				# BlitzMax
		'boo',				# Boo
		'b',				# Brainfuck
		'bro',				# Bro
		'c-objdump'         # C-ObjDump
		'chs',            	# C2hs Haskell
		'ceylon',         	# Ceylon
		'ck',         		# ChucK
		'clj',            	# Clojure
		'cmake',          	# CMake
		'coffee',         	# CoffeeScript
		'cfm',            	# ColdFusion
		'coq',            	# Coq
		'cppobjdump',		# Cpp-ObjDump
		'feature',			# Cucumber
		'pyx',           	# Cython
		'd',          		# D
		'd-objdump',		# D-ObjDump
		'darcspatch',		# Darcs Patch
		'dart',           	# Dart
		'dasm16',         	# DCPU-16 ASM
		'pas',            	# Delphi
		'dylan',          	# Dylan
		'ec',         		# eC
		'epj',            	# Ecere Projects
		'e',          		# Eiffel
		'ex',         		# Elixir
		'fs',         		# F#
		'factor',         	# Factor
		'fy',         		# Fancy
		'fan',            	# Fantom
		'f90',            	# FORTRAN
		's',          		# GAS
		'kid',            	# Genshi
		'ebuild',         	# Gentoo Ebuild
		'eclass',         	# Gentoo Eclass
		'po',         		# Gettext Catalog
		'go',         		# Go
		'gs',         		# Gosu
		'man',            	# Groff
		'groovy',         	# Groovy
		'gsp',            	# Groovy Server Pages
		'haml',           	# Haml
		'hx',         		# HaXe
		'mustache',			# HTML+Django
		'erb',            	# HTML+ERB
		'phtml',          	# HTML+PHP
		'ini',            	# INI
		'io',         		# Io
		'ik',         		# Ioke
		'irclog',         	# IRC log
		'jsp',            	# Java Server Pages
		'json',           	# JSON
		'jl',         		# Julia
		'kt',         		# Kotlin
		'ly',         		# LilyPond
		'lhs',            	# Literate Haskell
		'll',         		# LLVM
		'lgt',            	# Logtalk
		'mak',            	# Makefile
		'mako',           	# Mako
		'md',         		# Markdown
		'matlab',         	# Matlab
		'mxt',            	# Max
		'minid',          	# MiniD
		'druby',          	# Mirah
		'moo',            	# Moocode
		'mu',         		# mupad
		'myt',            	# Myghty
		'n',          		# Nemerle
		'nim',            	# Nimrod
		'nu',         		# Nu
		'numpy',          	# NumPy
		'objdump',			# ObjDump
		'j',          		# Objective-J
		'ml',         		# OCaml
		'ooc',            	# ooc
		'opa',            	# Opa
		'cl',         		# OpenCL
		'p',          		# OpenEdge ABL
		'parrot',         	# Parrot
		'pasm',           	# Parrot Assembly
		'pir',            	# Parrot Internal Representation
		'ps1',            	# PowerShell
		'prolog',         	# Prolog
		'pp',         		# Puppet
		'pd',         		# Pure Data
		'pytb',           	# Python traceback
		'r',          		# R
		'rkt',            	# Racket
		'raw',            	# Raw token data
		'rebol',          	# Rebol
		'cw',         		# Redcode
		'rst',            	# reStructuredText
		'rhtml',          	# RHTML
		'rs',         		# Rust
		'sage',           	# Sage
		'sass',           	# Sass
		'sci',            	# Scilab
		'scss',           	# SCSS
		'self',           	# Self
		'sh',         		# Shell
		'st',         		# Smalltalk
		'tpl',            	# Smarty
		'sml',            	# Standard ML
		'sc',         		# SuperCollider
		'tcl',            	# Tcl
		'tcsh',           	# Tcsh
		'tea',            	# Tea
		'textile',			# Textile
		't',          		# Turing
		'twig',           	# Twig
		'vala',           	# Vala
		'v',          		# Verilog
		'vhdl',           	# VHDL
		'vim',            	# VimL
		'vb',         		# Visual Basic
		'xquery',         	# XQuery
		'xs',         		# XS
		'xslt',           	# XSLT
		'yml'            	# YAML
	]