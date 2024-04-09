nike_shoes = {"Nike Air Force 1" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3,'Php' : 5000},
  
              "Nike Cortez" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 7000},
             
              "Nike Air Max" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 10000},
             
              "Nike Dunk Low" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 8000},
              } 

adidas_shoes = {"Adidas Samba" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 8000},

                "Adidas Stan Smith" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 5000},

                "Adidas Superstar" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 7000},

                "Adidas Ultra Boost" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3, 'Size 6' : 3, 'Php' : 10000},
                }

newbalance_shoes = {"New Balance 550" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 8000},

                    "New Balance 530" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 5000},

                    "New Balance 327" : {'Size 10' : 3, 'Size 9' : 3, 'Size 8' : 3,'Size 7' : 3,'Size 6' : 3, 'Php' : 5700},
                    }

user_account = {}

user_collection = {}

admin_user = "admin"
admin_pass = "adminpass"

def sign_up():
    print("")
    print("Create Account")
    while True:
        username = input("Create Username: ")
        if username in user_account:
            print("Username already exist")
            continue
        else:
            while True:
                password = input("Create Password: ")
                if len(password) < 8:
                    print("Password must at least 8 characters")
                else:
                    password1 = input("Re-enter Password: ")
                    balance = 0
                    if password == password1:
                        user_account[username] = {'password' : password, 'balance' : balance}
                        print("You already create an account")
                        print(f"Your username is {username} and your password is {password}.")

                        while True:
                            try:
                                print("")
                                choice = int(input("Press 1 if you want to go main menu or press 2 if you want to log in: "))
                                if choice == 1:
                                    main_menu()
                                if choice == 2:
                                    log_in()
                                else:
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)    
                    else:
                        print("Invalid password. Try again")
                        continue
            

def log_in():
    print("")
    print("Log in")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if user_account.get(username) and user_account[username]['password'] == password:
        print("Log in Successfully")
        print(f"Welcome user {username}.")
        user_menu(username)
    else:
        print("Wrong Username or Password. Try again")
        
        while True:
            try:
                choice = int(input("Press 1 to log in again or press 2 to go main menu: "))
                if choice == 1:
                    log_in()
                if choice == 2:
                    main_menu()
                else:
                    print("Invalid input. Try again")
                    continue
            except ValueError as e:
                print(e)


def admin_login():
    print("")
    print("Admin")
    while True:
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if username == admin_user and password == admin_pass:
            admin()
            break
        else:
            print("Wrong admin username or password.Try again")
            continue

