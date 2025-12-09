import pandas as pd
import os
from utils.preprocesar import procesar_perfil


DIR_CSV = 'DatosBrutos/'
DIR_IRI = 'IRI_Oficial/'
OUT = 'DatasetML/dataset_entrenamiento.csv'


rows = []
for f in os.listdir(DIR_CSV):
if not f.lower().endswith('.csv'): continue
name = os.path.splitext(f)[0]
df = procesar_perfil(os.path.join(DIR_CSV, f))


# Cargar IRI oficial (xlsx con celda D2 = IRI) o archivo txt con IRI
iri_file_xlsx = os.path.join(DIR_IRI, name + '_IRI.xlsx')
iri = None
if os.path.exists(iri_file_xlsx):
iri_df = pd.read_excel(iri_file_xlsx, header=None)
iri = float(iri_df.iat[1, 3])
else:
# buscar txt
iri_txt = os.path.join(DIR_IRI, name + '_IRI.txt')
if os.path.exists(iri_txt):
with open(iri_txt) as fh:
iri = float(fh.read().strip())


rows.append({
'tramo': name,
'pend_prom': df['pendiente'].mean(),
'rug_mean': df['abs_diff'].mean(),
'var_cota': df['cota_m'].var(),
'IRI_oficial': iri
})


out_df = pd.DataFrame(rows)
out_df.to_csv(OUT, index=False)
print('Dataset creado:', OUT)