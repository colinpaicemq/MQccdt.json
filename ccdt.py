import json

with open('/home/colinpaice/eclipse-workspace-C/server/ccdt.json') as json_file:  
    ccdt = json.load(json_file)

with open('/home/colinpaice/Documents/IBM/ccdt.json') as schema_file:  
    schema = json.load(schema_file)

def doit(data1,schema1):
  #     print("IN DOIT",data1)
  #     print("IN DOIT",schema1) 
  #     print(" ")
       for x in data1:
  #         print("TYPE X",type(x))
                   
  #         print("X IN DATA1",x)
           if x not in schema1:
               print(x,":",data1[x],"from",data1)
               print("not found in schema",list(schema1))
               print(" ")
           #   return

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

     


for p in ccdt["channel"]:
 
   doit(p,schema["channel"][0])
  
 
 
