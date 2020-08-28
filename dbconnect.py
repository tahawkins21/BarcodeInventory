import mysql.connector
from mysql.connector import cursor

#DatabaseHandler creates a connection to MySQL database and a cursor
#close it with close()
#lookupProd() to find product
#insertProd() to create a product


# TODO: Create setProduct that adss a new product to the product table
# TODO: need to create a setSession() function for new sessions && loadSessionList() that would return a list of all active sessions so we can load them on main app start
##Need to finish this and then fix what i removed in scattertext
##also TODO need to add this classes event to the kv file to test

class DatabaseHandler(object):
    def __init__(self):
        self.cnx = mysql.connector.connect(user='admin', password='Jess#0521',
                                host='127.0.0.1',
                                database='BarcodeInv')
        self.crs = self.getCursor()

    def getCursor(self):
        return self.cnx.cursor()

    def test(self):
        print(self.cnx)

    def close(self):
        self.cnx.close()

    def insertProd(self, barcode,line, tone, color ):

        sql = 'INSERT INTO products VALUES(%s,%s,%s,%s);'
        vals = (barcode,line,tone,color)
        try:
            self.crs.execute(sql,vals)
            self.cnx.commit()
            self.crs.fetchall()
        except mysql.connector.Error as err:
            print(err)
        
    #lookup product off the barcode in products table. If exists, returns rows. Exception returns false
    def lookupProd(self, barcode):
        sql = 'SELECT * FROM products WHERE barcode = ' + barcode +';'
        #vals = (barcode)
        print(sql)
        try:
            self.crs.execute(sql)
            rows = self.crs.fetchall()
            #print(rows)
            #for (barcode,line,tone,color) in self.cursor:
            #    print('{}, {}, {}, {}'.format(barcode,line,tone,color))
            #self.cnx.commit()
            return rows
        except Exception as err:
            print(err)
            return False
        
    def getSessProd(self, barcode, sessionid):
        sql = 'SELECT * FROM session_products WHERE barcode = ' + barcode +' AND sessionid = '+ str(sessionid) +';'
        #vals = (barcode)
        print(sql)
        try:
            self.crs.execute(sql)
            rows = self.crs.fetchall()
            return rows
        except mysql.connector.Error as err:
            print(err)
            return False  

    def setSessProd(self, barcode, sessionid, qty=None):
        sql = 'INSERT INTO session_products VALUES(' + str(sessionid) + ",'"+ str(barcode) + "'," +str(qty) +');'
        print(sql)
        try:
            self.crs.execute(sql)
            self.cnx.commit()
            return True
        except mysql.connector.DatabaseError as err:
            print(' in setSessProd')
            print(err)
            return False       

    def updateSessProd(self, barcode, sessionid, qty=None):
        sql = 'UPDATE session_products SET quantity =' + str(qty) + " WHERE barcode = '" + str(barcode) + "' AND sessionid = " + str(sessionid) + ';'
        print(sql)
        try:
            self.crs.execute(sql)
            self.cnx.commit()
            return True
        except mysql.connector.DatabaseError as err:
            print(' in updatesessprod')
            print(err)
            return False         

#db = DatabaseHandler()
#print(db.getSessProd('884486366245',1))
#print(db.lookupProd('884486366245'))
#db.updateSessProd('884486366245',1,1000)
#db.close()


        
