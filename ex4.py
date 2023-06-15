"""Write a program to remove characters from a string starting from zero up to n and return a new string."""
str=input("enter the string:-  ")
trimmed=str.strip()
n=input("enter the element position upto which the string has to be trimmed:--  ")
p=int(n)
print("trimmed string is :-  ", trimmed[p:])