import sys
import os
import shutil
import subprocess
import re
def Listfun(dir):
	"""
	cmd='ls-l'+dir
	print("command to run:",cmd)
	(status,output)=subprocess.getstatusoutput(cmd)
	if status:
		sys.stderr.write(output)
		sys.exit(status)
		"""
	current_file=""	
	cmd='mkdir hello' 								#create a directory
	os.system(cmd)

	cmd1="ls -l"											#list the directory
	os.system(cmd1)


	filenames=os.listdir(dir)					#filesnames in the dir as a list
	print(filenames)
	file_str=" ".join(filenames)			#coverting filenames as string
	print(file_str)
	match=re.search(r'(\w+.txt)',file_str) 		#matching it with .txt pattern
	if match:
		current_file+=match.group(0)
	else:
		print("not found")									#print a message if not found the .txt file
	print(current_file)
	cmd1="cat "+current_file						#concatenate a txt file
	os.system(cmd1)

			
		
			

def main():
	
	args=sys.argv[1]
	# print(args)
	Listfun(args)

if __name__ == '__main__':
  main()