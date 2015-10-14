#!/usr/bin/env python

import os
import sys

sendmail_prog = '/usr/sbin/sendmail' 

required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])

args = sys.argv[1:]

argdict = {}
for arg in args:
	key, val = arg.split('=')
	argdict[key] = val

#check for unfilled required fields
missing_fields = required_args.difference(list(argdict))
for item in missing_fields:
	argdict[item] = raw_input('Please specify who this email is {0}.  '.format(item))

#check for invalid fields
extra_fields = set(argdict).difference(valid_args)
for item in extra_fields:
	print item + ' is not a valid field for an email.'
	del argdict[item]

# add subject - I don't really understand what you meant in the assignment
if 'subject' not in argdict:
	argdict['subject'] = ''

sendmail_template = """From: {0}
To: {1}
Subject: {2}"""
sendmail = sendmail_template.format(argdict['from'], argdict['to'], argdict['subject'])
print sendmail
