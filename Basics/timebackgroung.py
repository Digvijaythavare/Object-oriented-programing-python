import threading 
def show_message():
    for i in range(3,20,+3):
        print(i)
timer = threading.Timer(5,show_message)
timer.start()
print("program is started ")
for volr in range(20,3,-3):
    print(volr)