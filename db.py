import sqlite3



def fetch_data():
    conn = sqlite3.connect('test.db')

    mouse_query = """
                SELECT
                    a.*, b.*
                FROM
                    SnpAll a, SnpPattern b
                WHERE
                    a.SpeciesId = %s AND
                    a.Id = b.SnpId
                ORDER BY a.Position
            """ % (1)
    
    cursor = conn.execute(mouse_query)

    json_data = {}
    for row in cursor:
        pass
        #put rows in json data

    conn.close()