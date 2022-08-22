import re

class Stack:
  def __init__(self, var_string : str):
    self.var_string = var_string
    self.stack_front = []
    self.stack_empty = []


  def isEmpty(self):
    verify = True
    symbol : str
    time_symbol : str
    bisic_leng_text = len(self.var_string)
    if len(self.var_string) != 0:
      i = 0

      while verify:
        for symbol in self.var_string:
          for time_symbol in "}])":

            if symbol == "{" and time_symbol == "}" and symbol in self.var_string and time_symbol in self.var_string:
              try:
                template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\{{1}[\s0-9a-zA-Zа-яёА-ЯЁ]{0,}\}{1})[^.*\}\]\)\{\(\[]{0,}")
                old_str = (re.search(template, self.var_string).group(0)) #[1:-1]
              except AttributeError:
                continue

              truth = [truth for truth in old_str if truth in "}]){(["][1 : -1]
              if truth != []:
                print("One symbol '}]){([' found")
                return "Code 400"

              if len(old_str) == 2:
                self.stack_empty.append(old_str)

              result = self.var_string.replace(str(old_str), "")
              self.var_string = result
              print(self.var_string)
              time_symbol = ""
              break

            if symbol == "(" and time_symbol == ")" and symbol in self.var_string and time_symbol in self.var_string:
              try:
                template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\({1}[\s0-9a-zA-Zа-яёА-ЯЁ]{0,}\){1})[^.*\}\]\)\{\(\[]{0,}")
                old_str = re.search(template, self.var_string).group(0) #[1:-1])
              except AttributeError:
                continue

              truth = [truth for truth in old_str if truth in "}]){(["][1:-1]
              if truth != []:
                print("One symbol '}]){([' found")
                return "Code 400"

              if len(old_str) == 2:
                self.stack_empty.append(old_str)

              result = self.var_string.replace(str(old_str), "")
              self.var_string = result
              print(self.var_string)
              time_symbol = ""
              break

            if symbol == "[" and time_symbol == "]" and symbol in self.var_string and time_symbol in self.var_string:
              try:
                template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\[{1}[\s0-9a-zA-Zа-яёА-ЯЁ]{0,}\]{1})[^.*\}\]\)\{\(\[]{0,}")
                old_str = re.search(template, self.var_string).group(0) #[1:-1])
              except AttributeError:
                continue

              truth = [truth for truth in old_str if truth in "}]){(["][1:-1]
              if truth != []:
                print("One symbol '}]){([' found")
                return "Code 400"

              if len(old_str) == 2:
                self.stack_empty.append(old_str)

              result = self.var_string.replace(str(old_str), "")
              self.var_string = result
              print(self.var_string)
              time_symbol = ""
              break
          continue

        if len(self.var_string) == 0:
          print("All symbol '}]){([' paired.", f"Empty {self.stack_empty} and number: {len(self.stack_empty)}")
          return "Code 200"
        i +=1
        if i >= bisic_leng_text - 1:
          print(f"ramins {self.var_string}, not find the paired.", f"Empty {self.stack_empty} and number: {len(self.stack_empty)}")
          verify = False
        # elif len(self.var_string) != 0:
        #   print(f"ramins {self.var_string}, not find the paired ")
        #   exit()
    else:
      if len(self.var_string) == 0:
        print(f"ramins {self.var_string}, not find the paired.", f"Empty {self.stack_empty} and number: {len(self.stack_empty)}")
      return "Code 400"



  def push(self):
    self.stack.append(...)

  def pop(self):
    self.stack.pop()

  def peek(self):
    ...

  def size(self):
    ...

# s = "([]((([{}])){dds}))"
# s = "[[{(pppp)[]}]"
s = "}{}"
g = Stack(s)
g.isEmpty()
