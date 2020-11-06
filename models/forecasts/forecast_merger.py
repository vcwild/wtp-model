import pandas as pd 
import numpy as np
from os import listdir


def list_model_files(path, entity, word):
  """Lists all model files for one variable from an entity"""
  archives = listdir(path) 
  matches = [value for value in archives if word in value]
  files = ['./'+ value for value in matches if entity in value]
  return sorted(files)


def model_dataframe(path, entity, word):
  """Transforms all searched models into one dataframe"""
  arima_file, ets_file, prophet_file = list_model_files(
    path=path, 
    entity=entity, 
    word=word
  )
  arima = pd.read_csv(arima_file)
  ets = pd.read_csv(ets_file)
  prophet = pd.read_csv(prophet_file)
  
  df = pd.DataFrame()
  df['DATE'] = arima['DATE']
  df['ARIMA'] = arima.iloc[:, 1]
  df['ETS'] = ets.iloc[:, 1]
  df['PROPHET'] = prophet.iloc[:, 1]

  return df


path = './'
entities = ['p1', 'p2']
words = [
  'COLIFORMES_TERMOTOLERANTES', 
  'DQO', 
  'FÓSFORO', 
  'NITROGÊNIO', 
  'DBO', 
  'PH', 
  'SURFACTANTES', 
  'SÓLIDOS', 
  'ÓLEOS', 
  'COR_VERDADEIRA'
]

# Lists all variables from all entities, find its models and merge their predictions into dataframes
for entity in entities:
  for word in words:
    df = model_dataframe(path=path, entity=entity, word=word)
    df.to_csv(f"./dataframe/{entity}_{word}.csv", encoding='utf8', index=False)