# -*- coding: utf-8 -*-
# =========================================================================
# TP-OE: Gestión de Ventas (Escenario B - Análisis de Ventas)
# Estudiante: Díaz Luis Santiago
# Universidad Tecnológica Nacional (UTN)
# Propósito: Analizar datos de ventas, calcular indicadores clave y graficar 
# la evolución mensual de una pequeña empresa de artículos de tecnología.
# =========================================================================

#Importación de Librerías
#En este caso, pandas porque permite manipular y analizar datos mediante tablas
import pandas as pd

#"matplotlib.pyplot" para la creación de gráficos estadísticos.
import matplotlib.pyplot as plt

print("----Ejecutando Script de Análisis de Ventas----")

#Carga de Datos
df = pd.read_csv('datos/dataset_ventas.csv') #Lee el archivo separado por comas (CSV) y lo convierte en un DataFrame. Hago uso de una ruta relativa para que funcione la reproducción del proyecto.

#Procesamiento de los Datos
#Creamos la columna sales_amount (monto total) multiplicando las filas de las cantidades existentes por su precio.
df['sales_amount'] = df['cantidad_vendida'] * df['precio']

#pd.to_datetime() convierte la columna de texto 'fecha_venta' a un formato de fecha real (Datetime)
df['fecha'] = pd.to_datetime(df['fecha_venta'])

#.dt.to_period('M'): esto lo que hace es extraer el período mensual (Año-Mes) ignorando los días.
#Esto se va a guardar en una columna nueva llamada 'mes' para poder agrupar los datos luego.
df['mes'] = df['fecha'].dt.to_period('M')


#CÁLCULO DE LOS INDICADORES SOLICITADOS

#Ventas Totales
ventas_totales = df['sales_amount'].sum() #.sum() es un método de pandas que suma todos los valores numéricos de la columna 'sales_amount'
print(f"Ventas Totales: ${ventas_totales:,.2f}")

#Producto más vendido
producto_mas_vendido = df.groupby('producto')['cantidad_vendida'].sum().idxmax()
#.groupby('producto') agrupa las filas que tienen los nombres de los productos.
#['cantidad_vendida'].sum(): esto para sumar la cantidad total de unidades que se vendieron de cada producto.
#.idxmax(): devuelve el índice (nombre del producto) que acumuló el valor máximo en la suma.
print(f"Producto más vendido: {producto_mas_vendido}")

#Ventas por mes
#Agrupamos por la columna 'mes' creada anteriormente y sumamos los montos de 'sales_amount'.
ventas_mes = df.groupby('mes')['sales_amount'].sum()
print("\nVentas por Mes:") 
#.to_string(): va a convertir los datos a texto plano
print(ventas_mes.to_string())

#Generación del Gráfico
fig, ax = plt.subplots(figsize=(10, 5))
#plt.subplots(): inicializa la figura y los ejes fijando el tamaño en pulgadas

ventas_mes.plot(kind='bar', ax=ax, color='steelblue')
#kind='bar': para definir el tipo de gráfico (barras verticales en este caso)
#ax=ax: indica que el gráfico debe dibujarse dentro de las dimensiones configuradas arriba
#color='steelblue': aplica un color azul a las barras.

#Etiquetas y elementos (configuración visual)
ax.set_title('Evolución de ventas mensuales', fontsize=14, fontweight='bold')
#ax.set_title(): para definir el título principal del gráfico (arriba)

ax.set_xlabel('Periodo (Mes)', fontsize=12)
ax.set_ylabel('Monto Total en Pesos ($)', fontsize=12)

plt.xticks(rotation=0)
#esto para controlar la rotación de los textos en el eje X

plt.tight_layout()
#ajustar de forma automática los márgenes para que no se corten las etiquetas

#Guardado en el Repositorio
plt.savefig('resultados/grafico_ventas.png', dpi=150)
print("[ÉXITO] El script ha sido ejecutado y el gráfico se exportó a resultados/grafico_ventas.png")
#plt.savefig(): para guardar el gráfico como una imagen física en la carpeta de resultados
