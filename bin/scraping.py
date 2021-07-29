import os
import sys
import time
import urllib
from colorama import Fore
def scrap():
  file = open("out.txt","r")
  lines = file.readlines()
  num_lines = sum(1 for line in open('out.txt'))
  print("")
  print(Fore.RED + "\n[#]Searching vulnerabilities for {} websites.").format(num_lines)
  file.close()
  i = 0
  for vuln in lines:
    url = vuln+"%27"
    try:
        response = urllib.urlopen(url)
    except:
        pass
    res = response.read()
    i = i + 1
    if "SQL" in res:
      print(Fore.GREEN + "\n{}.[$] SQL Injectable!\n"+ Fore.WHITE + "[Site]:" +vuln).format(i)
      f2 = open("Result.txt","a")
      f2.write(vuln+"\n")
      f2.close()
    else:
      print(Fore.RED + "\n{}.[x] SQL Not Injectable!\n"+ Fore.WHITE + "[Site]:" +vuln).format(i)
  
  os.system("rm out.txt")
  os.system("python compression.py")
if __name__ == "__main__":
   scrap()

