"""
Jorge Celaya
NCC CSCE 364; Spring 2022
Lab #2; celaya_jorge_lab2.py

Code Summary:
"""

from time import strftime
import pandas as pd
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

    return data


# Copy only the rows from a csv file that
# contain data to an output file
def copy_data(input_file, output_file):
    data = pd.read_csv(input_file, skiprows=2)
    data.to_csv(output_file, header=False)

    return


# Diplay the title from a csv file
def display_title(input_file):
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


def by_month(input_file):
    data = pd.read_csv(input_file, header=2)
    # data = data.rename(columns={'Date': 'Month'})
    data.index = pd.to_datetime(
        data['Date'])

    df = data.groupby(by=[data.index.month]).describe()
    print(df.style.format({'Date': lambda t: t.strftime('%b')}))


def main():
    # implement menu for functions here w/ try-catch blocks
    # data = duplicate_data(
    #     'data_table_for_daily_case_trends__the_united_states.csv', 'data.csv')
    by_month(
        'data_table_for_daily_case_trends__the_united_states.csv')

    return


main()
