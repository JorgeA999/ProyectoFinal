import pandas as pd
import numpy as np


def procesar_perfil(path, dx=0.15, col_cota=0):
#Lee CSV (cotas en mm), devuelve DataFrame
#con columnas en metros y features.
df = pd.read_csv(path, header=None)
df = df.iloc[:, col_cota].to_frame(name='cota_mm')
df['cota_m'] = df['cota_mm'] / 1000.0
df['dx'] = dx
df['diff'] = df['cota_m'].diff()
df['pendiente'] = df['diff'] / dx
df['abs_diff'] = df['diff'].abs()
df = df.fillna(0)
return df