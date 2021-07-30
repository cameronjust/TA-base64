#!/usr/bin/env python
# coding=utf-8

import sys, os, math
from base64 import b64decode, b64encode

splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'TA-base64', 'lib'))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators
from splunklib.six.moves import range


@Configuration()

class B64Command(StreamingCommand):
	"""
	Encode a string to Base64
	Decode a Base64 content

	 | base64 [action=(encode|decode)] field=<field> [mode=(replace|append)] [special_chars=(keep|remove|hash)]
	 """

	field  = Option(name='field',  require=True)
	action = Option(name='action', require=False, default="encode")
	mode   = Option(name='mode',   require=False, default="replace")
	special_chars = Option(name='special_chars',   require=False, default="keep")
	convert_newlines = Option(name='convert_newlines', require=False, default=True, validate=validators.Boolean())
	fix_padding = Option(name='fix_padding', require=False, default=True, validate=validators.Boolean())
	suppress_error = Option(name='suppress_error', require=False, default=False, validate=validators.Boolean())

	def stream(self, events):
		module = sys.modules['base64']

		if self.action == "decode" :
			fct = "b64decode"
		else:
			fct = "b64encode"

		if self.mode == "append" :
			dest_field = self.field + "_base64"
		else:
			dest_field = self.field

		for event in events:
			
			if not self.field in event :
				continue

			try:

				if fct == "b64encode":
					# Convert to bytestring if encode and the field is a string
					if isinstance(event[self.field], str):
						original = event[self.field].encode("utf-8")
					else:
						original = event[self.field]

				if fct == "b64decode":
					# Fix padding
					if self.fix_padding:
						original = event[self.field].ljust((int)(math.ceil(len(event[self.field]) / 4)) * 4, '=')
					else:
						original = event[self.field]

					
				ret = getattr(module, fct)( original )

				# replace unpritable characters by their hexadecimal 
				# representation. Example: \x00
				event[ dest_field ] = ""
				for c in ret:
				
					x = c
					if c < ord(' ') or c > ord('~') :
						if self.convert_newlines and c == 10:
							x = "\n"
						elif self.convert_newlines and c == 13:
							x = "\r"
						elif self.special_chars == "remove":
							continue
						elif self.special_chars == "hash":
							x = "#"
						elif self.special_chars == "star":
							x = "*"
						else:
							x = "\\x" + "{0:02x}".format(c)
					else:
						x = chr(x)
						
					event[ dest_field ] += x
	
			except Exception as e:
				if not self.suppress_error :
					raise e

			yield event

dispatch(B64Command, sys.argv, sys.stdin, sys.stdout, __name__)

