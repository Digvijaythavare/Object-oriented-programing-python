# Element present in first set only but not in second
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
Set_A = set_1.difference(set_2)
Set_B = set_2.difference(set_1)
print("This is Difference Set_A:",Set_A)
print("This is Difference Set_B:",Set_B)

# Alternative method
set_1 = {11,12,13,14,15}
set_2 = {14,15,16,17,18}
Set_A = set_1 - set_2
Set_B = set_2 - set_1
print("This is Difference Alternative Set_A:",Set_A)
print("This is Difference Alternative Set_B",Set_B)

