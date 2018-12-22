# -*- coding: utf-8 -*- 
# modification history
# 2018/12/21 long file name cut to 256
# 2018/12/21 do not rename while file exist
import  sys
import xlrd
import os.path
import re

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows 
    ncols = table.ncols 
    colnames =  table.row_values(colnameindex) 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows 
    colnames =  table.row_values(colnameindex) 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list
    
def replace_invalid_filename_char(filename, replaced_char='-'):
    '''Replace the invalid characaters in the filename with specified characater.
    The default replaced characater is '_'.
    e.g. 
    C/C++ -> C_C++
    '''
    valid_filename = filename
    invalid_characaters = '\\/:*?"<>|'
    for c in invalid_characaters:
        #print 'c:', c
        valid_filename = valid_filename.replace(c, replaced_char)

    return valid_filename 


def main():
    
    if len(sys.argv) < 3:
        print 'cmd python qc-ducomment-rename.py document-folder SolutionTitles.xls'  
        sys.exit()
    tables = excel_table_byname(sys.argv[2],0,"SolutionTitles")     
    for parent,dirnames,filenames in os.walk(sys.argv[1]):
        for filename in filenames:                      
            name, ext = os.path.splitext(filename)
            aliasname = filename.replace('_','-').upper()
            #aliasname = aliasname.upper()
            aliasname = replace_invalid_filename_char(aliasname)
            print("the full name of the file is: " + aliasname)
            for row in tables:              
              if aliasname.find(row['DCN']+'-') == 0:
              	if re.match(row['DCN']+'-'+"[A-Z]"+'-',aliasname):
              		finalname = re.match(row['DCN']+'-'+"[A-Z]"+'-',aliasname).group()+re.sub("[^A-Za-z0-9]", "-", row['Title'].encode('utf-8'))
              	else:
                	finalname = row['DCN']+"-"+re.sub("[^A-Za-z0-9]", "-", row['Title'].encode('utf-8'))
                finalname = finalname.replace('--','-')
                finalname = finalname.replace('--','-')
                finalname = finalname.replace('--','-')
                full_basename = os.path.join(parent,finalname)
                
                if len(full_basename) > 252:
                	print ("full basename  ", full_basename)
                	full_basename=full_basename[0:251]
                full_finalname = full_basename+ext
                if os.path.exists(full_finalname):
                	break
                if os.path.join(parent,filename) != full_finalname:
                  os.rename(os.path.join(parent,filename), full_finalname)
                  break
     

if __name__=="__main__":
    main()