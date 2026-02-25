import re
from utils.job_categorization import JobsCategorization
from utils.location_processing import LocationProcessor
from utils.salary_cleaning import SalaryProcessor
from utils.skills_extraction import SkillsExtractor
# Esta clase se encarga de limpiar los datos obtenidos del scraper, eliminando duplicados, filas con valores nulos en la descripción y filas con id vacíos. Además, rellena los valores nulos en la columna de ubicación con una cadena vacía.
class DataCleaning:
    def __init__(self):
        pass
    
    # Función para limpiar los datos de los trabajos, eliminando duplicados, filas con valores nulos en la descripción y filas con id vacíos. Además, rellena los valores nulos en la columna de ubicación con una cadena vacía.
    def clean_data_jobs(self, df):
        df = df.drop_duplicates(subset=['id']) 
        df = df.dropna(subset=['description'])
        df = df.drop(df[df.id == ""].index)
        df = df.reset_index()
        df = df.drop(['index'], axis=1)
        
        df['location'] = df['location'].fillna("")
        
        # Categorizar los trabajos utilizando la clase JobsCategorization
        categorizer = JobsCategorization()
        
        df['level'] = df['title'].apply(categorizer.job_level)
        df['job_group'] = df['title'].apply(categorizer.job_group)
        df['remote'] = df.apply(categorizer.remote_jobs, axis=1)
        df['remote'] = df.apply(categorizer.check_is_remote, axis=1)
        
        locationer = LocationProcessor()
        df = locationer.city_state(df)
        
        # Limpiar los salarios utilizando la clase SalaryProcessor
        salarier = SalaryProcessor()
        df = salarier.clean_salaries(df)
        
        # Extraer habilidades utilizando la clase SkillsExtractor
        skiller = SkillsExtractor()
        df['description_clean'] = df['description']
        df['description_clean'] = df['description_clean'].apply(lambda x:re.sub(r"\\","",x) if isinstance(x,str) else x)
        
        df = skiller.extract_skills(df)
        df['experience'] = df['description_clean'].apply(skiller.extract_experience)
        df['education'] = df['skills'].apply(lambda x: skiller.extract_highest_education(x.split(", ") if isinstance(x,str) else[]))
        df = skiller.new_column_extract_skills(df,'skills')
        df = df.drop(columns=['description_clean'])
        print("skiller")
        
        
        return df 