# Element present in first set only but not in second
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
Set_A = set_1.symmetric_difference(set_2)
print("This is symmetric_difference Set_A:",Set_A)


# Alternative method
set_1 = {11,12,13,14,15}
set_2 = {14,15,16,17,18}
Set_A = set_1 ^  set_2
print("This is symmetric_difference Alternative Set_A:",Set_A)


