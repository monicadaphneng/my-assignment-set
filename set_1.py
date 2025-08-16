'''Programming Set 1

This assignment will familiarize you with Python's basics.
'''
import math

def savings(gross_pay, tax_rate, expenses):
    """
    Find out how much money is left after paying taxes and expenses.

    Parameters: 
        gross_pay (int): total salary for one pay period
        tax_rate (float): tax rate between 0 and 1
        expenses (int): money spent on expenses

    Returns:
        int: money left over
    """
    after_tax = math.floor(gross_pay * (1 - tax_rate))
    remaining = after_tax - expenses
    return remaining


def material_waste(total_material, material_units, num_jobs, job_consumption):
    """
    Find out how much material is left after doing several jobs.

    Parameters:
        total_material (int): starting material
        material_units (str): unit of measurement (like "kg", "L")
        num_jobs (int): number of jobs
        job_consumption (int): material used per job

    Returns:
        str: leftover material with units (e.g. "10kg")
    """
    consumed = num_jobs * job_consumption
    waste = total_material - consumed
    return str(waste) + material_units


def interest(principal, rate, periods):
    """
    Compute the final value of money with simple interest.

    Parameters:
        principal (int): initial amount of money
        rate (float): interest rate per period (between 0 and 1)
        periods (int): number of periods

    Returns:
        int: final amount after interest, rounded down
    """
    final_value = principal + (principal * rate * periods)
    return math.floor(final_value)