import sys

# Time Limit Exceeded	
# hexadecimal_convert = {
#   0:"0",
#   1:"1",
#   2:"2",
#   3:"3",
#   4:"4",
#   5:"5",
#   6:"6",
#   7:"7",
#   8:"8",
#   9:"9",
#   10:"A",
#   11:"B",
#   12:"C",
#   13:"D",
#   14:"E",
#   15:"F",
# }

def convert_to_base10(base8: str):
  # Time Limit Exceeded	
  # base8_reversed = base8[::-1]
  # base10 = 0
  # for i in range(len(base8)-1,-1,-1):
  #   base10+= (int(base8_reversed[i]) * (8**i))

  base10 = int(base8, 8)
  return base10

def convert_to_base16(base10: int):
  # Time Limit Exceeded
  # remainders = []
  # if (base10==0):
  #   remainders.append(0)

  # result = base10
  # while result != 0:
  #   remainders.append(result%16)
  #   result = result//16

  # base16 = ""
  # for i in reversed(remainders):
  #   base16+= hexadecimal_convert[i]
  
  base16 = format(base10, 'X')
  return base16


def main():
  base8 = sys.stdin.readline()
  base10 = convert_to_base10(base8)
  base16 = convert_to_base16(base10)
  print(base16)

main()
