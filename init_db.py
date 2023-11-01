
import psycopg2

conn = psycopg2.connect(
    host="10.24.24.218",
    database = "paguitars",
    user= "postgres",
    password= "Bungfodder123"
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS guitars;')
cur.execute('CREATE TABLE guitars (id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'wood_type varchar (50) NOT NULL,'
                                 'cost integer NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO guitars (name, wood, cost)'
            'VALUES (%s, %s, %s)',
            ('Guitar numero one1',
             'Canadian walnut',
             4200)
            )

cur.execute('INSERT INTO guitars (name, wood, cost)'
            'VALUES (%s, %s, %s)',
            ('Guitar numero two2',
             'Correllian walnut',
             99999999)
            )



conn.commit()

cur.close()
conn.close()