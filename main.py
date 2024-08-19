import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

def create_database_and_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyData CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
    cursor.execute("USE CompanyData")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EmployeePerformance (
            id INT AUTO_INCREMENT PRIMARY KEY,
            employee_id INT,
            department VARCHAR(255),
            performance_score DECIMAL(5,2),
            years_with_company INT,
            salary DECIMAL(10,2)
        ) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
    """)

    conn.commit()
    cursor.close()
    conn.close()

def populate_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CompanyData",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    cursor = conn.cursor()

    data = pd.read_csv('datos_mockaroo.csv')
    for _, row in data.iterrows():
        cursor.execute("""
            INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
            VALUES (%s, %s, %s, %s, %s)
        """, (row['employee_id'], row['department'], row['performance_score'], row['years_with_company'], row['salary']))

    conn.commit()
    cursor.close()
    conn.close()

def analyze_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CompanyData",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )

    query = "SELECT * FROM EmployeePerformance"
    df = pd.read_sql(query, conn)

    # Estadísticas por departamento
    stats = df.groupby('department').agg({
        'performance_score': ['mean', 'median', 'std'],
        'salary': ['mean', 'median', 'std'],
        'employee_id': 'count'
    })

    # Correlaciones
    correlation_years_perf = df['years_with_company'].corr(df['performance_score'])
    correlation_salary_perf = df['salary'].corr(df['performance_score'])

    conn.close()

    print("Estadísticas por departamento:")
    print(stats)
    print("\nCorrelación entre años en la empresa y performance_score:", correlation_years_perf)
    print("Correlación entre salario y performance_score:", correlation_salary_perf)

def visualize_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="CompanyData",
        charset='utf8mb4',
        collation='utf8mb4_general_ci'
    )
    df = pd.read_sql("SELECT * FROM EmployeePerformance", conn)

    # Histograma del performance_score por departamento
    departments = df['department'].unique()
    for department in departments:
        df_dept = df[df['department'] == department]
        plt.hist(df_dept['performance_score'], bins=10, alpha=0.5, label=department)
    
    plt.title('Histograma de Performance Score por Departamento')
    plt.xlabel('Performance Score')
    plt.ylabel('Frecuencia')
    plt.legend(loc='upper right')
    plt.show()

    # Gráfico de dispersión years_with_company vs. performance_score
    plt.scatter(df['years_with_company'], df['performance_score'])
    plt.title('Years with Company vs. Performance Score')
    plt.xlabel('Years with Company')
    plt.ylabel('Performance Score')
    plt.show()

    # Gráfico de dispersión salary vs. performance_score
    plt.scatter(df['salary'], df['performance_score'])
    plt.title('Salary vs. Performance Score')
    plt.xlabel('Salary')
    plt.ylabel('Performance Score')
    plt.show()

    conn.close()

if __name__ == "__main__":
    create_database_and_table()
    populate_table()
    analyze_data()
    visualize_data()

