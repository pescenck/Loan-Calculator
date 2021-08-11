'''This code will accept inputs from the Windows Command Line Interface (cp) and utilize those imputs towards
calculating different types of loan payments. There are two main loan repayment types that this code can calculate
results for: annuity loans and differenciated payment loans. The user will input values as parameters into the
Windows Command Line Interface and the loan calculator will produce a result based on the parameters entered '''

import math
import argparse

# Create an ArgumentParser object which will store all the information about the arguments:
parser = argparse.ArgumentParser()  # Use the argument parser method to initialize the parser.

# There are 5 arguments total that need to be added to the parser in order to utilize within the code body.
parser.add_argument("-type", "--type", choices=['diff', 'annuity'],
                    help="Select 'diff' for the differenciated loan \
                         calculation type or 'annuity' for the annuity loan calculations")
parser.add_argument("-payment", "--payment", help="Monthly payment used for the annuity loan calculation type")
parser.add_argument("-principal", "--principal", help="Principal of the loan used for both loan calculation types")
parser.add_argument("-periods", "--periods", help="Period of the loan repayment used for both calculation types")
parser.add_argument("-interest", "--interest", help="Interest of the loan which is always required for both loan types")

# The parse_args() method is used for reading argument strings from the command line and collecting parameters to be
# used within the code body:
calculator_parameters = parser.parse_args()


# First, define a function that checks the calculator parameters entered by the user to ensure that they are correct.
def check_calculator_parameters_for_error(parameters):
    # The user can only enter one of two calculation types. If the user enters an incorrect value or no value then
    # print the error message and exit the code.
    if parameters.type != "diff" and parameters.type != "annuity":
        print("Incorrect parameters.")
        exit()

    # If the user enters "diff" as the calculation type, and they also enter a payment, then print the error message
    # and exit the code because this calculation type cannot accept payment as a parameter.
    if parameters.type == "diff" and parameters.payment is not None:
        print("Incorrect parameters.")
        exit()

    # The amount of interest on the loan is always required because this calculator cannot calculate this. If the
    # user does not enter any parameter for the interest argument then print the error message and exit the code.
    if parameters.interest is None:
        print("Incorrect parameters.")
        exit()

    # 4 out of 5 arguments are required as input parameters by the user. This section of the error checker function
    # will check to see if the user has entered the correct number of arguments.
    # It will also check each non-string parameter to ensure positive values.

    calculator_parameter_list = []

    # The type of calculation does not need to be checked for negative values because it is a string.
    # If the error checker function has not exited the code yet by this point,
    # then that ensures that the user entered a correct parameter for the type argument.
    if parameters.type is not None:
        calculator_parameter_list.append(parameters.type)

    # Check to see if the user entered a value for the payment parameter and also check to see if it is positive.
    # If the user did enter value and it is positive then add it to the calculator_parameter list.
    # If the user did enter a value and it is not positive then print the error message and exit the code.
    if parameters.payment is not None:
        if float(parameters.payment) > 0:
            calculator_parameter_list.append(float(parameters.payment))
        else:
            print("Incorrect parameters.")
            exit()

    # Check to see if the user entered a value for the principal parameter and also check to see if it is positive.
    # If the user did enter value and it is positive then add it to the calculator_parameter list.
    # If the user did enter a value and it is not positive then print the error message and exit the code.
    if parameters.principal is not None:
        if float(parameters.principal) > 0:
            calculator_parameter_list.append(float(parameters.principal))
        else:
            print("Incorrect parameters.")
            exit()

    # Check to see if the user entered a value for the periods parameter and also check to see if it is positive.
    # If the user did enter value and it is positive then add it to the calculator_parameter list.
    # If the user did enter a value and it is not positive then print the error message and exit the code.
    if parameters.periods is not None:
        if float(parameters.periods) > 0:
            calculator_parameter_list.append(float(parameters.periods))
        else:
            print("Incorrect parameters.")
            exit()

    # Check to see if the user entered a value for the pinterest parameter and also check to see if it is positive.
    # If the user did enter value and it is positive then add it to the calculator_parameter list.
    # If the user did enter a value and it is not positive then print the error message and exit the code.
    if parameters.interest is not None:
        if float(parameters.interest) > 0:
            calculator_parameter_list.append(float(parameters.interest))
        else:
            print("Incorrect parameters.")
            exit()

    # Only 4 parameters are needed to perform any given calculation. Therefore if the list of parameters is not 4
    # print the error message and exit the code.
    if len(calculator_parameter_list) != 4:
        print("Incorrect parameters.")


