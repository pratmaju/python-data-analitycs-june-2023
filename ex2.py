"""Write a program to iterate the first 10 numbers and in each iteration, 
print the sum of the current and previous number."""
a=input("enter the range upto which the addition of nos has to be printed :--  ")
n=int(a)
previous_num = 0

# loop from 1 to n
for i in range(1,(n+1)):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i


