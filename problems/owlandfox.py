import sys

def remove_zeros(number: str) -> int:
  return int(number.rstrip('0'))

def add_zeros(number: int, original_length: int) -> str:
  return str(number).ljust(original_length, '0')

def main():
  number_of_lines = int(sys.stdin.readline())
  for n in range(number_of_lines):
    str_number = sys.stdin.readline().replace('\n','')
    number_without_zeros = remove_zeros(str_number)
    achived_sum = int(number_without_zeros)-1
    number = add_zeros(achived_sum, len(str_number))
    print(int(number))
    
main()

