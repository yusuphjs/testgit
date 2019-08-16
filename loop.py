

import sys
string = "2.2, 1.3, 8.8, 5.5, 3.4, 12.5, 9.9, 2.7, 7.1, 1.1"

def numbers(num_string):
   num_list = num_string.split(', ')
   num_list_float = []
   for number in num_list:
       num_list_float.append(float(number))


   #num_list_float.sort()

   print(num_list)
   print(num_list_float)
   print("the smallest number is: " + str(num_list_float[0]))
   print("the largest number is: " + str(num_list_float[len(num_list)-1]))

   n=0
   total=0
   while n <=(len(num_list_float))-1:
       total = total + num_list_float[n]
       n = n  +1

   print("the total of all numbers in the string is: " +str(sum(num_list_float)))


if __name__ == "__main__":

    numbers(sys.argv[1])
