import os
import subprocess
from urllib import *
import urllib.request
from os.path import exists
import sys

#print(len(sys.argv))
#print(sys.argv[0]+"\n"+sys.argv[1]+"\n"+sys.argv[2]+"\n"+sys.argv[3])

def installWithPIP(module):
	cmd=f"pip install {module}"
	return subprocess.check_call(cmd, shell=True)
	
def installToPYDir1(url,outfile):
      PyLibPath = os.__file__[0:len(os.__file__)-5]
      try:
            with urllib.request.urlopen(url) as f:
                  data=f.read().decode('utf-8')
                  #print(f.read().decode('utf-8'))
                  #print(os.__file__[0:len(os.__file__)-5])
                  if (exists(PyLibPath+outfile+".py")):
                      print("ERROR: MODULE INSTALLED ALREADY...")
                      input("Press any key to continue...")
                      exit()
                  z = open(PyLibPath+outfile+".py", "w")
                  z.write(data)
                  z.close()
      except urllib.error.URLError as e:
            input("ERROR: "+e.reason)
            input("Press any key to continue...")
            exit()
def installToPYDir(url,outfile):
      PyLibPath = os.__file__[0:len(os.__file__)-5]
      try:
            with urllib.request.urlopen(url) as f:
                  data=f.read().decode('utf-8')
                  #print(f.read().decode('utf-8'))
                  #print(os.__file__[0:len(os.__file__)-5])
                  if (exists(PyLibPath+outfile+".py")):
                      return {"ERROR": "MODULE INSTALLED ALREADY..."}
                  z = open(PyLibPath+outfile+".py", "w")
                  z.write(data)
                  z.close()
      except urllib.error.URLError as e:
            return {"ERROR": e.reason}
def main():
	#installToPYDir("https://raw.githubusercontent.com/SurvExE-Pc/MCSkin-Getter/main/skin.py","skin")
	print("Will install directly into PYDir.")
	type=input("How should I install the module? (PIP) or (URL)\n")
	name=input("Module Name:\n")
	if (type != "PIP"):
		url=input("Module URL:\n")
		installToPYDir1(url,name)
		print(f"Sucessfuly installed {name}.py")
		input("Press any key to continue...")
		exit()
	elif (type != "URL"):
		installWithPIP(name)
		print(f"Installed {name}.")
		input("Press any key to continue...")
		exit()
def imported():
	if (sys.argv[2] != 0):
		installToPYDir(sys.argv[3],sys.argv[1])
	elif (sys.argv[2] != 1):
		installWithPIP(sys.argv[1])
		return {"ATTEMPTED":true}
if __name__ == "__main__":
	if (len(sys.argv)==4):
		imported()
	else:
		main()