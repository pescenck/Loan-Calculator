import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-type", "--type")
parser.add_argument("-payment", "--payment")
parser.add_argument("-principal", "--principal")
parser.add_argument("-periods", "--periods")
parser.add_argument("-interest", "--interest")

calculator_parameters = parser.parse_args()


def check_calculator_parameters_for_error(parameters):
    if parameters.type != "diff" and parameters.type != "annuity":
        print("Incorrect parameters.")
        exit()

    if parameters.type == "diff" and parameters.payment is not None:
        print("Incorrect parameters.")
        exit()

    if parameters.interest is None:
        print("Incorrect parameters.")
        exit()

    calculator_parameter_list = []

    if parameters.type is not None:
        calculator_parameter_list.append(parameters.type)

    if parameters.payment is not None:
        if float(parameters.payment) > 0:
            calculator_parameter_list.append(float(parameters.payment))
        else:
            print("Incorrect parameters.")
            exit()

    if parameters.principal is not None:
        if float(parameters.principal) > 0:
            calculator_parameter_list.append(float(parameters.principal))
        else:
            print("Incorrect parameters.")
            exit()

    if parameters.periods is not None:
        if float(parameters.periods) > 0:
            calculator_parameter_list.append(float(parameters.periods))
        else:
            print("Incorrect parameters.")
            exit()

    if parameters.interest is not None:
        if float(parameters.interest) > 0:
            calculator_parameter_list.append(float(parameters.interest))
        else:
            print("Incorrect parameters.")
            exit()

    if len(calculator_parameter_list) != 4:
        print("Incorrect parameters.")


check_calculator_parameters_for_error(calculator_parameters)


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
