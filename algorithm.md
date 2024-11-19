# Algorithm Document
Tasks:

1. Task 1- create a function to read data from file into a table or list of lists 9 
(use function from class)
2. Task 2- update the table by adding one element at each row to hold the profit 
(take table using the three rows find profit)
3. Task 3- writing each row using comma separated values on to another file, 
write the new table onto output file
   4. Task 4- row in table: 
   1.budget 
   -row.append(profit)
  - combine into one list, one string, with commas, by using for loop and plus sign 
   create one function that gives a row and combines that row into a string and returns it


1. Function 1
- Name: read_file_to_table
- Purpose: making file into a list of lists
- Parameters: none
- Return: table
- Algorithm:
    - set table variable equal to read the movie file


2. Function 2
- Name: update_table
- Purpose: update the file to have the profit on the end of it
- Parameters:possibly 
- Return: table with additional variable of profit added on the end of list
- Algorithm:
- for row in table:
- set budget equal to a_table[i][2]
- set worldwide equal to a_table[i][4]
- profit = wordwide - budget
- add profit to end of list using row.append(profit)


3. Function 3 
- Name: updated_display_of_table
- Purpose: reorganizing the table with commas and making everything into a string
- Parameters: update table
- Return: a table of strings separated with commas
- Algorithm:
- if the variable is a digit turn into string
- set line equal to empty string 
- for item in row:
  - if item.isdigit():
  - set line equal to str(item plus ',')
  - else
  - write line equals item plus ','
  -  output file_data.write(line)


4. Function 4
- Name: lowest_profit_movie
- Purpose: to print the movie with the lowest profit 
- Parameters: updated display of table
- Return: lowest profit movie
- Algorithm: 
- set profit equal to 999999999
- while profit is less than profit set lowest_profit equal to that number 
- output lowest_profit



5. Function 5
- Name: main
- Purpose: to call the 4 functions
- Parameters: none
- Return: list of movies with profits and lowest profit
- Algorithm:
- call read_file_to_table
- call  update_table
- call updated_display_of_table
- call lowest_profit_movie


6. call main 











