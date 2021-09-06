#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil


"""Copy Special exercise
"""
def get_special_paths(dir):
  abslist=[]
  try:
    filenames=os.listdir(dir)
    for filename in filenames:
      match=re.search(r'\w+w+\w+',filename)
      if match:
        path=os.path.join(dir,filename)
        abs=os.path.abspath(path)
        abslist.append(abs)
  except IOError:
    sys.stderr("Problem to files in the directory ",dir)
  return abslist
# +++your code here+++
# Write functions and modify main() to call them
  
  #copy function
def copy_to(todir,list2):
  print(todir,list2)
  if os.path.exists(todir):
    for paths in list2:
      shutil.copy(paths,todir)
  else:
      os.mkdir(todir)
    

    #zip functions
def zip_to(tozip,list2):
  print("Command I am going to do:,")
  for path in list2:
    cmd='zip -j '+tozip+" "+path
    print(cmd)
    os.system(cmd)
  

def print_fun(list2):
  for path in list2:
    print(path)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  list2=[]
  result=[]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    print(args)

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
    list2=get_special_paths(dir)
    for path in list2:
      result.append(path)
  
  if todir:
    copy_to(todir,result)
  elif tozip:
    zip_to(tozip,result)
  else:
    print_fun(result)
  
if __name__ == "__main__":
  main()
