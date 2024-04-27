import pandas as pd

class DataPreprocessing():
    def column_rename(self, df):
        ## Convert columns names into more human understandable format
        df.columns = ['client_id','bank_id','account_id','transaction_id','transaction_date','transaction_description','amount','category','merchant']
        return df

    def null_replace(self, df):
        ## Replace null value with 'unknown'
        df.fillna('unknown', inplace=True)
        return df
    
    def datetime_format(self, df):
        ## Convert date to datetime format
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], dayfirst=True)
        return df

