# Python program to check consistency an IBM MQ ccdt in json format 
#
# MIT License
#
# Copyright (c) 2019 Stromness Software Solutions.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#
#* Contributors:
#*   Colin Paice - Initial Contribution

"""
program to check consistency an IBM MQ ccdt in json format 
"""

import json
import argparse


def doit(data1,schema1):
 
       for x in data1:
           if x not in schema1:
               print(x,":",data1[x],"from",data1)
               print("not found in schema",list(schema1))
               print(" ")
  
           elif isinstance(data1[x],list):
                for z in data1[x]:
                  for zz in z:

                     if zz not in schema1[x][0]:
                        print("ZZ ",zz, "not in ",schema1[x][0])
                        print(" ")
                     else:

                         pass
           elif isinstance(data1[x],dict):
                doit(data1[x],schema1[x])
                pass
           elif type(data1[x]) == type(schema1[x] ):
                pass
           else :    
                print("types do not match",x,"in",data1,schema1)
                print(" ")  
parser = argparse.ArgumentParser(description="validate ccdt.json file")
parser.add_argument('-ccdt',dest="ccdt"
                        ,help="file with the ccdt.json"
                        ,required=True
                   )  
parser.add_argument('-schema',dest="schema"
                        ,help="ccdt.json file fully configured"
                        ,default="./IBMccdt.json"
                        
                   )  
args = parser.parse_args()

with open(args.ccdt) as json_file:  
    ccdt = json.load(json_file)

with open(args.schema) as schema_file:  
    schema = json.load(schema_file)

for p in ccdt["channel"]:
    doit(p,schema["channel"][0])
  
 
 
