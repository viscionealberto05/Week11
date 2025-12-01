from database.DB_connect import DBConnect
from model.object import Object
from model.connessione import Connessione


class DAO:
    def __init__(self):
       pass

    @staticmethod
    def readObjects():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM objects"
        cursor.execute(query)
        for row in cursor:
            oggetto = Object(row["object_id"], row["object_name"])
            result.append(oggetto)
           # result.append(Object(**row))    #fa l'unpacking del dizionario
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def readConnessioni(objects_dict):  #Riceve la idMap degli Object
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        #Nella query cerco quegli oggetti che sono stati messi in mostra con altri oggetti
        #diversi da loro stessi e devo contare quante volte sono stati esposti con altri
        #in esibizioni diverse


        query =  """SELECT eo1.object_id AS o1, eo2.object_id AS o2, COUNT(*) AS peso
                FROM exhibition_objects eo1, exhibition_objects eo2
                WHERE eo1.exhibition_id = eo2.exhibition_id
                AND eo1.object_id < eo2.object_id #escludo le coppie ribaltate
                GROUP BY eo1.object_id, eo2.object_id """
        cursor.execute(query)

        for row in cursor:
            o1 = objects_dict[row["o1"]]
            o2 = objects_dict[row["o2"]]
            peso = int(row["peso"])
            result.append(Connessione(o1, o2, peso))

        cursor.close()
        conn.close()
        return result

