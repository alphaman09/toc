
#while True:
import re

def form_dict(arr):

  my_dict = {}
  print(my_dict)
  for prod in arr:             #['S:ab', 'S:bc', 'S:AB', 'A:a', 'B:b']      "S:ab,S:bc,S:AB,A:a,B:b"
    KeyVal = prod.split(":")
    if KeyVal[0] in my_dict.keys():
      if type(my_dict[KeyVal[0]]) != list:
        #Transformting the value of the dictory to list
        my_dict[KeyVal[0]] = [my_dict[KeyVal[0]]]
        my_dict[KeyVal[0]].append(KeyVal[1])

      else:
        #Adding new value to the created list
        my_dict[KeyVal[0]].append(KeyVal[1])
    
    else:
      #Adding a new Key-Value pair
      my_dict[KeyVal[0]] = KeyVal[1]

  return my_dict


def find_terminal(productions):

  def check_lower(st):
    if st.islower():
      return st
    else:
      for char in st:
        if char.isupper():
          st = re.sub(char,productions[char],st)
          print(st)
          return check_lower(st)
      
  terminals = []

  for var in productions["S"]:
    if var.islower():
      terminals.append(var)
    else:
      term = check_lower(var)
      if term not in terminals:
        terminals.append(term)

  return terminals
  
def getTerminal(que):
  term = []
  for i in que:
    if i.islower():
      if i not in term:
        term.append(i)
  return term



G = { 'nonTerminal':[],'terminals':[],"start":[],"productions":[]}

#query = input("Enter Productions:")
query = "S:ab,S:bc,S:AB,A:a,B:b"

Prods_arr = query.split(",")
print(Prods_arr)
Prods = form_dict(Prods_arr)
print(Prods)

G['terminals'] = getTerminal(query)
G['nonTerminal'] = list(Prods.keys())[1:]
G['start'] = list(Prods.keys())[0]
G['productions'] = Prods


print(G)

print("End String:",find_terminal(Prods))

#Grammer
#S:a/b/ab
#S:ab,S:bc,S:AB,A:a,B:b

'''
Enter Productions:S:ab,S:bc,S:AB,A:a,B:b
{'S': ['ab', 'bc', 'AB'], 'A': 'a', 'B': 'b'}
{'nonTerminal': ['A', 'B'], 'terminals': ['a', 'b', 'c'], 'start': 'S', 'productions': {'S': ['ab', 'bc', 'AB'], 'A': 'a', 'B': 'b'}}
aB
ab
End String: ['ab', 'bc']
'''
