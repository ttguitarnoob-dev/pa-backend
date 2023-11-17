
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
                                 'description varchar (500) NOT NULL,'
                                 'neck_wood varchar (50) NOT NULL,'
                                 'top_wood varchar (50) NOT NULL,'
                                 'shape varchar (50) NOT NULL,'
                                 'back_sides_wood varchar (50) NOT NULL,'
                                 'construction varchar (150) NOT NULL,'
                                 'photos varchar[],'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO guitars (name, description, neck_wood, top_wood, shape, back_sides_wood, construction, photos)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            ('Guitar numero one1',
             'this guitar was built to be a guitar.  It was successfully made as a guitar',
             'Ebony colored ebony',
             'Bohemian Spruce',
             'Grand Dreadnaught',
             'Canadian Walnut',
             'Constructed using standard guitar making tools',
             ["https://cdn.shopify.com/s/files/1/0550/6737/products/BERKELEY-LIVE-ANGLED-RIGHT.jpg", "https://www.native-instruments.com/typo3temp/pics/img-welcome-hero-picked-acoustic-welcome-47c4eec96d4d847293f871cafc7cad2f-m@2x.jpg"]
             )
            )

cur.execute('INSERT INTO guitars (name, description, neck_wood, top_wood, shape, back_sides_wood, construction, photos)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s)',
            ('Guitar numero notone1',
             'this guitar was built for a child prodigy in western montezuma.',
             'Ebony colored spruce',
             'Home Depot Plywood',
             'Slightly unimpressive Auditorium',
             'Pine shavings held together by glue',
             'Constructed using a screwdriver and a box cutter',
             ["https://3.bp.blogspot.com/-hCj1ENOhrjQ/TzycGGkwCvI/AAAAAAAABbM/GMAiX4x9yqs/s1600/sitting.JPG"]
             )
            )



conn.commit()

cur.close()
conn.close()