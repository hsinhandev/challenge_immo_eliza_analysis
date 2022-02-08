import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

properties_data = pd.read_csv('raw_dataset_dropPrice_str.csv')

def convert_price_from_string_to_float(df):
    # convert columns dtypes
    # Convert 'price' string type values to int/float type
    df.price = properties_data_copy.price.astype(float)
    # return df.price

    # remove 'apartment block' sub-type
def remove_apartment_block(df):
    df.drop(data[data['property sub-type'] == 'APARTMENT_BLOCK'].index, inplace = True)   
    # return df

    # remove duplicates
def drop_duplicate_rows(df):
    # choice of rows to decide which properties are duplicates
    df.drop_duplicates(subset=['Immoweb ID'], keep=False)
    return df

    # transfer property sub-type
def transfer_property_subtype(df)    
    pd.get_dummies(df_duplicates_removed, columns=["property sub-type"])
    # return df

    # transfer terrace & terrace surface
    
    # transfer property type
    # transfer furnished
    # transfer postcode
    # transfer kitchen type
    # transfer building condition
    # transfer garden and garden surface
    # tenement building ????


