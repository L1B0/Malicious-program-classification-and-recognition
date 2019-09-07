# coding=UTF-8
#!/usr/bin/python3

from idaapi import *
from idautils import *
from idc import *

imports_list = []

def imp_cb(ea, name, ord):
       if not name:
           #print "%08x: ord#%d" % (ea, ord)
           return True
       else:
           #print "%08x: %s (ord#%d)" % (ea, name, ord)
           imports_list.append(name)
       # True -> Continue enumeration
       # False -> Stop enumeration
       return True

nimps = idaapi.get_import_module_qty()

#print "Found %d import(s)..." % nimps

for i in xrange(0, nimps):
       name = idaapi.get_import_module_name(i)
       if not name:
           print "Failed to get import module name for #%d" % i
           #continue

       #print "Walking-> %s" % name
       idaapi.enum_import_names(i, imp_cb)

#print "All done..."
#print imports_list


#path = 'F:\\大四上\\小学期\\api\\' + GetInputFilePath().split('\\')[-2] + '\\' + '.'.join(GetInputFile().split('.')[:-1]) + '.api'

path = 'F:\\大四上\\小学期\\final_example_class\\api\\' + GetInputFilePath().split('\\')[-2] + '\\' + GetInputFile() + '.api'
#path = 'F:\\大四上\\小学期\\api\\' + '.'.join(GetInputFile().split('.')[:-1]) + '.api'

with open(path.decode('UTF-8'),'w') as f:
	f.write(str(imports_list))
	
idc.Exit(0)
	
