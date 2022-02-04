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
from os.path import exists


# Copy all lines of a csv file to an output csv file
def duplicate_data(input_file, output_file):
    data = []
    with open(input_file) as infile, open(output_file, 'w', newline='') as outfile:
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
    data = pd.read_csv(input_file, header=2)
    data.to_csv(output_file, header=False)

    print('The data from the file was copied to data_copy.csv')

    return


# Display the file title
def display_title(input_file):
    with open(input_file) as infile:
        line = next(infile)
        print(line, end='')

    return


# Diplay the title from a csv file
def display_run_date(input_file):
    with open(input_file) as infile:
        i = 0
        while (i <= 1):
            line = next(infile)

            if (i == 1):
                print(line, end='')

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

    print('Displaying graph...')

    data.plot()
    plt.show()

    return


def user_options():
    print('\nPlease choose from one of the following.\n')
    print('\t1.) Duplicate the original file.')
    print('\t2.) Copy the data from the original file.')
    print('\t3.) Display the file title.')
    print('\t4.) Display the file generation/run-date.')
    print('\t5.) Display the header row column names.')
    print('\t6.) Display data from the file as a list.')
    print('\t7.) Display the most recent five days of data.')
    print('\t8.) Display the highest number of cases on a single day.')
    print('\t9.) Display the highest ten days of cases.')
    print('\t10.) Display a summary of each month of data provided.')
    print('\t11.) Display the summary data in a graph.\n')

    option = input('Please enter which function to run. (enter number): ')

    return option


def main():
    print('Hi, welcome to lab 2.\n')
    ans = input('Would you like to run a function? (yes/no): ')

    while(ans.lower() == 'yes'):
        option = user_options()
        print()

        if (option.lower() == 'exit' or option.lower() == 'quit'):
            break

        try:
            option = int(option)
        except ValueError:
            print('That was not a valid option. Please try again.')

        if option == 1:
            if not exists('duplicate.csv'):
                duplicate_data(
                    'data_table_for_daily_case_trends__the_united_states.csv', 'duplicate.csv')
            else:
                print(
                    'The file was already duplicated into the current directory. This file already exists as \'duplicate.csv\'.')
        elif option == 2:
            if not exists('data_copy.csv'):
                copy_data(
                    'data_table_for_daily_case_trends__the_united_states.csv', 'data_copy.csv')
            else:
                print(
                    'The file was already copied into the current directory. This file already exists as \'data_copy.csv\'.')
        elif option == 3:
            display_title(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 4:
            display_run_date(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 5:
            display_col_names(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 6:
            display_data(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 7:
            display_recent(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 8:
            get_highest_cases(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 9:
            ten_highest_days(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 10:
            monthly_stats(
                'data_table_for_daily_case_trends__the_united_states.csv')
        elif option == 11:
            graph(
                'data_table_for_daily_case_trends__the_united_states.csv')

        ans = input('\nWould you like to to run another function? (yes/no): ')
        print()

    print('Thank you.')

    return


main()
