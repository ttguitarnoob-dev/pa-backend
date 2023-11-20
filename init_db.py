
import psycopg2


data = [
    {
        "back_sides_wood": "Canadian Walnut",
        "construction": "Constructed using standard guitar making tools",
        "date_added": "Sat, 04 Nov 2023 00:00:00 GMT",
        "description": "this guitar was built to be a guitar.  It was successfully made as a guitar",
        "id": 1,
        "name": "Guitar numero one1",
        "neck_wood": "Ebony colored ebony",
        "shape": "Grand Dreadnaught",
        "top_wood": "Bohemian Spruce",
        "photos": ["https://gallagherguitar.com/wp-content/uploads/2022/08/IMG_1849-scaled.jpg", "https://cdn.mos.cms.futurecdn.net/qDEs6xt2aX5eDtiLFTFYm7-1200-80.jpg"]
    },
    {
        "back_sides_wood": "Pine shavings held together by glue",
        "construction": "Constructed using a screwdriver and a box cutter",
        "date_added": "Sat, 04 Nov 2023 00:00:00 GMT",
        "description": "this guitar was built for a child prodigy in western montezuma.",
        "id": 2,
        "name": "Guitar numero notone1",
        "neck_wood": "Ebony colored spruce",
        "shape": "Slightly unimpressive Auditorium",
        "top_wood": "Home Depot Plywood",
        "photos": ["https://www.cortguitars.com/_DATA/editor/2203/dbf796aa2576a284e4f3063ac9fa7fdb_1647839581_0505.jpg", "https://3.bp.blogspot.com/-hCj1ENOhrjQ/TzycGGkwCvI/AAAAAAAABbM/GMAiX4x9yqs/s1600/sitting.JPG"]
    },
]

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
            (data[0]["name"],
             data[0]['description'],
             data[0]['neck_wood'],
             data[0]['top_wood'],
             data[0]['shape'],
             data[0]['back_sides_wood'],
             data[0]['construction'],
             data[0]['photos']
             )
            )

cur.execute('INSERT INTO guitars (name, description, neck_wood, top_wood, shape, back_sides_wood, construction, photos)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (data[1]["name"],
             data[1]['description'],
             data[1]['neck_wood'],
             data[1]['top_wood'],
             data[1]['shape'],
             data[1]['back_sides_wood'],
             data[1]['construction'],
             data[1]['photos']
             )
            )

# cur.execute('INSERT INTO guitars (name, description, neck_wood, top_wood, shape, back_sides_wood, construction, photos)'
#             'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
#             ('Guitar numero one1',
#              'this guitar was built to be a guitar.  It was successfully made as a guitar',
#              'Ebony colored ebony',
#              'Bohemian Spruce',
#              'Grand Dreadnaught',
#              'Canadian Walnut',
#              'Constructed using standard guitar making tools',
#              ["https://cdn.shopify.com/s/files/1/0550/6737/products/BERKELEY-LIVE-ANGLED-RIGHT.jpg", "https://www.native-instruments.com/typo3temp/pics/img-welcome-hero-picked-acoustic-welcome-47c4eec96d4d847293f871cafc7cad2f-m@2x.jpg"]
#              )
#             )

# cur.execute('INSERT INTO guitars (name, description, neck_wood, top_wood, shape, back_sides_wood, construction, photos)'
#             'VALUES (%s, %s, %s, %s, %s, %s, %s)',
#             ('Guitar numero notone1',
#              'this guitar was built for a child prodigy in western montezuma.',
#              'Ebony colored spruce',
#              'Home Depot Plywood',
#              'Slightly unimpressive Auditorium',
#              'Pine shavings held together by glue',
#              'Constructed using a screwdriver and a box cutter',
#              ["https://3.bp.blogspot.com/-hCj1ENOhrjQ/TzycGGkwCvI/AAAAAAAABbM/GMAiX4x9yqs/s1600/sitting.JPG"]
#              )
#             )



conn.commit()

cur.close()
conn.close()