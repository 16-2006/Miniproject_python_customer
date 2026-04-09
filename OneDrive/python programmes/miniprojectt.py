#Inventry
veg=['carrot','tomato','potato','cucumber','drumsticks','redchilli','spinach','onion','mushroom','cabbage','banana','brinjal','radish']
quantity=[20,15,17,25,14,18,10,24,20,17,20,300,100]
price=[20,40,25,25,65,40,45,20,40,30,30,200,120]
cost_price=[15,30,20,15,50,30,36,15,30,24,25,180,100]
sold=[0]*len(veg)

customer_names=[]
customer_phones=[]
customer_bills=[]

SECURITY_QUESTION = "What is your shop name?"
SECURITY_ANSWER = "myshop"
OWNER_PASSWORD = ["my@123"]

while True:
    print("1.owner")
    print("2.customer")
    print("3.Exit")
    option=int(input("select the view:"))

    if option==1:
        while True:
            username=input("enter username:")
            if username=='myself':
                break
            else:
                print("enter correct username")

        while True:
            print("\n1. Enter Password")
            print("2. Forgot Password")
            pwd_choice = int(input("Select option: "))

            if pwd_choice == 1:
                password = input("enter password:")
                if password == OWNER_PASSWORD[0]:
                    print("Login successful!")
                    break
                else:
                    print("enter correct password")

            elif pwd_choice == 2:
                print(f"\nSecurity Question: {SECURITY_QUESTION}")
                answer = input("Your Answer: ")
                if answer.lower() == SECURITY_ANSWER.lower():
                    while True:
                        new_pass = int(input("Enter new password: "))
                        confirm_pass = int(input("Confirm new password: "))
                        if new_pass == confirm_pass:
                            OWNER_PASSWORD[0] = new_pass
                            print("Password reset successfully!")
                            break
                        else:
                            print("Passwords do not match")
                else:
                    print("Wrong answer!")

        while True:
            print("1.view menu")
            print("2.add item")
            print("3.delete item")
            print("4.modify item")
            print("5.sales report")
            print("6.profit report")
            print("7.customer list")
            print("8.stock report")
            print("9.Exit")
            choice=int(input("select your choice:"))

            if choice==1:
                print(f"{'Items':<15}{'Quantity':<10}{'price':<7}{'cost_price':<7}")
                for i in range(len(veg)):
                    print(f"{veg[i]:<15}{quantity[i]:<10}{price[i]:<7}{cost_price[i]:<7}")

            elif choice==2:
                item=input("enter the vegetable to add:")
                if item in veg:
                    print('already item exists! please modify if u want to add more qty')
                else:    
                    qnty=float(input("enter the quantity:"))
                    prc=float(input("enter the price:"))
                    cprice=float(input("enter cost price:"))
                    veg.append(item)
                    quantity.append(qnty)
                    price.append(prc)
                    cost_price.append(cprice)
                    sold.append(0)

            elif choice==3:
                item=input("enter vegetable to delete:")
                if item in veg:
                    index=veg.index(item)
                    veg.pop(index)
                    quantity.pop(index)
                    price.pop(index)
                    sold.pop(index)
                    cost_price.pop(index)
                    print("vegetable removed successfully")

            elif choice==4:
                item=input("enter vegetable to modify:")
                if item in veg:
                    index=veg.index(item)
                    quantity[index]=float(input("enter new qnty:"))
                    price[index]=float(input("enter new price:"))
                    print("Modified successfully")

            elif choice==5:
                print("-------SALES REPORT-------")
                total_sales=0
                for i in range(len(veg)):
                    sale_amount=sold[i]*price[i]
                    total_sales += sale_amount
                    print(f"{veg[i]:<15} --sold: {sold[i]:<5} kgs {sale_amount:<10}")
                print("Total sales:",total_sales)

            elif choice==6:
                print("-------PROFIT REPORT-------")
                total_profit=0
                for i in range(len(veg)):
                    profit=(price[i]-cost_price[i])*sold[i]
                    total_profit += profit
                    print(f"{veg[i]:<15} --profit {profit:<7}")
                print("Total profit:",total_profit)

            elif choice==7:
                print("\n-------CUSTOMER LIST-------")
                print(f"{'Name':<10}{'Phone.no':<11}{'Total':<10}")
                if len(customer_names)==0:
                    print("No Customers yet")
                else:
                    for i in range(len(customer_names)):
                        print(f"{customer_names[i]:<10}{customer_phones[i]:<11}{customer_bills[i]:<10}")

            elif choice==8:
                print("\n-------REMAINING STOCK------")
                print(f"{'Item':<15}{'Remaining Qty(kgs)':<20}")
                for i in range(len(veg)):
                    print(f"{veg[i]:<15}{quantity[i]:<20}")

            elif choice==9:
                break

    elif option==2:
        while True:
            print("welcome to the shop")
            cname=input("Enter your name: ")

            while True:
                cphone=input("Enter phone number: ")
                if len(cphone)==10:
                    break
                else:
                    print("please enter 10 digit phone number")

            cart_items=[]
            cart_qty=[]
            cart_price=[]
            cart_amount=[]

            while True:
                print("1.view menu")
                print("2.Add item")
                print("3.View cart")
                print("4.Remove item")
                print("5.Modify")
                print("6.checkout")
                choice=int(input("select your choice:"))

                if choice==1:
                    for i in range(len(veg)):
                        print(veg[i], price[i])

                elif choice==2:
                    item=input('what do you want:')
                    if item in veg:
                        idx=veg.index(item)
                        qty=float(input("How many Kgs you want:"))
                        if qty<=quantity[idx]:
                            amount=qty*price[idx]
                            quantity[idx]-=qty
                            sold[idx]+=qty
                            cart_items.append(item)
                            cart_qty.append(qty)
                            cart_price.append(price[idx])
                            cart_amount.append(amount)
                        else:
                            print('out of stock')

                elif choice==3:
                    total=0
                    for i in range(len(cart_items)):
                        print(cart_items[i], cart_qty[i], cart_amount[i])
                        total+=cart_amount[i]
                    print("Total:",total)

                elif choice==4:
                    item=input("enter item to remove:")
                    if item in cart_items:
                        idx=cart_items.index(item)
                        main_idx=veg.index(item)
                        quantity[main_idx]+=cart_qty[idx]
                        sold[main_idx]-=cart_qty[idx]
                        cart_items.pop(idx)
                        cart_qty.pop(idx)
                        cart_price.pop(idx)
                        cart_amount.pop(idx)

                elif choice==5:
                    item=input("enter item to modify:")
                    if item in cart_items:
                        idx=cart_items.index(item)
                        new_qty=float(input("enter new qty:"))
                        cart_qty[idx]=new_qty
                        cart_amount[idx]=new_qty*cart_price[idx]

                elif choice==6:
                    total=0
                    print("FINAL BILL")
                    for i in range(len(cart_items)):
                        print(cart_items[i], cart_qty[i], cart_amount[i])
                        total+=cart_amount[i]
                    print("Total:",total)

                    customer_names.append(cname)
                    customer_phones.append(cphone)
                    customer_bills.append(total)
                    break

            next_customer=input("Next customer? (yes/no): ")
            if next_customer=='no':
                break
            elif next_customer=='yes':
                continue

    elif option==3:
        break
