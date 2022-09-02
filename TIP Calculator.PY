print("Welcome to the tio calculator")
Total_bill= float(input("What was the total bill ?"))
percentage_tip=int(input("What percentage tip would you like to give ? 10 ,12 or 15"))
No_of_people=int(input(" How many people to split the bill  "))
pay=((Total_bill*(percentage_tip*0.01))+Total_bill)/No_of_people
print("Each person should pay:",round(pay,2)) # Rounding float numbers