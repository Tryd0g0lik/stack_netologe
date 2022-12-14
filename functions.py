import re

class Stack:
  def __init__(self, var_string : str):
    self.var_string = var_string
    self.stack_front = []
    self.stack_empty = []
    self.stack_list = []

  def pair(self):
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
    else:
      if len(self.var_string) == 0:
        print(f"ramins {self.var_string}, not find the paired.", f"Empty {self.stack_empty} and number: {len(self.stack_empty)}")
      return "Code 400"

  def _isEmpty(self):
   if self.stack_list != []:
    response = False
   else:
    response = True
   return response

  def push(self, symbols : str):
    response = Stack._isEmpty(self)

    if response == True:
      symbols_list = [s for s in symbols]
      self.stack_list = symbols_list[0]
      return

    elif response == False:
      symbols_list = [s for s in symbols]
      self.stack_list.append(symbols_list[0])
      return

  def pop(self):
    response = Stack._isEmpty(self)

    if response != True:
      self.stack_list =  self.stack_list.pop()
      return self.stack_list[-2 + 1 ]

    else:
      return self.stack_list

  def peek(self):
    response = Stack._isEmpty(self)

    if response != True:
      return self.stack_list[-2 + 1]

    else:
      return self.stack_list

  def size(self):
    return len(self.stack_list)

  def stackPair(self): # From work only the list. use other symbols cannot be. Only '{([]})'
    result_pair_symbol = []
    symbols_list = [s for s in "".join(reversed(self.var_string))]
    self.stack_list = self.stack_list + (symbols_list)
    truth = Stack._isEmpty(self)

    if truth == False:
      reverse_list = (self.stack_list)


      while truth == False:
        ind = 0
        for element in reverse_list:
          for symbol in reverse_list:

            if element == "]" and symbol == "[":
              result_pair_symbol.append(element + symbol)
              reverse_list.remove(reverse_list[reverse_list.index(element)])
              reverse_list.remove(reverse_list[reverse_list.index(symbol)])
              break

            if element == "}" and symbol == "{":
              result_pair_symbol.append(element + symbol)
              reverse_list.remove(reverse_list[reverse_list.index(element)])
              reverse_list.remove(reverse_list[reverse_list.index(symbol)])
              break

            if element == ")" and symbol == "(":
              result_pair_symbol.append(element + symbol)
              reverse_list.remove(reverse_list[reverse_list.index(element)])
              reverse_list.remove(reverse_list[reverse_list.index(symbol)])
              break

            if len(reverse_list) < 2:
              print(reverse_list, f"""{result_pair_symbol}
               Symbols of stack's list no have pairs - Несбалансированно
              """)
            remains = reverse_list

        if reverse_list == []:
          # truth = True
          print(f"Stack's list the simple empty, {result_pair_symbol} - Сбалансированно")
          return reverse_list

        elif element in "[{(" and symbol == "" or\
          element == None or \
          len(reverse_list) < 2:
          print(reverse_list, f"""
               Symbols of stack's list no have pairs {result_pair_symbol} - Несбалансированно
              """)
          return reverse_list


        ind +=1
        if ind == len(reverse_list) - 1 and reverse_list[-2+1] == element and reverse_list[-2+1] == symbol:
          break

    else:
      print(f"Stack's list the simple empty, {result_pair_symbol} - Пусто")

    print(remains, "//", result_pair_symbol)

    return self.stack_list

if __name__ == "__main__":

  # s = "([]((([{}])){}))"
  s = "[[{()[]}]"
  s = "}{}"
  s = "{{[(])]}}"
  s = "[[{())}]"

  l = ['[', '{', '[', '(', '(', '(', '(',']', '}', ']', ')', ')', ')', ')']
  g = Stack(s)
  g.stackPair()
