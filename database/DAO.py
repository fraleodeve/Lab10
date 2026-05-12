from database.DB_connect import DBConnect
from model.confine import Confine
from model.stato import Stato

class DAO():
    @staticmethod
    def getAllConfini(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from contiguity c 
                    where c.conttype = 1 and c.`year` <= %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Confine(**row))

        cursor.close()
        conn.close()
        return result

    def getAllConfiniSenzaTipo(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from contiguity c 
                    where c.`year` <= %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Confine(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * 
                    from country"""

        cursor.execute(query)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

