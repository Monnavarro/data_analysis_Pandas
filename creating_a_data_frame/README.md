# Module Overview

### Reading data from a csv file
In most cases, we’ll read data from a file. The most commonly used file 
formats are csv, excel, parquet, and json. In this course, we’ll use csv 
files. The pandas read_csv function creates a DataFrame from a csv file. 
Panda provides several other functions for reading data in files with 
different formats, such as read_json, read_parquet, read_excel, and so on.

### Using usecols parameter#
There are several other parameters of the read_csv function. For instance, 
we have the option to read only some of the columns from the csv file.

### Create a DataFrame

Although we mostly read data from an external file, Pandas also allows
for creating your own DataFrame.

