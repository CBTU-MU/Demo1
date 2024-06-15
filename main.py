import libDemo as ld

def hello(name):
  answer = 'Hello ' + name
  print(answer)
  return answer

def main():
  name = input('What is your name? ')
  hello(name)
  ld.helloDemo(name)

if __name__ == '__main__':
  main()
