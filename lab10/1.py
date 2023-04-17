import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postrgres",
    password = "Samad2003",
    port = 5432
)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY, 
    name VARCHAR(255), 
    age INT, 
    gender CHAR
);
""")

conn.commit()

cur.close()
conn.close()