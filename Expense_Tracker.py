while True:
    print("SELECT 1 for Add Expenses.")
    print("SELECT 2 for view all Expenses.")
    print("select 3 calculate total Expenses.")
    print("select 4 to search Expense name.")
    print("select 5 for delet an Expenses.")
    print("select 6 to exit")
    option=int(input("Enter the option:"))
    if option==1:
        name=input("Enter the name:")
        cost=int(input("enter the cost:"))
        with open("expense.txt","a") as f:
            f.write(name +"-"+ str(cost) + "\n")
        print("Sucessfully added!")
    elif option==2:
        with open("expense.txt","r")as f:
            data=f.read()
            if not data:
                print("No expenses is stored")
            else:
                print("All expenses")
                print(data)
    elif option==3:
        total=0
        with open("expense.txt","r")as f:
            data=f.readlines()
            if not data:
                print("No expenses is stored!")
            else:
                print("Total expenses are:")
                for i in data:
                    expense=i.strip().split("-")
                
                    cost=int(expense[1])
                    total +=cost
                print(total)

    elif option==4:
        found=0
        with open("expense.txt","r") as f:
            data=f.readlines()
        
            if not data:
                print("No expenses is stored!")
            else:
                name=input("Enter the expense name:")
                for i in data:
                    f_name=i.strip().split("-")
                    if name.lower() ==f_name[0].lower():
                        print("Found:\n",i)
                        found +=1
                if not found:    
                    print("Not found!")
    elif option==5:
        with open("expense.txt","r")as f:
            data=f.readlines()
            if not data:
                print("No expenses is stored!")
            else:
                delet=input("Enter the expense name you want to remove:")
                found=False
                for i in data:
                    d_name=i.strip().split("-")
                    if delet.lower() == d_name[0].lower():
                        found=True
                if found:
                    with open("expense.txt","w")as f:
                        for line in data:
                            d_name=line.strip().split("-")
                            if d_name[0].lower() !=delet.lower():
                                f.write(line)
                    print("Expense daleted successfully!")
                else:
                    print("Expense not found!")    

    elif option==6:
        print("Exiting...")
        break