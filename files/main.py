#############################################
# Author: Filipy da Silva Furtado           #
# Computer Science also is a form of art!   #
#############################################


#Import library's
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sklearn
from datetime import datetime
from pathlib import Path


#Import the dataframe to process in the script.
def import_df(df_path, op, type_of):
    try:
        if type(df_path) != str or type(op) != str or type(type_of) != str:
            raise TypeError("Verify the type of parameters, they have to be str type.")

        elif op != 'r':
            raise ValueError("You can use only the read mode. i.e 'r'")

        else:
            if type_of == 'csv':
                with open(Path(df_path), f'{op}') as file:
                    dataframe = pd.read_csv(file)
                    return dataframe

    except Exception as e:
        print(f"Something goes wrong: {e}")


#Measure the avarage of the items in the dataframe. Sort by need's to be a list.
def mean_values(dataframe, time_col, sort_by):
    try:
        if type(dataframe) != pd.DataFrame or type(time_col) != str or type(sort_by) != list:
            return TypeError("Please, use a valid parameter type.")
        format_datetime = lambda x: datetime.date(x)
        dataframe = dataframe.sort_values(by=sort_by)
        dataframe[time_col] = pd.to_datetime(dataframe[time_col])
        dataframe[time_col] = dataframe[time_col].apply(format_datetime)
        dataframe = dataframe.groupby([sort_by[0], time_col]).mean()
        return dataframe

    except Exception as e:
        print(f'Something bad occurred on measuring the average of the items: {e}')


#def correlation(x):
#    if type(x) != pd.DataFrame:
#        return ValueError('Please, use a dataframe as parameter')


#if __name__ == '__main__':
    #df = import_df(df_path = f'{'databases/weather_data.csv'}', op = 'r', type_of = 'csv')
    #df = mean_values(dataframe = df, time_col = 'Date_Time', sort_by = ['Location', 'Date_Time'])

