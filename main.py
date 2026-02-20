import pandas as pd
import sqlite3
from utils.scraper import JobScraper
from utils.data_cleaning import DataCleaning

def main():
    '''searches = ["data analyst", "data scientist", "python developer"]
    sites = ["indeed"]
    results = 1000
    old = 1000
    country = "USA"
    
    scraper = JobScraper()
    df = scraper.scraper_jobs(searches, sites, results, old, country)
    
    con = sqlite3.connect('jobs.db')
    df.to_sql('jobs_raw_table', con, if_exists='append', index=False)
    
    df.to_csv('jobs_raw_table.csv')'''
    
    conn = sqlite3.connect('jobs.db')
    query = "SELECT * FROM jobs_raw_table"
    df = pd.read_sql_query(query, conn)
    
    datacleaner = DataCleaning()
    
    df_processed = datacleaner.clean_data_jobs(df)
    
    df_processed.to_sql('jobs_cleaned_table', conn, if_exists = 'replace', index=False)
    
    conn.close()
    
if __name__ == "__main__":
    main()