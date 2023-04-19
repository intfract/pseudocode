import os
import math

class Constant():
  def __init__(self, data_type, data):
    self.mutable = False
    self.data = data
    self.data_type = data_type


keywords = [
  'declare',
  'constant',
  'for',
  'while',
  'case',
]

special = '!@#$%^&*()[]{}\\+-=</>*'
print(special)

def isValid(name: str) -> bool:
  for char in name:
    if char in special:
      return False
  return True

def read(filePath):
  with open(filePath, 'r') as file:
    return file.readlines()

def process(pseudocode: list):
  print('processing psuedocode...')
  memory = {}
  for line in pseudocode:
    print(line)
    tokens = []
    token = ''
    for char in line:
      if char == ' ' and token != '':
        tokens.append(token)
        token = ''
      else:
        token += char
    tokens.append(token.replace('\n', ''))
    print(tokens)
    for i in range(len(tokens)):
      if tokens[i] == ' ':
        pass # indent
      elif tokens[i] in keywords:
        match tokens[i]:
          case 'constant':
            name = tokens[i + 1]
            if isValid(name):
              if tokens[i + 2] == ':':
                data_type = tokens[i + 3]
                data = eval(tokens[i + 5])
                if tokens[i + 4] != '<-':
                  raise SyntaxError(f'\nLine: {i + 1}\nProblem: {tokens[i]} {name} {tokens[i + 2]} {tokens[i + 3]} {tokens[i + 4]}\nMessage: expected "<-" but given "{tokens[i + 4]}"')
                match data_type:
                  case 'integer':
                    if type(data) == type(0):
                      memory[name] = Constant(data_type, data)
              else:
                raise SyntaxError(f'\nLine: {i + 1}\nProblem: {tokens[i]} {name} {tokens[i + 2]}\nMessage: expected ":" but given "{tokens[i + 2]}"')
            else:
              raise SyntaxError(f'\nLine: {i + 1}\nProblem: {tokens[i]} {name}\nMessage: "{name}" is not a valid constant name!')


print(process(read('pseudocode.txt')))