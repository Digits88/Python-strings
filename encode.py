#!/usr/bin/python

#email: ombagi@promaxted.com

import base64
import binascii

print """
########################################################################
# Simple decode & encode of a raw string to  hex and Base64 digits,    #
# using the binascii and base64 module respectively. Check source code.#
########################################################################
"""

text = raw_input("Enter a word: ")
print "\n"

en_text = base64.b16encode(text)
print "Encode as Base64"
print en_text +  "\n"

enx_text = binascii.b2a_hex(text)
print "Encode as hex"
print enx_text + "\n"

print "Decode back to bytes"
enx_decode = binascii.a2b_hex(enx_text)
print enx_decode + "\n"

print """
######################################################################
# NOTE: base64.b16decode() and base64.b16encode() only operate 	     #
#	with uppercase hex letters, while the functions in binascii  #
#	work with either case.         				     #	 
######################################################################
"""

print "Encode as Base16"
uni_string  = base64.b16encode(enx_text)
print uni_string + "\n"

print "Decoding the  B16 to ascii"
print(uni_string.decode('ascii')) + "\n"

print """
############################################################################
# Note: Output produced by the encoding functions is always a byte string. #
#      To get Unicode for output, we  need to tweak the code a little bit  #
############################################################################
"""


