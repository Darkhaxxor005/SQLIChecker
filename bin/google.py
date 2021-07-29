from googlesearch import search
from colorama import Fore
print("")
query = input(Fore.GREEN + "[x] Enter Dork: " + Fore.WHITE + "inurl:")
query1 = "inurl:http:// "+query
print("")
numbers = input(Fore.GREEN + "[x] How much website do you want? : " + Fore.WHITE + "")
hist = open(".History.txt","w")
hist.write(query)
hist.close()
numbers = int(numbers)
def write_line():
  for site in search(query, num=numbers, stop=numbers):
      f = open("out.txt","a")
      f.write(site+"\n")
      f.close()
if __name__ == "__main__":
  write_line()
