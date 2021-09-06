#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  url_list=[]
  try:
    f=open(filename,'r')
    match=re.search(r'_([\w.]+)',filename)
    if match:
      file=match.group(1)
    text=f.read()
    words=re.findall(r'(GET\s)([/\w-]+.jpg)',text)
    for word in words:
      url="http://"+file+word[1]
      url_list.append(url)
  except IOError:
    sys.stderr.write("Problem reading "+filename)
  return sorted(url_list)
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if os.path.exists(dest_dir):
    file="index.html"
    file_path=os.path.join(dest_dir,file)
    f=open(file_path,'w')
    f.write("<html><head>")
    f.write("<title>index.html</title></head>")
    f.write("<body>")
    i=0
    for paths in img_urls:
      new="img"+str(i)
      
      path=os.path.join(dest_dir,new)
      urllib.request.urlretrieve(paths,path)
      f.write("<img src="+new+">")
      i=i+1
    f.write("</body></html>")
  else:
      os.mkdir(dest_dir)
    

  

def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  print(img_urls)
  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
