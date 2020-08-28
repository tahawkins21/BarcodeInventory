import dbconnect

#Handles the barcode that was scanned, talks to the DatabaseHandler class to query and update the database
# ARGUMENTS: sessionid is required. 
#TODO: require sessionid to create barcode handler. Probably do it in a try: except in scattertext
#TODO: need to require a sessionid to instantiate
class BarcodeHandler(object):

    def __init__(self,sessionid):
        self.sessionid = sessionid
        self.db = dbconnect.DatabaseHandler()#instance of DatabaseHandler
        

    def setSession(self, newSession):
        self.sessionid = newSession

    def getSession(self):
        return self.sessionid
    # 1
    #use to check if the product exists before updating invetory or prompting to create the item in products table
    #maybe bad idea, qty passed here is passed to the other methods too .. kind of confusing. use data field?
    def checkProd(self, barcode, qty=None):
        prods = self.db.lookupProd(barcode)#lookup product and store the results
        if prods:
            print(prods)
            if qty == None:
                qty = 1
            self.updateInv(prods, barcode, qty)#if exists, update database session_products with current sessionid
        else: #if product not in database, prompt user to create the product
            print("Product not found. Do you want to add this to the database?")
            #there is a setProduct already...
            return False

    # 2
    def updateInv(self, prods, barcode, qty=None):
        #if the product is already in session_products for that id, just update the row
        sessProd = self.db.getSessProd(barcode, self.sessionid)
        if sessProd: #if the product already counted for this session
            print(sessProd)
            currQty = sessProd[0][2]#get the current quantity from the query results
            qty = qty + currQty#add the quantity scanned to the exisiting qty
            print(qty)
            self.db.updateSessProd(barcode, self.sessionid, qty)#updates the row in session_products for the new qty
        else:
            defaultQty = 1
            self.db.setSessProd(barcode, self.sessionid, defaultQty)#insert into the session_prodcuts table with default qty of 1

#test = BarcodeHandler(1)#create an instance of handler and pass a session id that it stores 
#test.checkProd('884486366245', 15)
#test.checkProd('30330',2020)

#test.db.close()

#IT WAS A MISPLACED SEMICOLON!!!! ALWAYS CHECK THE FINAL SQL!!!

##TODO: write logic for setSessProd -- also need logic  call dbconnect.setProduct() which creates a totallhy new product