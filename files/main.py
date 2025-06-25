import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sklearn
import datetime
from pathlib import Path


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


def etl(dataframe, time_col, sort_by):
    try:
        if type(dataframe) != pd.DataFrame:
            return TypeError("Please, use a valid DataFrame.")
        dataframe = dataframe.sort_values(by=sort_by)
#        dataframe = dataframe.to_timestamp()

        return dataframe



    except Exception as e:
        print(f"Something bad as occurred: {e}")

df = import_df(df_path = f'{'databases/weather_data.csv'}', op = 'r', type_of = 'csv')
df = etl(df, 'Location', ['Location', 'Date_Time'])

print(df)