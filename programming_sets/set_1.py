'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''
def savings(gross_pay, tax_rate, expenses):
    '''Compute Remaining Pay.

    Calculates how much money an employee keeps after taxes and expenses.

    Process:
        1. Apply the tax rate to gross pay and round down.
        2. Subtract the expenses from the after-tax amount.

    Parameters
    gross_pay: int
        Total earnings before deductions (in centavos)
    tax_rate: float
        Tax rate as a decimal (ex: 0.12 for 12%)
    expenses: int
        Expenses to be deducted (in centavos)

    Returns
    int
        Amount left after taxes and expenses
    '''
    x = int(gross_pay * (1 - tax_rate))
    x = x - expenses
    return int(x)


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Determine Material Leftover.

    Computes how much material remains after performing a number of jobs.

    Steps:
        1. Multiply number of jobs by material used per job.
        2. Subtract total used material from the total available.
        3. Return as a string with units (no space between number and unit).

    Parameters
    total_material: int
        Starting material amount
    material_units: str
        Unit of measurement (ex: "kg", "L")
    num_jobs: int
        Number of jobs performed
    job_consumption: int
        Material used per job

    Returns
    str
        Remaining material with its unit (ex: "10kg")
    '''
    x = num_jobs * job_consumption
    x = total_material - x
    return str(x) + str(material_units)


def interest(principal, rate, periods):
    '''Calculate Final Investment.

    Computes the final amount of an investment using simple interest.

    Steps:
        1. Multiply principal by rate and number of periods to get interest.
        2. Add interest to the principal.
        3. Round down to nearest whole unit.

    Parameters
    principal: int
        Initial investment amount (in centavos)
    rate: float
        Interest rate per period as a decimal (ex: 0.05 for 5%)
    periods: int
        Number of periods invested

    Returns
    int
        Final investment value after interest
    '''
    x = principal * (rate * periods)
    x = principal + x
    return int(x)
