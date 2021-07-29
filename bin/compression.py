import os
import sys
import time
from colorama import Fore
def redup():
  if True:
    os.system("sort  Result.txt | uniq > Result.root")
    x = sum(1 for line in open('Result.root'))
    y = 1
    z= x-y 
    print("[x] Total {} SQL injectable sites found!").format(z)
    if os.path.exists("Result.txt"):
      os.system("rm Result.txt")
    file = open("Result.root","r")
    y = file.readlines()
    file.close()

    for x in y:
      print(Fore.GREEN + x +"\n")
    os.system('rm Result.root')
if __name__ == "__main__":
  redup()
