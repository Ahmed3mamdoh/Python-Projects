""" LEVEL 2 TASKS : """                     # All Done Except Task 5 In Level 2

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task1= Transform all names to uppercase """
"Normal list"

list1=[]
for name in Names:
    list1.append(name.upper())
print (list1)

"list comprehension"

name = str
list2=[name.upper() for name in Names]
print (list2)

"functional programming"

for name in Names:
    upper_case = (lambda x:x)
    list3 = [(upper_case(name.upper()))]
    print (list3)


"__________________________________________________________________________________________________________________________"


Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task2= Get the names that contains 'a' in a list  """
"Normal list"

def list_contains_a(words):
    list1=[]
    for name in words:
        if 'a' in name:
            list1.append(name)
    return list1
print(list_contains_a(Names))

"list comprehension"

def list2_comp(words):
    return [name for name in words if 'a' in name]
print(list2_comp(Names))

"functional programming"

def list3_contains_a(words):
    if 'a' in words :
        return words
functional_prog = list(filter(list3_contains_a, Names))
print (functional_prog)

"__________________________________________________________________________________________________________________________"

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task3= Get the names that starts with 't' in a list """
"Normal list"

def list_start_with_t(words):
    list1 = []
    for name in words:
        if name.startswith('t') or name.startswith('T'):
            list1.append(name)
    return list1
print(list_start_with_t(Names))

"list comprehension"

def list2_comp(words):
    return [name for name in words if name.startswith('t') or name.startswith('T') ]
print(list2_comp(Names))

"functional programming"

def list3_start_with_t(words):
    if words.startswith('t') or words.startswith('T'):
        return words
functional_prog_starts_with_t = list(filter(list3_start_with_t , Names))
print (functional_prog_starts_with_t)

"__________________________________________________________________________________________________________________________"

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task4 = Get the names that contains 2 or more 'a' letter """
"Normal list"

def contains_2or_more_a(words):
    list1=[]
    for name in words:
        if name.count('a') >= 2:
            list1.append(name)
    return list1
print(contains_2or_more_a(Names))

"list comprehension"

def contains_2or_more_a(words):
    return [name for name in words if name.count('a') >= 2]
print(contains_2or_more_a(Names))

"functional programming"

def contains_2or_more_a(words):
    if words.count('a') >= 2:
        return words
functional_prog_contains_2or_more_a = list(filter(contains_2or_more_a, Names))
print(functional_prog_contains_2or_more_a)

"__________________________________________________________________________________________________________________________"

""" Task5 = Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]      ==     IDK (wdym???????)  """

"__________________________________________________________________________________________________________________________"

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task6 = Unpack the list"""

name1, name2, name3, name4, name5, name6, name7 = Names

print(name1)  # 'mahmoud'
print(name2)  # 'farida'
print(name3)  # 'ali'
print(name4)  # 'hassan'
print(name5)  # 'mohamed'
print(name6)  # 'khaled'
print(name7)  # 'taha'

"__________________________________________________________________________________________________________________________"

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task7:  a,b , a= the first index , b = rest of the list """

a , *b = Names
print(f"""
a contains : {a}
b contains : {b} 
""")

"__________________________________________________________________________________________________________________________"

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task8: a = the first index , b = the last index """

a , *_ , b = Names
print(f"""
a contains : {a}
b contains : {b} 
""")

"__________________________________________________________________________________________________________________________"

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

""" Task9: a = the first index , b = the second index """

a , b , *_ = Names
print(f"""
a contains : {a}
b contains : {b} 
""")
