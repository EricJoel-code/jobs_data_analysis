import pandas as pd

# Estamos cargando el archivo Excel que contiene la información de los niveles de trabajo y sus perfiles asociados. Luego, convertimos esta información en un diccionario para facilitar su uso en la categorización de trabajos.
job_level_df = pd.read_excel('master_data/profile.xlsx')
JOB_LEVEL_DICT = job_level_df.set_index('Value')['Profile'].to_dict()

# De manera similar, estamos cargando otro archivo Excel que contiene información sobre los grupos de trabajo y sus categorías asociadas. También convertimos esta información en un diccionario para su uso en la categorización de trabajos.
job_group_df = pd.read_excel('master_data/categories.xlsx')
JOB_GROUP_DICT = job_group_df.set_index('keyword')['category'].to_dict()

# Finalmente, definimos una lista de palabras clave que se utilizarán para identificar trabajos remotos en la función de categorización de trabajos.
REMOTE_KEYWORDS = ['remote', 'hybrid', 'on site']