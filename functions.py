import re

class Stack:
  def __init__(self, var_string : str):
    self.var_string = var_string
    self.stack = []
    self.verify = True

  def isEmpty(self):
    symbol : str
    time_symbol : str


    if len(self.var_string) != 0:
      var_string = reversed(self.var_string)
      for symbol in var_string:
        if symbol in "{([":
          self.stack.append(symbol)

        for time_symbol in "}])":

          if symbol == "{" and time_symbol == "}":
            # template = re.compile("[^.*]\{[^\[\{\(]*.*[^\}\]\)]*\}[^.*]")
            template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\{{1}.{0,}\}{1})[^.*\}\]\)\{\(\[]{0,}")

            old_str = (re.search(template, self.var_string).group(0))[1:-1]
            truth = [truth for truth in old_str if truth in "}]){(["]
            if truth != []:
              print("One symbol '}]){([' found")
              exit()

            result = self.var_string.replace(str(old_str), "")
            self.var_string = result
            # template = old_str = result = None
            print(self.var_string)
          if symbol == "(" and time_symbol == ")":
            # template = re.compile("[^.*]\([^\[\{\(]*.*[^\}\]\)]*\)[^.*]")
            template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\({1}.{0,}\){1})[^.*\}\]\)\{\(\[]{0,}")

            old_str = (re.search(template, self.var_string).group(0)[1:-1])
            truth = [truth for truth in old_str if truth in "}]){(["]
            if truth != []:
              print("One symbol '}]){([' found")
              exit()


            result = self.var_string.replace(str(old_str), "")
            self.var_string = result
            # template = old_str = result = None
            print(self.var_string)
          if symbol == "[" and time_symbol == "]":
            # template = re.compile("[^.*]\[[^\[\{\(]*.*[^\}\]\)]*\][^.*]")
            # template = re.compile("[^.*]{0,}(\[[^\[\{\(]*.*[^\}\]\)]*\])[^.*]{1,}")
            # [ ^.*]{1, }(\{{1}[ ^\[\{\(]{0, }.*[^ \}\]\)]{1, }\}{1})[ ^.*]{1, }
            template = re.compile("[^.*\}\]\)\{\(\[]{0,}(\[{1}.{0,}\]{1})[^.*\}\]\)\{\(\[]{0,}")

            truth = [truth for truth in old_str if truth in "}]){(["]
            if truth != []:
              print("One symbol '}]){([' found")
              exit()

            old_str = (re.search(template, self.var_string).group(0)[1:-1])
            result = self.var_string.replace(str(old_str), "")
            self.var_string = result
            # template = old_str = result = None
            print(self.var_string)
          if len(self.stack) == 0:
            break
    else:
      exit()

  def push(self):
    self.stack.append(...)

  def pop(self):
    self.stack.pop()

  def peek(self):
    ...

  def size(self):
    ...

s = "(((([{55 }]))"
g = Stack(s)
g.isEmpty()
