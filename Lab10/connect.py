import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    connection = psycopg2.connect(host = '127.0.0.1', database = 'suppliers', user='postgres', password='Yerdaulet_05', port='5432')
    cursor = connection.cursor()
    try:
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS Test(
                id INT PRIMARY KEY NOT NULL,
                NAME TEXT,
                SALARY INT
            ) 
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print('creted')
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    connect()
conn = psycopg2.connect("dbname=suppliers user=postgres password=Yerdaulet_05")