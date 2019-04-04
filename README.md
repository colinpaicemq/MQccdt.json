# MQTools
A repository of useful bits of code for processing IBM MQ.

## C samples 
  1. One for putting an getting messages - with bugs to educate people on debugging MQ!
  1. One acting as a MQ server in C  

## Python code

These build on the low level MQ services provided by [pymqi](https://dsuch.github.io/pymqi/). 

This python script checks an IBM MQ ccdt.json to make sure the keywords are in
an IBM provided sample with all of the fields. 


I would welcome suggestions, comments, and reports of bugs.  Please contact me at ColinPaiceMQ@GMAIL.COM
or raise an issue on [MQTools GitHub](https://github.com/colinpaicemq/MQTools).

If you want to install it use

**pip3 -v  install   git+http://github.com/colinpaicemq/MQccdt/** and it will install mqtools.
 
 to uninstall it use
 
 pip3 -v  uninstall mqtools

Syntax:

python3 ccdt.py your.json <IBMccdt.json>

Where your.json is the file you want to validate
IBMccdt.json contains a list of all of the json fields.

