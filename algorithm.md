# Algorithm Document
Tasks:

Task 1- create a function to read data from file into a table or list of lists 9 
(use function from class)
Task 2- update the table by adding one element at each row to hold the profit 
(take table using the three rows find profit)
Task 3- writing each row using comma separated values on to another file, 
write the new table onto output file
Task 4- row in table:
            budget 
    row.append(profit)
combine into one list, one string, with commas, by using for loop and plus sign 
create one function that gives a row and combines that row into a string and returns it


1. when writing covert everything in the list to a string
2. if it is a digit apply str
3. if .isdigit use str
4. for an item in row:
   5.   str = ''
   6. if item.isdigit:
      6. line = str(item) +',
   7. line = item + 
   8. file_data.write(line) 






- Function 1
- Name: read_file_to_table
- Purpose: making file into a list of lists
- Parameters: possibly
- Return: table
- Algorithm:
    - set table variable equal to read the movie file


- Function 2
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


- Function 3 
- Name: updated_display_of_table
- Purpose: reorganizing the table with commas and making everything into a string
- Parameters:
- Return: a table of strings separated with commas
- Algorithm:
- if the variable is a digit turn into string
- set line equal to empty string 
- for item in row:
  - if item.isdigit():
  - set line equal to str(item plus ',')
  - else
  - write line 
  - 









