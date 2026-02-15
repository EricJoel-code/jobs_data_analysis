import pandas as pd
import sqlite3
from utils.scraper import JobScraper

def main():
    searches = ["data analyst", "data scientist", "python developer"]
    sites = ["indeed"]
    results = 1000
    old = 1000
    country = "USA"
    
    scraper = JobScraper()
    df = scraper.scraper_jobs(searches, sites, results, old, country)
    
    con = sqlite3.connect('jobs.db')
    df.to_sql('jobs_raw_table', con, if_exists='append', index=False)
    
    df.to_csv('jobs_raw_table.csv')
    
if __name__ == "__main__":
    main()