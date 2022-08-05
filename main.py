import sys, fitz

def main():
  fname = sys.argv[1]
  doc = fitz.open(fname)
  for page in doc:
    for field in page.widgets():
      print('Input info:')
      print(field.field_name)
      print(field.field_value)
      print('----')

if __name__ == '__main__':
  main()