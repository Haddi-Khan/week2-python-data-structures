# 2.	Maximum Element in List – Find the largest number in a list.
list1=[1,2,3,4,5]
num_max = list1[0]
for num in list1:    
    if num > num_max:   
        num_max = num  
print("maxium elememt in list", num_max)
# using bulid in function
# num_max = max(list1)
# print("Maximum element in list:", num_max)