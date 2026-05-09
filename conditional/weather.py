wind = int(input()) # Don't change this line
status = "unset"
# Type your code below


# Don't change the line below
if wind < 8:
    status = "Calm"
elif wind > 8 and wind < 31 :
    status ="Breeze"
elif wind > 32 and wind < 63 :
    status ="Gale"
else:
    status = "Storm"    
     
print(f"status = {status}")