check_calculator_parameters_for_error(calculator_parameters)


# Setup a function that will calculate differenciated loan monthly payments as well of as the overpayment (if there
# is one).
# Parameters needed for calculation are: interest, periods, and principal.
def differenciated_payments_loan_calculation():
    interest = float(calculator_parameters.interest)
    periods = float(calculator_parameters.periods)
    principal = float(calculator_parameters.principal)
    differenciated_payment_total_list = []

    nominal_interest_rate = interest / (12 * 100)
    m = 1

    while m <= periods:
        differenciated_payment = math.ceil(
            (principal / periods) + (nominal_interest_rate * (principal - (principal * (m - 1) / periods)))
        )

        print(f'Month {m}: payment is {differenciated_payment}')
        m += 1

        differenciated_payment_total_list.append(differenciated_payment)

    differenciated_payment_total = sum(differenciated_payment_total_list)

    overpayment = int(differenciated_payment_total - principal)

    print(f' \nOverpayment = {overpayment}')


# Setup a function that will calculate the monthly payment of an annuity type loan.
# Parameters needed for calculation are: interest, periods, and principal.
def annuity_monthly_payment_calculation():
    interest = float(calculator_parameters.interest)
    periods = float(calculator_parameters.periods)
    principal = float(calculator_parameters.principal)

    nominal_interest_rate = interest / (12 * 100)

    payment = math.ceil(
        principal * (nominal_interest_rate * (math.pow((1 + nominal_interest_rate), periods)
                                              / (math.pow((1 + nominal_interest_rate), periods) - 1)))
    )

    print(f'Your monthly payment = {payment}!')
    overpayment = int(payment * periods - principal)
    print(f'Overpayment = {overpayment}')

# Setup a function that will calculate the principal of an annuity loan.
# Parameters needed for calculation are: interest, periods, and payment.
def annuity_loan_principal_calculation():
    interest = float(calculator_parameters.interest)
    periods = float(calculator_parameters.periods)
    payment = float(calculator_parameters.payment)

    nominal_interest_rate = interest / (12 * 100)

    principal = math.floor(
        payment / ((nominal_interest_rate * (math.pow((1 + nominal_interest_rate), periods)
                                             / (math.pow((1 + nominal_interest_rate), periods) - 1))))
    )

    print(f'Your loan principal = {principal}!')
    overpayment = int(payment * periods - principal)
    print(f'Overpayment = {overpayment}')

# Setup a function that will calculate the periods of an annuity loan.
# Parameters needed for calculation are: interest, payment, and principal.
def annuity_periods_calculation():
    interest = float(calculator_parameters.interest)
    payment = float(calculator_parameters.payment)
    principal = float(calculator_parameters.principal)

    nominal_interest_rate = interest / (12 * 100)

    periods = math.ceil(
        math.log((payment / (payment - (nominal_interest_rate * principal))), (1 + nominal_interest_rate))
    )

    number_of_years_remaining = periods // 12
    number_of_months_remaining = periods % 12

    if number_of_months_remaining > 0:
        print(
            f'It will take {number_of_years_remaining} years '
            f'and {number_of_months_remaining} months to repay this loan!')
        overpayment = int(payment * periods - principal)
        print(f'Overpayment = {overpayment}')

    else:
        print(f'It will take {number_of_years_remaining} years to repay this loan!')
        overpayment = int(payment * periods - principal)
        print(f'Overpayment = {overpayment}')

# Create a function to decide which loan calculation to perform based on the parameters the user inputs into the
# command line. For annuity loan calculations, calculate the parameter that the user does not input as long as the
# input parameters are valid.
def calculation_type(parameters):
    if parameters.type == 'diff':
        differenciated_payments_loan_calculation()
    elif parameters.type == 'annuity':
        if parameters.payment is None:
            annuity_monthly_payment_calculation()
        elif parameters.principal is None:
            annuity_loan_principal_calculation()
        elif parameters.periods is None:
            annuity_periods_calculation()


calculation_type(calculator_parameters)
