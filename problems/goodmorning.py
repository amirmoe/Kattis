import sys

phone_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9],["", 0, ""]]

class Coordinate: 
    def __init__(self, number: int): 
        if number<1:
          self.x = 1
        else:
          self.x = (number-1)%3

        if number<1:
          self.y=3
        elif number<4:
          self.y=0
        elif number<7:
          self.y=1
        else:
          self.y=2

class Code: 
    def __init__(self, value: int, code: int): 
      self.value = value
      self.abs = abs(code-value)

def get_possible_codes(code:str, coord: Coordinate, prefix: str) -> list:
  possile_codes = []

  for i in range(coord.x, 3):
    for j in range (coord.y, 4):
      value = phone_matrix[j][i]
      if value != "":
        possile_codes.append(Code(int(prefix+str(phone_matrix[j][i])), int(code)))
  return possile_codes

def get_code(code: str):
  acceptable = True
  x_cord = 0
  y_cord = 0
  final_code = ""
  for digit in code:
    coord = Coordinate(int(digit))
    
    if (coord.x>=x_cord and coord.y>=y_cord):
      x_cord=coord.x
      y_cord=coord.y
      final_code=final_code+digit
    else:
      acceptable=False
      break

  if acceptable==False:
    possile_codes = get_possible_codes(code, Coordinate(int(final_code[-1:])), final_code)
    possile_codes.extend(get_possible_codes(code, Coordinate(1), str(int(final_code)-1)))
    possile_codes.extend(get_possible_codes(code, Coordinate(1), str(int(final_code)+1)))

    possile_codes.sort(key=lambda x: x.abs)
    final_code = possile_codes[0].value

  return final_code

def main():
  number_of_lines = int(sys.stdin.readline())
  for n in range(number_of_lines):
    code = sys.stdin.readline()
    code = code.strip()
    print(get_code(code))

main()