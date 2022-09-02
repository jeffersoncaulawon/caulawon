def cube(x):
    return x * x * x
print("CUBE")
number = float(input(" Enter value for cube : "))
cub = cube(number)
print("cube = {1}".format(number, cub))
print("")
print("Factorial")

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
x=int(input("Enter value for factorial : "))
print("factorial =",factorial(x)) 
print("")



print(" Pattern Count")
print("")
def pattern_count(pattern):
    count = start = 0
given_list = [ 'a','b','c','b','a','b','f']
pattern = ['a','b']
text = ''.join(str(x) for x in given_list)
print("List =", text)
pattern = ''.join(str(x) for x in pattern)
print("Pattern =" ,pattern)
print("No. of occurances:",text.count(pattern))
print ("")
given_list = [ 'g','a','b','a','b','a','b','a']
pattern = ['a','b','a']
text = ''.join(str(x) for x in given_list)
print("List =", text)
pattern = ''.join(str(x) for x in pattern)
print("Pattern =" ,pattern)
print("No. of occurances:",text.count(pattern))
