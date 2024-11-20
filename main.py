# Programmers: Andrew Leimbach, Theresa DeJacimo
# Course:  CS151, Zelalem Yalew
# Due Date: 11/20/24
# Lab Assignment:  Lab 10
# Problem Statement: Update movie list by calculating and adding profit
# Data In: filename
# Data Out:  Users file of choice
# Credit: Class Assignment
# Input Files: movies.csv

# Purpose: Read data
# Parameters: none
# Return: table
def read_file_to_table():
    filename = input("Enter the input file name (movies.csv): ")
    table = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split(',')  # Split line into a list
                table.append(row)
        return table
    except FileNotFoundError:
        print("File does not exist. Please try again.")
        return read_file_to_table()

# Purpose: Update file to include profit
# Parameters: table
# Return: table
def update_table(table):
    for i in range(len(table)):
        try:
            budget = int(table[i][2])
            worldwide_gross = int(table[i][4])
            profit = worldwide_gross - budget
            table[i].append(profit)  # Add profit to the row
        except (ValueError, IndexError):
            print("Skipping row due to invalid data:", table[i])
    return table

# Purpose: Reorganizing the table with comments and making everything into a string
# Parameters: Update table
# Return: none
def updated_display_of_table(table):
    output_file = input("Enter the output file name (e.g., updated_movies.csv): ")
    with open(output_file, 'w') as file:
        for row in table:
            line = ""  # Initialize an empty line for the row
            for item in row:
                if str(item).isdigit():  # Check if the string representation is a digit
                    line += str(item) + ','  # Add item as string and append comma
                else:
                    line += str(item) + ','  # Add non-digit item as string with comma
            file.write(line[:-1] + '\n')  # Remove the trailing comma and write the row

# Purpose: To print the movie with the lowest profit
# Parameters: table
# Return: none
def lowest_profit_movie(table):
    lowest_profit = 999999999  # Initialize with a large number
    lowest_profit_movie = []  # Placeholder for the movie with the lowest profit

    for i in range(len(table)):
        try:
            profit = int(table[i][-1])  # Profit is the last column
            if profit < lowest_profit:
                lowest_profit = profit
                lowest_profit_movie = table[i]
        except (ValueError, IndexError):
            print("Invalid data for row:", table[i])

    # Display the lowest profit movie
    if len(lowest_profit_movie) > 0:
        print("Movie with the lowest profit:")
        for item in lowest_profit_movie:
            print(item, end=' ')
        print()
    else:
        print("No valid data found to determine the lowest profit movie.")

# Purpose: Welcome user and run functions
# Parameters: none
# Return: none
def main():
    print("\nWelcome! This program is designed to analyze data on movies, their budgets, and their profits!")
    table = read_file_to_table()
    table = update_table(table)
    updated_display_of_table(table)
    lowest_profit_movie(table)
    print("Thank you for using this program!")

# Call the main function
main()
