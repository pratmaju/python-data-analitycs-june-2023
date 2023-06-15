"""Write a program to accept a string from the user and display characters 
that are present at an even index number."""
str=input("enter the string :-  ")
n=len(str)
for i in range(0, n, 2):   #need to learn this
    print("index[", i, "]", str[i])  #need to learn this
