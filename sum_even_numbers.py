#Program:Sum of even numbers in a list.
#Author:Radhika
#Description:This program gives sum of total even numbers from given list.
l=[1,2,3,4,5,6]
total=0
for i in l:
  if(i%2==0):
    total+=i
print("Sum of even numbers:",total)
