import math

print('''What do you want to calculate? 
type "n" for number of monthly payments, 
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
x = input()

if x == "n":
    print("Enter the loan principal:")
    loan = int(input())

    print("Enter the monthly payment:")
    payment = int(input())

    print("Enter the loan interest:")
    percent = float(input())

    month_interest = percent / (12 * 100)

    first = payment / (payment - month_interest * loan)

    n = math.ceil(math.log(first, 1 + month_interest))

    years = n // 12
    months = n - years * 12
    if years < 1:
        print(f"It will take {months} months to repay this loan!")
    if years == 1:
        print(f"It will take 1 year to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")



if x == "a":
    print("Enter the loan principal:")
    loan = int(input())

    print("Enter the number of periods:")
    months = int(input())

    print("Enter the loan interest:")
    percent = float(input())


    month_interest = percent / (12 * 100)

    first = math.pow((1 + month_interest), months)

    second = (month_interest * first) / (first - 1)

    a = loan * second

    print(f"Your monthly payment = {math.ceil(a)} !")


if x == "p":
    print("Enter the annuity payment:")
    payment = float(input())

    print("Enter the number of periods:")
    months = int(input())

    print("Enter the loan interest:")
    percent = float(input()) 


    month_interest = percent / (12 * 100)

    first = math.pow((1 + month_interest), months)

    second = (month_interest * first) / (first - 1)

    p = payment / second

    print(f"Your loan principal = {int(p)} !")