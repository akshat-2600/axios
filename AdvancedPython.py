# Advanced Level:
'''Q21 Create a program that calculates the sum of the digits of numbers in a list using a list comprehension.'''

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

lst = eval(input("Enter a list of numbers :"))
sums = [sum_of_digits(number) for number in lst]

print("The sum of the digits of numbers in a list :", sums)
The sum of the digits of numbers in a list : [5, 9, 21, 18, 21, 24, 11]
'''Q22 Write a program to find the prime factors of a given number using a `for` loop and list comprehension.'''

num = int(input("Enter a number :"))
a = num
num_lst = []

for i in range(1,num + 1) :
    if a%i == 0 :
        num_lst.append(i)

print(f"Prime factors of {num} :")
for i in num_lst :
    print(i)
    
    
print("                                           OR")

'''USING LIST COMPREHENSION'''

n = int(input("Enter a number :"))
b = n
prime_lst = [i for i in range(1,n + 1) if b%i == 0]

print(f"Prime factors of {n} :")
for j in prime_lst :
    print(j)
Prime factors of 24 :
1
2
3
4
6
8
12
24
                                           OR
Prime factors of 57 :
1
3
19
57
'''Q23 Develop a program that extracts unique elements from a list and stores them in a new list using a list
comprehension.'''

lst = eval(input("Enter a list :"))
unique_lst = []
new_lst = [unique_lst.append(i) for i in lst if i not in unique_lst]
print("Unique elements of list :", unique_lst)
Unique elements of list : [1, 2, 3, 4, 56, 7, 8, 45, 90, 23, 24, 556]
'''Q24 Create a program that generates a list of all palindromic numbers up to a specified limit using a list
comprehension.'''

limit = int(input("Enter the limit of palindronic numbers :"))
palindronic_lst = [i for i in range(limit+1) if str(i) == str(i)[::-1]]
print("List of palindronic numbers upto", limit,":")
print(palindronic_lst)
List of palindronic numbers upto 1000 :
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]
'''Q25 Write a program to flatten a nested list using list comprehension.'''

nested_lst = eval(input("Enter a nested list"))
simple_lst = []
lst = [simple_lst.extend(lst) if type(lst) == type([]) else simple_lst.append(lst) for lst in nested_lst ]
print("Flatten list :", simple_lst)
Flatten list : [2, 3, 4, 'hello', 'hi', 4, 56, 7, 23]
'''Q26 Develop a program that computes the sum of even and odd numbers in a list separately using list
comprehension.'''

lst = eval(input("Enter a list of numbers :"))
even_lst = []
odd_lst = []
new_lst = [even_lst.append(ele) if ele%2 == 0 else odd_lst.append(ele) for ele in lst]

print("List of even numbers :", even_lst)
print("List of odd numbers :", odd_lst)
List of even numbers : [2, 4, 6, 8, 10]
List of odd numbers : [1, 3, 5, 7, 9]
'''Q27 Create a program that generates a list of squares of odd numbers between 1 and 10 using list
comprehension.'''


square_of_lst = [i**2 for i in range(1,11) if i%2 != 0]
print("List of squares of odd numbers between 1 and 10 :", square_of_lst)
List of squares of odd numbers between 1 and 10 : [1, 9, 25, 49, 81]
'''Q28 Write a program that combines two lists into a dictionary using list comprehension.'''

print("Both lists size should be same")
keys_lst = eval(input("Enter a list of keys :"))
values_lst = eval(input("Enter a list of values :"))
new_lst = keys_lst + values_lst
dic = dict()

dict_lst = [dic.update({new_lst[i] : new_lst[len(new_lst)//2 + i]}) for i in range(len(new_lst)//2)  ]
print("Combined two lists into a dictionary :", dic)
Both lists size should be same
Combined two lists into a dictionary : {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
'''Q29 Develop a program that extracts the vowels from a string and stores them in a list using list
   comprehension.'''

string = input("Enter a string")
vowel_lst = ["a","e","i","o","u"]
string_vowel_lst = [alph for alph in string if alph.lower() in vowel_lst]
print("List of vowels from string :", string_vowel_lst)
List of vowels from string : ['a', 'e', 'i', 'A', 'A', 'A', 'E', 'A']
'''Q30 Create a program that removes all non-numeric characters from a list of strings using list 
   comprehension.'''

lst = eval(input("Enter a list of strings"))
num_lst = ["1","2","3","4","5","6","7","8","9","0"]
new_lst = [int(j) for i in lst for j in i if j in num_lst]
print(new_lst)
[1, 4, 5, 2, 3, 4, 7, 8]
