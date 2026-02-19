#Program:Count even numbers in a list
#Author:Radhika
#Description:This program counts total even numbers from given list.
l=[1,2,3,4,5]
count=0
for i in l:
  if(i%2==0):
    count+=1
print("Total even numbers are:",count)
