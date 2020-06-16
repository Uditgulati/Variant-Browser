import mysql.connector
from mysql.connector import Error



def fetch_data(limit=100):
    connection = mysql.connector.connect(host='localhost',
                                        database='db_webqtl',
                                        user='webqtlout',
                                        password='webqtlout')

    mouse_query = """
                    SELECT
                        a.*, b.*
                    FROM
                        SnpAll a, SnpPattern b
                    WHERE
                        a.SpeciesId = %s AND
                        a.Id = b.SnpId
                    ORDER BY a.Position
                    LIMIT %s
                """ % (1, limit)

    query = """
        SELECT * FROM SnpAll
        LIMIT %s
        """ % (limit)


    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    print("Total number of rows is: ", cursor.rowcount)

    query_data = []

    for row in records:
        curr_data = {
            "Id": str(row[0]),
            "SpeciesId": str(row[1]),
            "SnpName": str(row[2]),
            "Chromosome": str(row[4]),
            "Position": str(row[5]),
            "Position_2016": str(row[6]),
            "Alleles": str(row[7]),
            "Source": str(row[8])
        }
        query_data.append(curr_data)

    if connection.is_connected():
        connection.close()
        cursor.close()
    
    return query_data