
age = [10,20,30,40]

print(age) # print whole list 
# print(age+2) # this is not valid that's why we use for loop

#forloop will be used to visit every element in list

for i in age:
    print(i)
# this will print the whole list line by line seperatly.

for i in age:
    print(i+2)
# this will add the number 2 to each value in the list.

for i in age:
    print(i**2)
    # This will square each number and then print them speratly in differnt lines.


# Eg:- we have n=3 ,list =[0,1,2,3,4,5,6,7,8,9] then square the numbers and print them line to line.

numbers=[0,1,2,3,4,5,6,7,8,9]
for n in numbers[0:3]:
    print(n)
    print(n**2)

#slicing 
num=[1,2,3,4,5]
print(num[0:3]) 

