import sys

def main():
  dict = {}
  translate = False
  for line in sys.stdin:
    line = line.strip()

    if not line:
      translate = True
      continue
    
    if translate:
      if line in dict.keys():
        print(dict[line])
      else:
        print("eh")
    else:
      words = line.split(' ')
      dict[words[1]] = words[0]
  
    
main()

