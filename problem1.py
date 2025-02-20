import random

def calc():
    sal = float(input("Enter monthly salary: "))
    m = input("Enter month: ")
    
    save_pct = float(input("Savings percentage: "))
    rent_pct = float(input("Rent percentage: "))
    elec_pct = float(input("Electricity percentage: "))
    
    save_amt = (save_pct / 100) * sal
    rent_amt = (rent_pct / 100) * sal
    elec_amt = (elec_pct / 100) * sal
    
    total_exp = save_amt + rent_amt + elec_amt
    rem = sal - total_exp
    
    yr_rent = rent_amt * 12
    yr_elec = elec_amt * 12
    
    sal_sq = sal ** 2
    
    add_save = 50*12
    save_div = add_save / save_amt if save_amt > 0 else 0
    
    print(f"Salary: ${sal:.2f}")
    print(f"Savings: ${save_amt:.2f}")
    print(f"Rent: ${rent_amt:.2f}")
    print(f"Electricity: ${elec_amt:.2f}")
    print(f"Total expenses: ${total_exp:.2f}")
    print(f"Remaining: ${rem:.2f}")
    print(f"Yearly Rent: ${yr_rent:.2f}")
    print(f"Yearly Electricity: ${yr_elec:.2f}")
    print(f"Salary squared: {sal_sq:.2f}")
    print(f"50 divided by savings: {save_div:.2f}")
   

if __name__ == "__main__":
    calc()
