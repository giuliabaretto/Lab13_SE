from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def get_cromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT cromosoma
                    FROM gene
                    WHERE cromosoma > 0 """

        cursor.execute(query)

        for row in cursor:
            result.append(row["cromosoma"])

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def get_interazioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT correlazione, G1.cromosoma as c1, G2.cromosoma as c2
                    FROM interazione I, gene G1, gene G2
                    WHERE I.id_gene1 = G1.id AND I.id_gene2 = G2.id AND G1.cromosoma <> 0 AND G2.cromosoma <> 0 AND G1.cromosoma <> G2.cromosoma"""
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result