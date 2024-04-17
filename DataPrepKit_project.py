# import the Packages
import pandas as pd
import numpy as np


def ReadData(data):
    try:
        # specify the function that will read the file
        File_Format = data.split('.')[-1]
        read = getattr(pd,('read_'+ File_Format))
        df = read(data)
        return df

    # handling the expected Errors
    except FileNotFoundError:
        print('file not found: please enter a valid path to the file')
    except AttributeError:
        print(f"Unsupported file format:{data.split('.')[-1]}")
    except Exception as e:
        print(f"An Error occurred: {e}")


def DataSummary(data):
    # Display the first 5 rows in the data
    print("The First 5 rows in the data".center(50),end='\n\n')
    print(data.head(5),end='\n\n\n\n')
    # Display the first 5 rows in the data
    print("The Last 5 rows in the data".center(50),end='\n\n')

    # Display Some general information about the data
    print(data.tail(5),end='\n\n\n\n')
    print('Some general information about the data'.center(50),end='\n\n')
    print(data.info(),end='\n\n\n\n')

    # Display a Statistical description of the data
    print('Statistical description of the data'.center(50), end='\n\n')
    print(data.describe())



def DataClean(data):
    print('Handing missing values Strategy depends on the Data so this function offers some strategy for you to choose one')
    df_clean = data.copy()
    # extract the columns with missing values and the number of the None values
    columns = data.isna().sum()
    columns_with_None = [(i, columns[i]) for i in columns.index if columns[i] > 0]

    if len(columns_with_None) != 0:
        print("These are the columns that have Missing values")
        print(columns_with_None)
        print('DataClean function offers two strategies to handle Missing values of numeric or categorical data')
        print('Numeric: 1- Delete None values\n         2- Replace None values with Mean or median or Mode')
        print('categorical: 1- Delete None values\n             2- Replace None values with the Mode')


        # Ask the use about the strategies
        try:
            for col in columns_with_None:
                column, strategy = input('Please! Enter the column and strategy "example: column,strategy"\n>>> ').lower().split(',')
                column = column.strip()
                strategy = strategy.strip()
                if strategy == 'delete':
                    df_clean.drop(columns=column,inplace=True)
                elif strategy == 'mean':
                    mean = df_clean[column].mean()
                    df_clean = df_clean[column].fillna(mean,inplace=True)
                elif strategy == 'median':
                    median = df_clean[column].median()
                    df_clean = df_clean[column].fillna(median,inplace=True)
                else:
                    mode = df_clean[column].mode()
                    df_clean = df_clean[column].fillna(mode,inplace=True)
                return df_clean
        except:
            print('please! Enter a valide column name and strategy as given in the example "column,strategy"')


    else:
        print("There is no Missing values")



if __name__ == '__main__':
    print("Welcome to the DataPrepKit")
    file = input('Enter the file path\n>>> ')
    # Reading the data file
    df = ReadData(file)

    # the summary of the data
    summary = input("Do you want to display the summary of the data").lower().strip()
    if summary == 'yes':
        DataSummary(df)

    clean = input("Do you want to Missing values of the data").lower().strip()
    if clean == 'yes':
        df_clean = DataClean(df)

    encode = input("Do you want to Encode the categorical columns of the data").lower().strip()
    if encode == 'yes':
        df_encoded, encoded_columns = CategoricalDataEncoding(df)
        print(encoded_columns)
        print(df_encoded.head())
    