def admin():
    while True:
        try:
            print("")
            print("Admin Menu")
            print("1. Edit shop")
            print("2. Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                admin_edit()
            if choice == 2:
                main_menu()
            else:
                ("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def admin_edit():
    while True:
        try:
            print("")
            print("Admin Edit")
            print("Choose the shoe brand that you want to edit")
            print("1. Nike")
            print("2. Adidas")
            print("3. New Balance")
            print("4. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                edit_nike()
            if choice == 2:
                edit_adidas()
            if choice == 3:
                edit_newbalance()
            if choice == 4:
                admin()
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def edit_nike():
    while True:
        try:
            print("")
            print("Edit Nike")
            print([nike_shoes])
            print("1. Edit Price")
            print("2. Edit Size Quantity")
            print("3. Add New Shoes")
            print("4. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("")
                print("Edit Price")
                while True:
                    shoe_name = input("Type the shoe name you want to edit: ")
                    if shoe_name in nike_shoes:
                        new_price = int(input("Enter the new price: "))
                        nike_shoes[shoe_name]['Php'] = new_price
                        print("Price is updated successfully")
                        print([nike_shoes])
                        while True:
                            try:
                                choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                                if choice == 1:
                                    edit_nike()
                                if choice == 2:
                                    admin_edit()
                                else: 
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)
                    else:
                        print("Shoe name doesn't exist")
                        continue

            if choice == 2:
                print("")
                print("Edit Size Quantity")
                while True:
                    shoe_name = input("Type the shoe name you want to edit: ")
                    if shoe_name in nike_shoes:
                        print("Choose the size that you want to edit the quantity")
                        print("Enter [1] for Size 10")
                        print("Enter [2] for Size 9")
                        print("Enter [3] for Size 8")
                        print("Enter [4] for Size 7")
                        print("Enter [5] for Size 6")

                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            nike_shoes[shoe_name]['Size 10'] = new_size_quantity
                            print("Size 10 quantity is updated successfully")
                            print([nike_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_nike()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 2:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            nike_shoes[shoe_name]['Size 9'] = new_size_quantity
                            print("Size 9 quantity is updated successfully")
                            print([nike_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_nike()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 3:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            nike_shoes[shoe_name]['Size 8'] = new_size_quantity
                            print("Size 8 quantity is updated successfully")
                            print([nike_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_nike()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 4:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            nike_shoes[shoe_name]['Size 7'] = new_size_quantity
                            print("Size 7 quantity is updated successfully")
                            print([nike_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_nike()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 5:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            nike_shoes[shoe_name]['Size 6'] = new_size_quantity
                            print("Size 6 quantity is updated successfully")
                            print([nike_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_nike()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)
                        else:
                            print("Invalid input. Try again")
                            continue
                    else:
                        print("Shoe name doesn't exist")
                        continue

            if choice == 3:
                print("")
                print("Add New Nike Shoes")
                shoe_name = input("Enter the shoe name that you want to add: ")
                price = int(input("Enter the price of shoes that you want to add: "))
                size_10 = int(input("Enter size 10 quantity: "))
                size_9 = int(input("Enter the size 9 quantity: "))
                size_8 = int(input("Enter the size 8 quantity: "))
                size_7 = int(input("Enter the size 7 quantity: "))
                size_6 = int(input("Enter the size 6 quantity: "))
                nike_shoes[shoe_name] = {'Size 10' : size_10, 'Size 9' : size_9, 'Size 8' : size_8, 'Size 7' : size_7, 'Size 6' : size_6, 'Php': price}
                print(f"{shoe_name} has been added in Nike Shoes successfully")
                print([nike_shoes])
                while True:
                    try:
                        choice = int(input("Press 1 if you want to edit nike again or press 2 if you want to go back: "))

                        if choice == 1:
                            edit_nike()
                        if choice == 2:
                            admin_edit()
                        else: 
                            print("Invalid input. Try again")
                            continue
                    except ValueError as e:
                        print(e)

            if choice == 4:
                admin_edit()
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def edit_adidas():
    while True:
        try:
            print("")
            print("Edit Adidas")
            print([adidas_shoes])
            print("1. Edit Price")
            print("2. Edit Size Quantity")
            print("3. Add New Shoes")
            print("4. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("")
                print("Edit Price")
                while True:
                    shoe_name = input("Type the shoe name you want to edit: ")
                    if shoe_name in adidas_shoes:
                        new_price = int(input("Enter the new price: "))
                        adidas_shoes[shoe_name]['Php'] = new_price
                        print("Price is updated successfully")
                        print([adidas_shoes])
                        while True:
                            try:
                                choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                                if choice == 1:
                                    edit_adidas()
                                if choice == 2:
                                    admin_edit()
                                else:
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)
                    else:
                        print("Shoe name doesn't exist")
                        continue

            if choice == 2:
                print("")
                print("Edit Size Quantity")
                while True:
                    shoe_name = input("Type the shoe name you want to edit: ")
                    if shoe_name in adidas_shoes:
                        print("Choose the size that you want to edit the quantity")
                        print("Enter [1] for Size 10")
                        print("Enter [2] for Size 9")
                        print("Enter [3] for Size 8")
                        print("Enter [4] for Size 7")
                        print("Enter [5] for Size 6")

                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            adidas_shoes[shoe_name]['Size 10'] = new_size_quantity
                            print("Size 10 quantity is updated successfully")
                            print([adidas_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_adidas()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)
 
                        if choice == 2:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            adidas_shoes[shoe_name]['Size 9'] = new_size_quantity
                            print("Size 9 quantity is updated successfully")
                            print([adidas_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_adidas()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 3:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            adidas_shoes[shoe_name]['Size 8'] = new_size_quantity
                            print("Size 8 quantity is updated successfully")
                            print([adidas_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_adidas()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 4:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            adidas_shoes[shoe_name]['Size 7'] = new_size_quantity
                            print("Size 7 quantity is updated successfully")
                            print([adidas_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_adidas()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 5:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            adidas_shoes[shoe_name]['Size 5'] = new_size_quantity
                            print("Size 5 quantity is updated successfully")
                            print([adidas_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_adidas()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                    else:
                        print("Shoe name doesn't exist")
                        continue            

            if choice == 3:
                print("")
                print("Add New Adidas Shoes")
                shoe_name = input("Enter the shoe name that you want to add: ")
                price = int(input("Enter the price of shoes that you want to add: "))
                size_10 = int(input("Enter size 10 quantity: "))
                size_9 = int(input("Enter the size 9 quantity: "))
                size_8 = int(input("Enter the size 8 quantity: "))
                size_7 = int(input("Enter the size 7 quantity: "))
                size_6 = int(input("Enter the size 6 quantity: "))
                adidas_shoes[shoe_name] = {'Size 10' : size_10, 'Size 9' : size_9, 'Size 8' : size_8, 'Size 7' : size_7, 'Size 6' : size_6, 'Php': price}
                print(f"{shoe_name} has been added in Adidas Shoes successfully")
                print([adidas_shoes])
                while True:
                    try:
                        choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                        if choice == 1:
                            edit_adidas()
                        if choice == 2:
                            admin_edit()
                        else: 
                            print("Invalid input. Try again")
                            continue
                    except ValueError as e:
                        print(e)

            if choice == 4:
                admin_edit()
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def edit_newbalance():
    while True:
        try:
            print("")
            print("Edit New Balance")
            print([newbalance_shoes])
            print("1. Edit Price")
            print("2. Edit Size Quantity")
            print("3. Add New Shoes")
            print("4. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("")
                print("Edit Price")
                while True:
                    shoe_name = input("Type the shoe name you want to edit: ")
                    if shoe_name in newbalance_shoes:
                        new_price = int(input("Enter the new price: "))
                        newbalance_shoes[shoe_name]['Php'] = new_price
                        print("Price is updated successfully")
                        print([newbalance_shoes])
                        while True:
                            try:
                                choice = int(input("Press 1 if you want to edit new balance again or press 2 if you want to go back: "))

                                if choice == 1:
                                    edit_newbalance()
                                if choice == 2:
                                    admin_edit()
                                else: 
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)
                    else:
                        print("Shoe name doesn't exist")
                        continue

            if choice == 2:
                print("")
                print("Edit Size Quantity")
                while True:
                    shoe_name = input("Type the shoe name you want to edit: ")
                    if shoe_name in newbalance_shoes:
                        print("Choose the size that you want to edit the quantity")
                        print("Enter [1] for Size 10")
                        print("Enter [2] for Size 9")
                        print("Enter [3] for Size 8")
                        print("Enter [4] for Size 7")
                        print("Enter [5] for Size 6")

                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            newbalance_shoes[shoe_name]['Size 10'] = new_size_quantity
                            print("Size 10 quantity is updated successfully")
                            print([newbalance_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit new balance again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_newbalance()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)
 
                        if choice == 2:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            newbalance_shoes[shoe_name]['Size 9'] = new_size_quantity
                            print("Size 9 quantity is updated successfully")
                            print([newbalance_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit new balance again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_newbalance()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 3:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            newbalance_shoes[shoe_name]['Size 8'] = new_size_quantity
                            print("Size 8 quantity is updated successfully")
                            print([newbalance_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit new balance again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_newbalance()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 4:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            newbalance_shoes[shoe_name]['Size 7'] = new_size_quantity
                            print("Size 7 quantity is updated successfully")
                            print([newbalance_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit new balance again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_newbalance()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)

                        if choice == 5:
                            new_size_quantity = int(input("Enter the new size quantity: "))
                            newbalance_shoes[shoe_name]['Size 6'] = new_size_quantity
                            print("Size 6 quantity is updated successfully")
                            print([newbalance_shoes])
                            while True:
                                try:
                                    choice = int(input("Press 1 if you want to edit new balance again or press 2 if you want to go back: "))

                                    if choice == 1:
                                        edit_newbalance()
                                    if choice == 2:
                                        admin_edit()
                                    else:
                                        print("Invalid input. Try again")
                                        continue
                                except ValueError as e:
                                    print(e)
                        else:
                            print("Invalid input. Try again")
                            continue
                    else:
                        print("Shoe name doesn't exist")
                        continue

            if choice == 3:
                print("")
                print("Add New 'New Balance' Shoes")
                shoe_name = input("Enter the shoe name that you want to add: ")
                price = int(input("Enter the price of shoes that you want to add: "))
                size_10 = int(input("Enter size 10 quantity: "))
                size_9 = int(input("Enter the size 9 quantity: "))
                size_8 = int(input("Enter the size 8 quantity: "))
                size_7 = int(input("Enter the size 7 quantity: "))
                size_6 = int(input("Enter the size 6 quantity: "))
                newbalance_shoes[shoe_name] = {'Size 10' : size_10, 'Size 9' : size_9, 'Size 8' : size_8, 'Size 7' : size_7, 'Size 6' : size_6, 'Php': price}
                print(f"{shoe_name} has been added in New Balance Shoes successfully")
                print([newbalance_shoes])
                while True:
                    try:
                        choice = int(input("Press 1 if you want to edit adidas again or press 2 if you want to go back: "))

                        if choice == 1:
                            edit_newbalance()
                        if choice == 2:
                            admin_edit()
                        else: 
                            print("Invalid input. Try again")
                            continue
                    except ValueError as e:
                        print(e)

            if choice == 4:
                admin_edit()
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def user_menu(username):
    while True:
        try:
            print("")
            print("User Menu")
            print("1. Go Shopping")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Shoe Collection")
            print("5. Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                shopping(username)
            if choice == 2:
                deposit(username)
            if choice == 3:
                check_balance(username)
            if choice == 4:
                shoe_collection(username)
            if choice == 5:
                main_menu()
            else: 
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def shopping(username):
    print("")
    while True:
        try: 
            print("Go Shopping")
            print("1. View Available Shoes")
            print("2. Buy")
            print("3. User Menu")
        
            choice = int(input("Enter your choice: "))

            if choice == 1:
                view_available(username)
            if choice == 2:
                buy_shoes(username)
            if choice == 3:
                user_menu(username)
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)    


def view_available(username):
    while True:
        try:
            print("")
            print("View Available Shoes")
            print("1. Nike")
            print("2. Adidas")
            print("3. New Balance")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                print([nike_shoes])
                print("")
                while True:
                    try:
                        choice = int(input("Press 1 if you want to buy shoes or press 2 if you want to go user menu: "))
                        if choice == 1:
                            buy_shoes(username)
                        if choice == 2:
                            user_menu(username)
                        else:
                            print("Invalid input. Try again")
                            continue
                    except ValueError as e:
                        print(e)

            if choice == 2:
                print([adidas_shoes])
                print("")
                while True:
                    try:
                        choice = int(input("Press 1 if you want to buy shoes or press 2 if you want to go user menu: "))
                        if choice == 1:
                            buy_shoes(username)
                        if choice == 2:
                            user_menu(username)
                        else:
                            print("Invalid input. Try again")
                            continue
                    except ValueError as e:
                        print(e)

            if choice == 3:
                print([newbalance_shoes])
                print("")
                while True:
                    try:
                        choice = int(input("Press 1 if you want to buy shoes or press 2 if you want to go user menu: "))
                        if choice == 1:
                            buy_shoes(username)
                        if choice == 2:
                            user_menu(username)
                        else:
                            print("Invalid input. Try again")
                            continue
                    except ValueError as e:
                        print(e)
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def buy_shoes(username):
    while True:
        try:
            print("")
            print("Choose shoe brand that you want to buy")
            print("1. Nike")
            print("2. Adidas")
            print("3. New Balance")
            print("4. Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Nike")
                print(nike_shoes)

                buy_nike = input("Enter the shoes that you want to buy: ")
                if buy_nike not in nike_shoes:
                    print("Not available")
                    buy_shoes(username)
                if buy_nike in nike_shoes:
                        print("Choose size of the shoes you want to buy: ")
                        print("Enter [1] for Size 10")
                        print("Enter [2] for Size 9")
                        print("Enter [3] for Size 8")
                        print("Enter [4] for Size 7")
                        print("Enter [5] for Size 6")    

                        choice = int(input("Enter your choice: "))
                        while True:
                            try:

                                if choice == 1:
                                    if nike_shoes[buy_nike]['Size 10'] > 0:
                                        if user_account[username]['balance'] >= nike_shoes[buy_nike]['Php']:
                                            user_account[username]['balance'] -= nike_shoes[buy_nike]['Php']
                                            nike_shoes[buy_nike]['Size 10'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_nike]
                                            else:
                                                user_collection[username].append(buy_nike)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 10 is out of stock")
                                        break

                                if choice == 2:
                                    if nike_shoes[buy_nike]['Size 9'] > 0:
                                        if user_account[username]['balance'] >= nike_shoes[buy_nike]['Php']:
                                            user_account[username]['balance'] -= nike_shoes[buy_nike]['Php']
                                            nike_shoes[buy_nike]['Size 9'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_nike]
                                            else:
                                                user_collection[username].append(buy_nike)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 9 is out of stock")
                                        break
            
                                if choice == 3:
                                    if nike_shoes[buy_nike]['Size 8'] > 0:
                                        if user_account[username]['balance'] >= nike_shoes[buy_nike]['Php']:
                                            user_account[username]['balance'] -= nike_shoes[buy_nike]['Php']
                                            nike_shoes[buy_nike]['Size 8'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_nike]
                                            else:
                                                user_collection[username].append(buy_nike)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 8 is out of stock")
                                        break

                                if choice == 4:
                                    if nike_shoes[buy_nike]['Size 7'] > 0:
                                        if user_account[username]['balance'] >= nike_shoes[buy_nike]['Php']:
                                            user_account[username]['balance'] -= nike_shoes[buy_nike]['Php']
                                            nike_shoes[buy_nike]['Size 7'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_nike]
                                            else:
                                                user_collection[username].append(buy_nike)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 7 is out of stock")
                                        break 

                                if choice == 5:
                                    if nike_shoes[buy_nike]['Size 6'] > 0:
                                        if user_account[username]['balance'] >= nike_shoes[buy_nike]['Php']:
                                            user_account[username]['balance'] -= nike_shoes[buy_nike]['Php']
                                            nike_shoes[buy_nike]['Size 6'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_nike]
                                            else:
                                                user_collection[username].append(buy_nike)               
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)   
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 6 is out of stock")
                                        break
                                else:
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)

            if choice == 2:

                print("Adidas")
                print(adidas_shoes)

                buy_adidas = input("Enter the shoes that you want to buy: ")
                if buy_adidas not in adidas_shoes:
                    print("Not available")
                    buy_shoes(username)
                if buy_adidas in adidas_shoes:
                        print("Choose size of the shoes you want to buy: ")
                        print("Enter [1] for Size 10")
                        print("Enter [2] for Size 9")
                        print("Enter [3] for Size 8")
                        print("Enter [4] for Size 7")
                        print("Enter [5] for Size 6")    

                        choice = int(input("Enter your choice: "))
                        while True:
                            try:

                                if choice == 1:
                                    if adidas_shoes[buy_adidas]['Size 10'] > 0:
                                        if user_account[username]['balance'] >= adidas_shoes[buy_adidas]['Php']:
                                            user_account[username]['balance'] -= adidas_shoes[buy_adidas]['Php']
                                            adidas_shoes[buy_adidas]['Size 10'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_adidas]
                                            else:
                                                user_collection[username].append(buy_adidas)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 10 is out of stock")
                                        break

                                if choice == 2:
                                    if adidas_shoes[buy_adidas]['Size 9'] > 0:
                                        if user_account[username]['balance'] >= adidas_shoes[buy_adidas]['Php']:
                                            user_account[username]['balance'] -= adidas_shoes[buy_adidas]['Php']
                                            adidas_shoes[buy_adidas]['Size 9'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_adidas]
                                            else:
                                                user_collection[username].append(buy_adidas)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 9 is out of stock")
                                        break
            
                                if choice == 3:
                                    if adidas_shoes[buy_adidas]['Size 8'] > 0:
                                        if user_account[username]['balance'] >= adidas_shoes[buy_adidas]['Php']:
                                            user_account[username]['balance'] -= adidas_shoes[buy_adidas]['Php']
                                            adidas_shoes[buy_adidas]['Size 8'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_adidas]
                                            else:
                                                user_collection[username].append(buy_adidas)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 8 is out of stock")
                                        break

                                if choice == 4:
                                    if adidas_shoes[buy_adidas]['Size 7'] > 0:
                                        if user_account[username]['balance'] >= adidas_shoes[buy_adidas]['Php']:
                                            user_account[username]['balance'] -= adidas_shoes[buy_adidas]['Php']
                                            adidas_shoes[buy_adidas]['Size 7'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_adidas]
                                            else:
                                                user_collection[username].append(buy_adidas)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 7 is out of stock")
                                        break 

                                if choice == 5:
                                    if adidas_shoes[buy_adidas]['Size 6'] > 0:
                                        if user_account[username]['balance'] >= adidas_shoes[buy_adidas]['Php']:
                                            user_account[username]['balance'] -= adidas_shoes[buy_adidas]['Php']
                                            adidas_shoes[buy_adidas]['Size 6'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_adidas]
                                            else:
                                                user_collection[username].append(buy_adidas)               
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)   
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 6 is out of stock")
                                        break
                                else:
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)

            if choice == 3:
                print("New Balance")
                print(newbalance_shoes)

                buy_newbalance = input("Enter the shoes that you want to buy: ")
                if buy_newbalance not in newbalance_shoes:
                    print("Not available")
                    buy_shoes(username)
                if buy_newbalance in newbalance_shoes:
                        print("Choose size of the shoes you want to buy: ")
                        print("Enter [1] for Size 10")
                        print("Enter [2] for Size 9")
                        print("Enter [3] for Size 8")
                        print("Enter [4] for Size 7")
                        print("Enter [5] for Size 6")    

                        choice = int(input("Enter your choice: "))
                        while True:
                            try:

                                if choice == 1:
                                    if newbalance_shoes[buy_newbalance]['Size 10'] > 0:
                                        if user_account[username]['balance'] >= newbalance_shoes[buy_newbalance]['Php']:
                                            user_account[username]['balance'] -= newbalance_shoes[buy_newbalance]['Php']
                                            newbalance_shoes[buy_newbalance]['Size 10'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_newbalance]
                                            else:
                                                user_collection[username].append(buy_newbalance)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 10 is out of stock")
                                        break

                                if choice == 2:
                                    if newbalance_shoes[buy_newbalance]['Size 9'] > 0:
                                        if user_account[username]['balance'] >= newbalance_shoes[buy_newbalance]['Php']:
                                            user_account[username]['balance'] -= newbalance_shoes[buy_newbalance]['Php']
                                            newbalance_shoes[buy_newbalance]['Size 9'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_newbalance]
                                            else:
                                                user_collection[username].append(buy_newbalance)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 9 is out of stock")
                                        break
            
                                if choice == 3:
                                    if newbalance_shoes[buy_newbalance]['Size 8'] > 0:
                                        if user_account[username]['balance'] >= newbalance_shoes[buy_newbalance]['Php']:
                                            user_account[username]['balance'] -= newbalance_shoes[buy_newbalance]['Php']
                                            newbalance_shoes[buy_newbalance]['Size 8'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_newbalance]
                                            else:
                                                user_collection[username].append(buy_newbalance)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 8 is out of stock")
                                        break

                                if choice == 4:
                                    if newbalance_shoes[buy_newbalance]['Size 7'] > 0:
                                        if user_account[username]['balance'] >= newbalance_shoes[buy_newbalance]['Php']:
                                            user_account[username]['balance'] -= newbalance_shoes[buy_newbalance]['Php']
                                            newbalance_shoes[buy_newbalance]['Size 7'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_newbalance]
                                            else:
                                                user_collection[username].append(buy_newbalance)
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")   
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 7 is out of stock")
                                        break 

                                if choice == 5:
                                    if newbalance_shoes[buy_newbalance]['Size 6'] > 0:
                                        if user_account[username]['balance'] >= newbalance_shoes[buy_newbalance]['Php']:
                                            user_account[username]['balance'] -= newbalance_shoes[buy_newbalance]['Php']
                                            newbalance_shoes[buy_newbalance]['Size 6'] -= 1
                                            if username not in user_collection:
                                                user_collection[username] = [buy_newbalance]
                                            else:
                                                user_collection[username].append(buy_newbalance)               
                                            print(f"You already bought your chosen item. Your new balance is {user_account[username]['balance']}.")
                                            while True:
                                                try:
                                                    choice = int(input("Press 1 if you want to buy again or press 2 if you want go to user menu: "))
                                                    if choice == 1:
                                                        buy_shoes(username)
                                                    if choice == 2:
                                                        user_menu(username)
                                                    else:
                                                        print("Invalid input. Try again")
                                                        continue
                                                except ValueError as e:
                                                    print(e)   
                                        else:
                                            print("Your balance is not enough to buy your chosen item")
                                            user_menu(username)        
                                    else:
                                        print("Size 6 is out of stock")
                                        break
                                else:
                                    print("Invalid input. Try again")
                                    continue
                            except ValueError as e:
                                print(e)

            if choice == 4:
                shopping(username)

            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)
    

def deposit(username):
    while True:
        try:
            print("")
            print("Deposit")
            dep_amt = int(input("Enter the amount you want to deposit: "))

            user_account[username]['balance'] += dep_amt
            print(f"You successfully deposit {dep_amt}, your new balance is {user_account[username]['balance']}")

            while True:
                try:
                    choice = int(input("Press 1 to go user menu: "))
                    if choice == 1:
                        user_menu(username)
                    else:
                        print("Invalid input, Try again")
                        continue 
                except ValueError as e:
                    print(e)
        except ValueError as e:
            print(e)


def check_balance(username):
    while True:
        try:
            print("")
            print("Balance")
            print(f"Your current balance is {user_account[username]['balance']}")
            choice = int(input("Press 1 to go user menu: "))
            if choice == 1:
                user_menu(username)
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


def shoe_collection(username):
    while True:
        try:
            print("")
            print("Shoe Collection")
            if username in user_collection:
                print(f"Your shoe collection: {user_collection[username]} ")
            else: 
                print("Your shoe collection is empty")
                
            choice = int(input("Press 1 to go user menu: "))
            if choice == 1:
                user_menu(username)
            else:
                print("Invalid input. Try again")
            continue
        except ValueError as e:
            print(e)  


def main_menu():
    while True:
        try:
            print("")
            print("MAIN MENU")
            print("1. Create Account")
            print("2. Log In Account")
            print("3. Admin Log In")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                sign_up()
            if choice == 2:
                log_in()
            if choice == 3:
                admin_login()
            elif choice == 4:
                print("Exiting")
                quit()
            else:
                print("Invalid input. Try again")
                continue
        except ValueError as e:
            print(e)


main_menu()