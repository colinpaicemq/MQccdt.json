# MQccdt.json 
A python program for valiating the structure of a IBM MQ ccdt.json file.



This python script checks an IBM MQ ccdt.json to make sure the keywords are in
an IBM provided sample with all of the fields. 



If you want to install it use

**pip3 -v  install   git+http://github.com/colinpaicemq/MQccdt/** and it will install mqtools.
 
 to uninstall it use
 
 pip3 -v  uninstall mqtools

Syntax:

python3 ccdt.py your.json <IBMccdt.json>

Where your.json is the file you want to validate

IBMccdt.json contains a list of all of the json fields.  It is the sample provided
by IBM.

