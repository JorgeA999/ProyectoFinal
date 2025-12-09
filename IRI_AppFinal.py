import pandas as pd
import pickle
import matplotlib.pyplot as plt
from utils.preprocesar import procesar_perfil


MODEL = '../Modelo/modelo_iri.pkl'
model = pickle.load(open(MODEL, 'rb'))


def predecir(path_csv):
df = procesar_perfil(path_csv)
feats = {
'pend_prom': df['pendiente'].mean(),
'rug_mean': df['abs_diff'].mean(),
'var_cota': df['cota_m'].var()
}
X = pd.DataFrame([feats])
iri = model.predict(X)[0]


# Graficas
plt.figure()
plt.plot(df['cota_m'].values)
plt.title('Perfil longitudinal (m)')
plt.xlabel('Muestra')
plt.ylabel('Cota (m)')
plt.grid(True)
plt.show()


print('IRI predicho (m/m):', iri)
return iri


if __name__ == '__main__':
import sys
if len(sys.argv) < 2:
print('Uso: python app.py DatosBrutos/archivo.csv')
else:
predecir(sys.argv[1])