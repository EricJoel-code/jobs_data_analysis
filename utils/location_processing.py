from config import STATES_DICT

# Este módulo define la clase LocationProcessor, que se encarga de procesar y categorizar la información de ubicación de los trabajos.
class LocationProcessor:
    
    def __init__(self):
        self.states_dict = STATES_DICT
        
    # La función find_state busca en la ubicación proporcionada si hay alguna coincidencia con los nombres de los estados en el diccionario de estados. Si encuentra una coincidencia, devuelve el código del estado; de lo contrario, devuelve None.    
    def find_state(self, location):
        for state, code in self.states_dict.items():
            if state.lower() in location.lower():
                return code
        return None
    
    # La función parse_location toma una cadena de ubicación y la divide en partes utilizando la coma como separador. Luego, dependiendo del número de partes, intenta identificar el estado, la ciudad y el país. Si hay tres partes, asume que el formato es "Ciudad, Estado, País". Si hay dos partes, intenta determinar si una de ellas es un estado o un país. Si solo hay una parte, intenta encontrar un estado utilizando la función find_state. Finalmente, devuelve una tupla con el estado, la ciudad y el país (si están disponibles).    
    def parse_location(self, location):
        parts = [p.strip() for p in location.split(',')]
        
        if len(parts) == 3:
            return parts[1], parts[0], parts[2]
        elif len(parts) == 2:
            if 'US' in location or 'United States' in location:
                return parts[0], None, parts[1]
            else:
                return parts[1], parts[0], None
        
        state = self.find_state(location)
        return state, None, None
    
    # La función city_state toma un DataFrame que contiene una columna de ubicación y agrega nuevas columnas para la ciudad, el estado y el país. Itera sobre cada fila del DataFrame, procesa la ubicación utilizando la función parse_location y luego limpia los valores de estado y ciudad eliminando cualquier referencia a trabajos remotos. Finalmente, crea una nueva columna 'city_state' que combina la ciudad y el estado para facilitar su análisis.
    def city_state(self, df):
        
        df['city'] = None
        df['state'] = None
        df['country'] = None
        
        for idx, row in df.iterrows():
            location = row['location']
            
            if isinstance(location, str):
                df.at[idx, 'state'], df.at[idx, 'city'], df.at[idx, 'country'] = self.parse_location(location)
        
        df['state'] = df['state'].replace(['Remote',r'^Remote in', r'^Hybrid remote in'], None, regex = True)
        df['city'] = df['city'].replace(['Remote',r'^Remote in', r'^Hybrid remote in'], None, regex = True)        
        
        df['city_state'] = df['city'] + ', ' + df['state']
        
        return df