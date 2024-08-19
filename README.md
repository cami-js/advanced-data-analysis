# Advanced Data Analysis

## Descripción
Este proyecto realiza análisis de datos avanzados en un conjunto de datos de rendimiento de empleados, extraídos de una base de datos MySQL y visualizados utilizando matplotlib.

## Requisitos
- Python 3.x
- MySQL
- Librerías de Python:
  - mysql-connector-python
  - pandas
  - numpy
  - matplotlib

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/advanced-data-analysis.git
    cd advanced-data-analysis
    ```

2. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configurar la base de datos MySQL. Asegurarse de que MySQL esté corriendo y que se haya configurado las credenciales en el script `main.py`.

## Uso
1. Ejecutar el script principal:
    ```bash
    python main.py
    ```

2. El script creará la base de datos, poblará la tabla `EmployeePerformance` con datos ficticios leídos del archivo `datos_mockaroo.csv`, analizará los datos y generará visualizaciones.

