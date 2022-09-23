num = (1,2,3,4,5,6,7,8,9,10,11) 
num_odd = 0
num_even = 0
for x in num:
    if not x%2:
        num_even+=1
    else:
        num_odd+=1   
print("numbers of even no. :",num_even)
print("numbers of odd no. : ", num_odd)         
