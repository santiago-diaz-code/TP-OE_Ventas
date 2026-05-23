#TP-OE-Escenario B: Análisis de Ventas
## Descripción del proyecto
Este proyecto corresponde al **Trabajo Práctico nro 2 de Organización Empresarial**.
El objetivo es simular un entorno profesional aplicando metodologías ágiles (**Jira**) y control de versiones (**Git/GitHub**), desarrollando un script en **Python** para el **análisis de ventas** de una pequeña empresa de artículos de tecnología.

El script 'scripts/analisis_ventas.py' procesa un dataset de ventas y genera métricas de negocio junto con gráficos estadísticos.

## Estructura del repositorio
/datos
dataset_ventas.csv
/scripts
analisis_ventas.py
/resultados
grafico_ventas.png
README.md

- **/datos** → contiene el dataset de ventas simulado.
- **/scripts** → incluye el script principal de análisis en Python.
- **/resultados** → guarda los gráficos generados automáticamente.
- **README.md** → documentación del proyecto.

## Instrucciones de ejecución
### Requisitos
- Python 3.x
- Librerías: 'pandas', 'matplotlib'

### Pasos
'''bash
# Clonar el repositorio
git clone <URL-del-repo>
cd TP-OE_Ventas

# Instalar dependencias
pip install pandas matplotlib

# Ejecutar el script
python scripts/analisis_ventas.py

El gráfico se exporta automáticamente a la carpeta /resultados.

## Metodología y Trazabilidad
Se utilizo GitFlow para organizar ramas y commits.
Cada commits está vinculado a tareas en Jira:
- SANTIAGO16-1 → Inicialización del repositorio y estructura de carpetas
- SANTIAGO16-2 → Desarrollo del script de análisis de datos
- SANTIAGO16-3 → Revisión, documentación y merge de Pull Request

## Autor y Roles
Luis Santiago Díaz
- Rol Líder (SANTIAGO16-1)
- Rol Desarrollador (SANTIAGO16-2)
- Rol QA (SANTIAGO16-3)
