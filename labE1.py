# q1
# a
# def main():
#     for num in range(11):
#         square = num ** 2
#         print(f"The square of {num} is: {square}")

# if __name__ == "__main__":
#     main()


#b
# def main():
#     total_sum = 0
#     for num in range(0, 11, 2):
#         total_sum += num
#     print("The sum of all even numbers from 0 to 10 is:", total_sum)

# if __name__ == "__main__":
#     main()


#2
# def validate_username(username):
#     if not username.isalpha():
#         print("Error: Username must contain only alphabetical characters.")
#         return False
#     return True

# def validate_password(password):
#     if not password.isdigit():
#         print("Error: Password must contain only numeric characters.")
#         return False
#     if len(password) < 5:
#         print("Error: Password must be at least 5 characters long.")
#         return False
#     return True

# def main():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if validate_username(username) and validate_password(password):
#         print("Authentication successful!")
#     else:
#         print("Authentication failed.")

# if __name__ == "__main__":
#     main()


# #q3
def calculate_monthly_payment(car_price, down_payment, loan_period):
    loan_amount = car_price - down_payment
    if down_payment < car_price * 0.1:
        print("You are not eligible for the bank loan.")
        return

    interest_rate = 0.027
    total_interest = interest_rate * loan_amount * loan_period
    total_loan_amount = loan_amount + total_interest
    total_months = loan_period * 12
    monthly_installment = total_loan_amount / total_months

    return monthly_installment

def main():
    car_price = 103300
    down_payment = float(input("Enter down payment amount: "))
    loan_period = int(input("Enter loan period in years: "))

    monthly_payment = calculate_monthly_payment(car_price, down_payment, loan_period)
    if monthly_payment is not None:
        print("Your monthly payment will be RM {:.2f}".format(monthly_payment))

if __name__ == "__main__":
    main()



