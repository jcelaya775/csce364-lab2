"""
Jorge Celaya
NCC CSCE 364; Spring 2022
Lab #2; celaya_jorge_lab2.py

Code Summary:
"""

from calendar import month
from time import strftime
import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime as dt


# Copy all lines of a csv file to an output csv file
def duplicate_data(input_file, output_file):
    data = []
    with open(input_file) as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, delimiter=',')

        for row in reader:
            writer.writerow(row)
            data.append(row)

    print('File was duplicated to duplicate.csv')

    return data


# Copy only the rows from a csv file that
# contain data to an output file
def copy_data(input_file, output_file):
    data = pd.read_csv(input_file, skiprows=2)
    data.to_csv(output_file, header=False)

    print('The data from the file was copied to data_copy.csv')

    return


# Display the file title
def display_title(input_file):
    with open(input_file) as infile:
        print(str(next(infile)).strip())

    return


# Diplay the title from a csv file
def display_run_date(input_file):
    with open(input_file) as infile:
        i = 0
        while (i <= 1):
            line = next(infile)

            if (i == 1):
                print(line)

            i += 1

    return


# Display row column names from a csv file as a list
def display_col_names(input_file):
    with open(input_file) as infile:
        i = 0
        while(i <= 2):
            line = next(infile)

            if (i == 2):
                # print list of all columns in header row
                print([col.strip() for col in line.split(',')])

            i += 1

    return


# Display the data from a csv file as a list of lists
def display_data(input_file):
    data = pd.read_csv(input_file, header=2)
    print(data.values)


def display_recent(input_file):
    print('Five Most Recent Cases:\n')
    data = pd.read_csv(input_file, header=2)
    print(data.head()[['New Cases', 'Date']])

    return


# Display the max numbers of cases on any given day from a csv file
def get_highest_cases(input_file):
    data = pd.read_csv(input_file, header=2)
    print(data['New Cases'].max())

    return


# Display the highest ten days of cases (date and cases)
def ten_highest_days(input_file):
    data = pd.read_csv(input_file, header=2)

    print('Highest Ten Days of Cases:\n')
    print(data.sort_values(by='New Cases', ascending=False)
          [0:9][['Date', 'New Cases']].to_string(index=False))


# Extract and display a summary of each month of data provided.
# Create a nicely formatted display that shows the month name,
# the total cases for the month, and the average daily cases for that month.
def monthly_stats(input_file):
    data = pd.read_csv(input_file, header=2)
    # data = data.rename(columns={'Date': 'Month'})
    data.index = pd.to_datetime(
        data['Date'])

    print(data.groupby(by=[data.index.month]).describe())
    # print(df.style.format({'Date': lambda t: t.strftime('%b')}))

    return


def graph(input_file):
    data = pd.read_csv(input_file, header=2)
    data.plot()
    plt.show()

    return


def user_options():
    print('Please choose from one of the following.\n')
    print('\t1.) Duplicate the original file, save it into the project directory.')
    print('\t2.) Copy the data from the original data (data is all rows except rows 1,2,3) into the project directory.')
    print('\t3.) Extract and display the file title (first row of data).')
    print('\t4.) Extract and display the file generation/run-date (second row of data).')
    print('\t5.) Extract and display the row column names, as a list (third row of data).')
    print('\t6.) Extract and display data from csv file as a list of lists (each row is a list).')
    print('\t7.) Extract and display the most recent five days of data (date and cases reported).')
    print('\t8.) Extract and display the highest number of cases on a single day (date and cases).')
    print('\t9.) Extract and display the highest ten days of cases (date and cases) .')
    print('\t10.) Display a summary of each month of data provided.')
    print('\t11.) Display summary data in a graph.\n')
    print('Please enter which function to run. (enter number): ', end='')

    ans = 0

    try:
        ans = int(input())
    except ValueError:
        print('That was not a valid option. Please try again.\n')
        user_options()

    return ans


def main():
    print('Hi, welcome to lab 2.\n')
    ans = input('Would you like to run a function? (yes/no): ')
    duplicated = False

    while(ans.lower() == 'yes'):
        print()
        option = user_options()
        print()

        if option == 1:
            if not duplicated:
                duplicate_data(
                    'data_table_for_daily_case_trends__the_united_states.csv', 'duplicate.csv')
                duplicated = True
            else:
                print(
                    'You have already duplicated this file into the current directory. This file already exists.')
        elif option == 2:
            copy_data(
                'data_table_for_daily_case_trends__the_united_states.csv', 'data_copy.csv')
        elif option == 3:
            display_title(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 4:
            display_col_names(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 5:
            display_data(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 6:
            display_recent(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 7:
            get_highest_cases(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 8:
            ten_highest_days(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 9:
            monthly_stats(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 10:
            ten_highest_days(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 11:
            ten_highest_days(
                'data_table_for_daily_case_trends__the_united_states.csv')

        ans = input('\nWould you like to to run another function? (yes/no): ')

    print('\nThank you.')

    return


main()
