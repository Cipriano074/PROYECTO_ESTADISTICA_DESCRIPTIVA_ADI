import os
import pandas as pd

# Cargar el archivo Excel
ruta_archivo_entrada = 'excel/Proyecto Análisis de Datos 1(1-89).xlsx'
df = pd.read_excel(ruta_archivo_entrada)


def conocer_columnas():
    # Mostrar las columnas disponibles en el archivo de entrada
    print("Columnas disponibles en el archivo de entrada:")
    print(df.columns.tolist())


def obtener_datos(columnas_a_usar):
    #Verificar si el nuevo archivo Excel ya existe
    ruta_archivo_salida = 'excel/datos.xlsx'

    if os.path.exists(ruta_archivo_salida):
        # Si el archivo existe, cargar el contenido existente
        df_existente = pd.read_excel(ruta_archivo_salida)
        
        # Concatenar el contenido existente con el nuevo DataFrame
        nuevo_df = pd.concat([df_existente, df[columnas_a_usar]])
    else:
        # Si el archivo no existe, usar el DataFrame original
        nuevo_df = df[columnas_a_usar]

    # Guardar el nuevo DataFrame en un archivo Excel
    nuevo_df.to_excel(ruta_archivo_salida, index=False, engine='openpyxl')

    print("Nuevo archivo Excel creado o actualizado correctamente.")

__name__ = "__main__"
if __name__ == "__main__":
    conocer_columnas()
    
    # Especificar las columnas que deseas usar en el nuevo archivo
    columnas_a_usar = ['ID', 'Nombre','Edad', 'Identidad de Género\xa0', 'Carrera Principal', 
                        'Segunda Carrera', 'Subir la captura de pantalla de la categoría juegos en la aplicación de tiempo en pantalla de tu celular.\xa0']
    obtener_datos(columnas_a_usar) 