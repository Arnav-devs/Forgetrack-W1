def add_expense():
    date = input("Enter date: (DD/MM/YYYY) ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note: ")

    with open("data.txt", "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")
    

def view_All_expenses():
    sum = 0

    print("Date\tCategory\tAmount\tNote")
    print("-" * 50)

    with open("data.txt", "r") as file:
        for line in file:
            date, category, amount, note = line.strip().split(",")

            print(f"{date}\t{category}\t{amount}\t{note}")

            sum += float(amount)

    print("-" * 35)
    print(sum)

def filter_by_category():
    search = input("Enter category: ")
    sum = 0

    with open("data.txt" , "r") as file:
        for line in file:
            date, category, amount, note = line.strip().split(",")

            if category.lower() == search.lower():
                print(f"{date}\t{category}\t{amount}\t{note}")
                sum += float(amount)
    

    print(sum)

while True:
    print("\n1. Add an Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. Exit")

    inp = input("input: ")

    if inp == "1":
        add_expense()
    elif inp == "2":
        view_All_expenses()
    elif inp == "3":
        filter_by_category()
    elif inp == "4":
        break
    
