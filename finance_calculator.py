import math

print("\nInvestment - calculates the amount of interest you will earn on your investment", "\n" "Bond - calculates the amount of interest you will have to pay on a home loan \n")

calculator_choice = input("Enter either 'investment' or 'bond':\n ").lower()

if calculator_choice == 'investment':
    deposit = 0
    rate = 0
    time = 0
    simple_interest = (deposit * (1 + rate * time))

    deposit = float(input("Enter deposit amount: "))
    
    if deposit <= 0:
        print("Deposit amount can't be less than zero")
    else:
        rate = float(input("Enter interest rate: "))
        if rate <= 0:
            print("Interest rate can't be less than zero")
        else:
            time = int(input("Enter time in years: "))
            if time < 0:
                print("Time can't be less than or equal to zero")
            else:
                print("£",deposit)
                print(rate,"%")
                print(time, "years")
                
                print("Do you want 'Simple' or 'Compound interest'?")

                interest_type = input("Please enter interest type:\n simple\n compound\n ")
                
                if interest_type == "simple":
                    print("You have chosen Simple interest")
                    total = deposit*(1 + (rate/100) * time)

                elif interest_type == "compound":
                    print("You have chosen compound interest")
                    total = deposit * pow(1 + (rate/100),time)

                else:
                    print("invalid request!")
                print(f"Balance after {time} years: £{total:.2f}")

else:
    if calculator_choice == 'bond':
        house_value = 0
        bond_rate = 0
        time = 0

        house_value = float(input("Enter house value: "))
        if house_value < 0:
            print("House value can't be less than zero")
        else:
            bond_rate = float(input("Enter interest rate: "))
            if bond_rate < 0:
                print("Interest rate can't be less than zero")
            else:
                time = int(input("Enter time in months: "))
                if time < 0:
                    print("Time can't be less than or equal to zero")
                else:
                    bond_interest = ((bond_rate/100)/12)
                    print("£",house_value)
                    print(bond_rate,"%")
                    print(time, "months")
                    print(bond_interest)
                    
                    repayment = (bond_interest * house_value)/(1-(1 + bond_interest) ** (-time))
                    print(f"Total monthly bont repayment: £{repayment:.2f}")

    else:
        print("Invalid Value Entry ")
