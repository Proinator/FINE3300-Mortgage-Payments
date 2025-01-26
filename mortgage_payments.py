def mortgage_payments(principal, rate, amortization):
    """
    Calculate the periodic mortgage payments based on the present value of annuity factor.

    Args:
        principal (float): Principal loan amount.
        rate (float): Quoted annual interest rate (as a percentage).
        amortization (int): Amortization period in years.

    Returns:
        tuple: Monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly payments.
    """
    # Convert the quoted rate to a decimal and calculate periodic rates
    rq = rate / 100
    r_monthly = (1 + rq / 2)**(2 / 12) - 1
    r_semi_monthly = (1 + rq / 2)**(2 / 24) - 1
    r_bi_weekly = (1 + rq / 2)**(2 / 26) - 1
    r_weekly = (1 + rq / 2)**(2 / 52) - 1

    # Calculate the total number of payments
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52

    # Calculate payments using the present value of annuity formula
    monthly_payment = principal / ((1 - (1 + r_monthly)**-n_monthly) / r_monthly)
    semi_monthly_payment = principal / ((1 - (1 + r_semi_monthly)**-n_semi_monthly) / r_semi_monthly)
    bi_weekly_payment = principal / ((1 - (1 + r_bi_weekly)**-n_bi_weekly) / r_bi_weekly)
    weekly_payment = principal / ((1 - (1 + r_weekly)**-n_weekly) / r_weekly)
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4

    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2),
    )

# Prompt the user for inputs
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted annual interest rate (in %): "))
amortization = int(input("Enter the amortization period (in years): "))

# Calculate payments using the mortgage_payments function
payments = mortgage_payments(principal, rate, amortization)

# Display the results
print(f"\nMonthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")