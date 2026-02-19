import re

class DataCleaning:
    def __init__(self):
        pass
    
    def clean_data_jobs(self, df):
        df = df.drop_duplicates(subset=['id'])
        df = df.dropna(subset=['description'])
        df = df.drop(df[df.id == ""].index)
        df = df.reset_index()
        df = df.drop(['index'], axis=1)
        
        df['location'] = df['location'].fillna("")
        
        return df