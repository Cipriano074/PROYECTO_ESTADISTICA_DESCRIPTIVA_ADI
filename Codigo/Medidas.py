import pandas as pd

class Medidads:

    # Cargar el archivo Excel
    ruta_archivo = 'ruta/del/archivo.xlsx'
    df = pd.read_excel(ruta_archivo, sheet_name='Datos')  # Asegúrate de ajustar el nombre de la hoja

    def media(self, columna):
        media = return columna.mean() if not columna.empty else None
    