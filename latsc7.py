z = [1, 3, 2, 4, 'Alice', 'Bob']
z.sort(key=str)
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.")

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = ' Hello World '
a=spam.strip()
b=spam.lstrip()
c=spam.rstrip()
print (spam)
print(a)
print(b)
print(c)

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))