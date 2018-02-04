import pandas as pd

cdp_health_data = pd.read_csv("Food_Inspections.csv", nrows=5,
                              index_col="Inspection ID")

#original_col_names_lists = list(cdp_health_data.columns.values)
#print(original_col_names_lists)

def cdp_health_query(pandas_df, query_dict):
    """
    Intakes a query in form of a dictionary and filter the given pandas data
    frame accordingly
    Inputs:
        pandas_df: pandas DataFrame to filter
        query_dict:
    """
    for key, value in query_dict.items():
        df_filter = pandas_df[key] == value
        pandas_df = pandas_df[df_filter]

    return pandas_df
