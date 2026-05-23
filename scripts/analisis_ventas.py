# -*- coding: utf-8 -*-
#TP-OE: Gestión de Ventas (Escenario B - Análisis de Ventas)
#Estudiante: Díaz Luis Santiago
#Universidad Tecnológica Nacional (UTN)
#CONTROL DE CALIDAD (QA): Auditoria de Documentación y Comentarios (correspondiente al Rol 3)
#Propósito: Script optimizado para análisis mensual de artículos tecnológicos.

import pandas as pd
import matplotlib.pyplot as plt

print("----Ejecutando Script de Análisis de Ventas----")
#Carga de datos (desde un archivo CSV)
df = pd.read_csv('datos/dataset_ventas.csv')

#Cálculo automático del monto bruto por fila de las ventas
df['sales_amount'] = df['cantidad_vendida'] * df['precio']

#Conversión de la columna 'fecha_venta' a un formato de fecha real
df['fecha'] = pd.to_datetime(df['fecha_venta'])

df['mes'] = df['fecha'].dt.to_period('M')

#---Métricas de Ventas---
ventas_totales = df['sales_amount'].sum()
print(f"Ventas Totales: ${ventas_totales:,.2f}")

#Cálculo para obtener el producto con mayor cantidad vendida
producto_mas_vendido = (df.groupby('producto')['cantidad_vendida'].sum().idxmax())
print(f"Producto más vendido: {producto_mas_vendido}")

#Agrupamos ventas por mes
ventas_mes = df.groupby('mes')['sales_amount'].sum()

print("\nVentas por Mes:")
print(ventas_mes.to_string())

#---Visualización de Datos---

#Crear figura y ejes del gráfico
fig, ax= plt.subplots(figsize=(10, 5))

#Generar gráfico de barras sobre las ventas mensuales
ventas_mes.plot(kind='bar', ax=ax, color='steelblue')

#Configurar títulos y etiquetas
ax.set_title('Evolución de ventas mensuales', fontsize=14, fontweight='bold')
ax.set_xlabel('Periodo (Mes)', fontsize=12)
ax.set_ylabel('Monto Total en Pesos ($)', fontsize=12)

#Mantener las etiquetas horizontales
plt.xticks(rotation=0)

#Ajustar márgenes automáticamente
plt.tight_layout()

#---Exportación---
#Guardar gráfico en formato PNG
plt.savefig('resultados/grafico_ventas.png', dpi=150)

print("[ÉXITO] Gráfico exportado correctamente.")
