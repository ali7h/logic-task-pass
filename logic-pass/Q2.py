min_number = int(input("Enter the min : "))
max_number = int(input("Enter the max : "))


for i in range(min_number,max_number + 1):
   if i > 1:
       for j in range(2,i):
           if (i % i) == 0:
               break
       else:
           print(i)