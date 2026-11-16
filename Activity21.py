#List
passengers = ["VEN", "LETLET", "DAN"]
passengers.append("CEDRICK")
passengers.insert(0, "Yani")
passengers.remove("VEN")
x = passengers.pop()
y = passengers.pop(0)
"LETLET" in passengers
passengers.reverse()


# Jeepney Simulator (interactive)
route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers)," of ", SEATS, " seats")
    print("1 Sakay 2 Priority seat 3 Para po!" )
    print("4 Baba sa pinto 5 Baba sa harap" )
    print("6 Seat check 7 balikan 8 Exit")
    choice = input("choice: ")
    
    if choice =="1":
        if len(passengers) == SEATS:
            print("Puno na")
        else:
            name = input("Name: ")
            passengers.append(name)
            total += FARE
        print(name, "Boarded")
    
    elif choice =="2":
        if len(passengers) == SEATS:
            print("Puno na")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total += FARE
            print(name, "Took the priority seat")
    elif choice =="3":
        name = input("Name: ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. Ingat!")
        else:
            print(name, "is not on this jeep")
    elif choice =="4":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            left = passengers.pop()
            print(left, "got off at the door, Ingats!")
    elif choice =="5":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            front = passengers.pop(0)
            print(front, "got off at the front, Ingats!")
    elif choice == "6":
        for i in range(len(passengers)):
            print(f"{i+1}. {passengers[i]}") 
    elif choice == "7":
        route.reverse()
        print("Route:", route)
    elif choice == "8":
        print("Total fare collected: ₱", total)
        break
    else:
        print("Invalid choice. Please try again.")
