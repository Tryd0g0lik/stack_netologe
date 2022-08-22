import re

class Stack:
  def __init__(self, var_string : str):
    self.var_string = var_string
    self.stack_front = []
    self.stack_back = []
    self.verify = True

  def isEmpty(self):
    symbol : str
    time_symbol : str

    if len(self.var_string) != 0:
      front_path_string = ''.join(reversed(self.var_string[0 : len(self.var_string)//2]))
      back_path_string = (self.var_string[len(self.var_string)//2 : ])

      for symbol in front_path_string:
        if symbol in "{([":
          self.stack_front.append(symbol)

        for time_symbol in "}])":

          if symbol == "{" and time_symbol == "}" and symbol in self.var_string and time_symbol in self.var_string:
            template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\{{1}[\s0-9a-zA-Zа-яёА-ЯЁ]{0,}\}{1})[^.*\}\]\)\{\(\[]{0,}")

            old_str = (re.search(template, self.var_string).group(0)) #[1:-1]
            truth = [truth for truth in old_str if truth in "}]){(["][1 : -1]
            if truth != []:
              print("One symbol '}]){([' found")
              exit()

            result = self.var_string.replace(str(old_str), "")
            self.var_string = result
            print(self.var_string)
            time_symbol = ""

          if symbol == "(" and time_symbol == ")" and symbol in self.var_string and time_symbol in self.var_string:
            template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\({1}[\s0-9a-zA-Zа-яёА-ЯЁ]{0,}\){1})[^.*\}\]\)\{\(\[]{0,}")

            old_str = re.search(template, self.var_string).group(0) #[1:-1])
            truth = [truth for truth in old_str if truth in "}]){(["][1:-1]
            if truth != []:
              print("One symbol '}]){([' found")
              exit()


            result = self.var_string.replace(str(old_str), "")
            self.var_string = result
            print(self.var_string)
            time_symbol = ""

          if symbol == "[" and time_symbol == "]" and symbol in self.var_string and time_symbol in self.var_string:
            template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\[{1}[\s0-9a-zA-Zа-яёА-ЯЁ]{0,}\]{1})[^.*\}\]\)\{\(\[]{0,}")

            old_str = re.search(template, self.var_string).group(0) #[1:-1])
            truth = [truth for truth in old_str if truth in "}]){(["][1:-1]
            if truth != []:
              print("One symbol '}]){([' found")
              exit()


            result = self.var_string.replace(str(old_str), "")
            self.var_string = result
            print(self.var_string)
            time_symbol = ""

      if len(self.var_string) == 0:
        print("All symbol '}]){([' paired")
        exit()

      elif len(self.var_string) != 0:
        print(f"ramins {self.var_string}, not find the paired ")
      exit()
    else:
      if len(self.var_string) == 0:
        print(f"ramins {self.var_string}, not find the paired")
      exit()



  def push(self):
    self.stack.append(...)

  def pop(self):
    self.stack.pop()

  def peek(self):
    ...

  def size(self):
    ...

s = "(((([{55 }]))))"
# s = "((((55 ))"
g = Stack(s)
g.isEmpty()
