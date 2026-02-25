import pandas as pd

# Estamos cargando el archivo Excel que contiene la información de los niveles de trabajo y sus perfiles asociados. Luego, convertimos esta información en un diccionario para facilitar su uso en la categorización de trabajos.
job_level_df = pd.read_excel('master_data/profile.xlsx')
JOB_LEVEL_DICT = job_level_df.set_index('Value')['Profile'].to_dict()

# De manera similar, estamos cargando otro archivo Excel que contiene información sobre los grupos de trabajo y sus categorías asociadas. También convertimos esta información en un diccionario para su uso en la categorización de trabajos.
job_group_df = pd.read_excel('master_data/categories.xlsx')
JOB_GROUP_DICT = job_group_df.set_index('keyword')['category'].to_dict()

# Finalmente, definimos una lista de palabras clave que se utilizarán para identificar trabajos remotos en la función de categorización de trabajos.
REMOTE_KEYWORDS = ['remote', 'hybrid', 'on site']

states_df = pd.read_excel('master_data/states.xlsx')
STATES_DICT = states_df.set_index('State')['Code'].to_dict()

# Definimos un diccionario que contiene factores de conversión para diferentes intervalos de tiempo. Esto se utilizará para convertir salarios a una base anual, facilitando la comparación entre diferentes ofertas de trabajo que pueden tener salarios expresados en diferentes intervalos (por ejemplo, mensual, semanal, diario, etc.).
INTERVAL_FACTORS = {'yearly':1, 'monthly':12, 'weekly':49, 'daily':230, 'hourly':1840}

# Cargamos un archivo Excel que contiene información sobre habilidades y sus grupos asociados. Convertimos esta información en un diccionario para facilitar la extracción de habilidades de las descripciones de los trabajos.
skills_df = pd.read_excel('master_data/skills.xlsx')
SKILLS_DICT = skills_df.set_index('Skills')['Group'].to_dict()

# Definimos un diccionario que asigna una prioridad numérica a diferentes niveles de educación. Esto se utilizará para determinar el nivel de educación más alto mencionado en las habilidades extraídas de las descripciones de los trabajos.
EDUCATION_PRIORITY = {"None":0, "Bachelor":1, "Master":2, "MBA":3, "Phd":4}

# Definimos un diccionario que contiene categorías de habilidades, como lenguajes de programación e idiomas. Esto se utilizará para categorizar las habilidades extraídas de las descripciones de los trabajos.
CATEGORIES = {
    'programming_languages': {"Python", "Java", "C++", "JavaScript", "R", "SQL", "Go", "Ruby", "PHP", "Rust", "C#", "DAX", "VBA", "ABAP", "HTML", "CSS", "Julia", "Swift"},
    'languages':{"English", "Spanish", "French", "German", "Chinese", "Japanese", "Portuguese", "Russian", "Arabic", "Hindi"}
}

# Definimos listas de frases que se utilizarán para identificar y eliminar menciones de edad y experiencia en las descripciones de los trabajos. Esto es importante para evitar confusiones al extraer la experiencia requerida para el trabajo, ya que a menudo las descripciones pueden mencionar requisitos de edad o experiencia en la empresa que no están relacionados con la experiencia laboral requerida para el puesto.
AGE_PHRASES = ["Yearly","Adolescence (13 to 17 years)","years!","last 20 years","years in a row","years in age","Must be 18 years", "years-old","years old","years of age","yrs of age","years or older", "years or over","years and older","yrs or older","yrs. or older","or older"]

COMPANY_PHRASES = ["designs up to","For more than **","For more than","Minimum age requirement is","For over","for over","provider with more than","celebrating", "In over","We are","with over","has over","company experience","years in business","years of success","in operation for","founded"]