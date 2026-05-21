def To_do_list():
    tasks = []
    while True:
         print("1. Add task")
         print("2. Remove task")
         print("3. Show task")
         print("4. quite")
         choise = input("Enter your choise : ")

         if choise == "1":
              task = input(" Enter task : ")
              tasks.append(task)
  
         elif choise == "2":
              task = input("Enter task : ")

              if task in tasks:
                   tasks.remove(task)
              else:
                print("Task not found ! sorry")


         elif choise == "3":
             print("Tasks : ")
             for task in tasks:
                 print("- ",task)
         elif choise == "4":               
             break
         else:
              print("Sorry!")     
To_do_list()                          