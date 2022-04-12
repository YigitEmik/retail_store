
# Discounts(2 for each year, max 10) for every employee
# If employee is a manager, +10 to discount
# If employee is a hourly employee, +2
# Max discount == $20
# employee discount number

employee_list = []
item_list = []
employee_types = ["hourly", "manager"]

def unique_employee_disc(s):
    for a in employee_list:
        while s == a[6]:
            return True

def unique_item_num(itemnum):
    for b in item_list:
        while itemnum == b[0]:
            return True

def create_employee():
    employee_list_temp = []
    cont = True
    while cont:
        total_purchased = 0
        total_discounts = 0
        employee_id = input("Employee ID: ")
        # Check if employee id is numeric
        while employee_id.isnumeric() == False:
            employee_id = input("Value must be integer please enter again: ")
        # We are checking if the employee id is unique by looping through the list
        for i in employee_list:
            for a in i:
                while a == employee_id:
                    employee_id = input("Value must be unique for employee please enter again: ")
        employee_name = input("Employee Name: ")
        employee_type = input("Employee Type: ")
        while employee_type not in employee_types:
            employee_type = input("Employee type Must be manager or hourly please enter again: ")
        years_worked = input("Years Worked: ")
        # Check if years worked is numeric
        while years_worked.isnumeric() == False:
            years_worked = input("Value must be integer please enter again: ")
        employee_discount_num = input("Employee Discount Number: ")
        # We are checking if the discount number is unique by looping through the list
        while employee_discount_num.isnumeric() == False:
            employee_discount_num = input("Value must be integer please enter again: ")
        for c in employee_list:
            for b in c:
                while b == employee_discount_num:
                    employee_discount_num = input("Value must be unique for employee please enter again: ")
        employee_list_temp.append(employee_id)
        employee_list_temp.append(employee_name)
        employee_list_temp.append(employee_type)
        employee_list_temp.append(years_worked)
        employee_list_temp.append(total_purchased)
        employee_list_temp.append(total_discounts)
        employee_list_temp.append(employee_discount_num)
        employee_list.append(employee_list_temp)
        print(employee_list)
        answ = input("Would you like to continue? (Y/N) ")
        if answ == "y":
            create_employee()
        else:
            ask = input("Would you like to go to the Menu? (Y/N) ")
            if ask == "y":
                menu()
            else:
               exit()

def create_item():
    item_list_temp = []
    while True:
        try:
            item_number = int(input("Item number: "))
        except ValueError:
            print("Item number must be an integer please enter again: ")
            create_item()
        # We are checking if the item number is unique by looping through the list
        for i in item_list:
            for a in i:
                while a == item_number:
                    item_number = int(input("Item number must be unique please enter again: "))
        item_name = input("Item name: ")
        try:
            item_cost = int(input("Item Cost: "))
        except ValueError:
            print("Item Cost must be a number please enter again: ")
            create_item()

        # Check if item cost is numeric
        item_list_temp.append(item_number)
        item_list_temp.append(item_name)
        item_list_temp.append(item_cost)
        item_list.append(item_list_temp)
        answer = input("Would you like to add another item? (Y/N) ")
        if answer.lower() == "y":
            create_item()
        else:
            answer2 = input("Would you like to go to the menu? (Y/N) ")
            if answer2.lower() == "y":
                menu()
            else:
                exit()

def make_purchase():
    print("Item Number | Item Name | Item Cost")
    for i in item_list:
        print(i)
    employee_discount_num1 = input("Enter an employee discount number: ")
    # Check if employee discount number exist
    while unique_employee_disc(employee_discount_num1) == False:
            print("We couldn't find an employee with this discount number.")
            employee_discount_num1 = input("Please enter again: ")
    purchase = int(input("Enter an Item number: "))
    while unique_item_num(purchase) == False:
            purchase = int(input("Please enter an exist item number: "))

    answerr = input("Confirm Purchase? (Y/N) ")
    for p in item_list:
        if p[0] == purchase:
            add = p
    for e in employee_list:
        if e[6] == employee_discount_num1:
            added = e
    if answerr.lower() == "y":
        added[4] += add[2]
        calculate_discount(employee_discount_num1)
        answerr2 = input("Would you like to make a new purchase? (Y/N) ")
        if answerr2.lower() == "n":
            display_employee_summary()
            ans3 = input("Would you like to go to the Menu? (Y/N) ")
            if ans3.lower() == "y":
                menu()
            else:
                exit()
    else:
        answerr2 = input("Would you like to make a new purchase? (Y/N) ")
        if answerr2.lower() == "n":
            print(employee_list)
            ans3 = input("Would you like to go to the Menu? (Y/N) ")
            if ans3.lower() == "y":
                menu()
            else:
                exit()
        else:
            make_purchase()

def calculate_discount(num):
    dscnt = 0
    for q in employee_list:
        if q[6] == num:
            if q[2] == "manager" and dscnt != 21:
                q[5] += 10
            elif q[2] == "hourly" and dscnt != 21:
                q[5] += 2
            if q[3] == "1":
                q[5] += 2
            elif q[3] == "2":
                q[5] += 4
            elif q[3] == "3":
                q[5] += 6
            elif q[3] == "4":
                q[5] += 8
            elif q[3] == "5":
                q[5] += 10

def display_employee_summary():

    print("Employee ID,Employee Name,Employee Type,Years Worked,Total Purchased,Total Discount,Employee Discount Number ")
    for i in employee_list:
        print(i)
    ans4 = input("Would you like to go to the Menu? (Y/N) ")
    if ans4.lower() == "y":
        menu()
    else:
        exit()

def menu():
    print("-" * 27)
    print("| 1- Create Employee      |")
    print("| 2- Create Item          |")
    print("| 3- Make Purchase        |")
    print("| 4- All Employee Summary |")
    print("| 5- Exit                 |")
    print("-" * 27)
    askmenu = int(input("Choose an option: "))
    if askmenu == 1:
        create_employee()
    elif askmenu == 2:
        create_item()
    elif askmenu == 3:
        make_purchase()
    elif askmenu == 4:
        display_employee_summary()
    elif askmenu == 5:
        exit()
    else:
        print("Wrong Input")
        menu()

menu()
