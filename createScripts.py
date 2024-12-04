from utils import *
productNames = [ 'Orange', 'Apple', 'Banana', 'Strawberry', 'Kiwi',                 #list that contains product names the function can choose from
                'Carrot', 'Lettuce', 'Tomato', 'Cabbage', 'Onion',                  #5 per productType: Fruits, Vegetables, Canned Goods, Dairy, Bath Products, Drinks
                'Corned Beef', 'Sardines', 'Spam', 'Canned Tuna', 'Baked Beans', 
                'Milk', 'Cheese', 'Butter', 'Yogurt', 'Cream', 
                'Shampoo', 'Conditioner', 'Deodorant', 'Body Wash', 'Bar Soap', 
                'Soda', 'Beer', 'Water', 'Root Beer', 'Juice']

suppliers = [ 'Supplier A', 'Supplier B', 'Supplier C', 'Supplier D', 'Supplier E',                 #list that contains suppliers the function can choose from
             'Supplier F', 'Supplier G', 'Supplier H', 'Supplier I', 'Supplier J', 'Supplier K'] 

possiblePrices = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]                   #list that contains productPrices the function can choose from

def insertProducts():                           #function to insert a set number of product documents into collection
    conn = openConnection()
    db = conn['contempt_databases_project']
    collection = db['Product']    
    ctr = 0

    while ctr < 10000:                              #number dicates how many items are added in collection(1000 = 1000 products)
        productId = ctr
        productNameIndex = randint(0,10)          #chooses random product name

        if productNameIndex in [0,1,2,3,4]:       #conditional statements to assign correct productType
            productType = 'Fruit'                 #also assigns a random supplier
            supplierIndex = randint(0,10)
        elif productNameIndex in [5,6,7,8,9]:
            productType = 'Vegetables'
            supplierIndex = randint(0,10)
        elif productNameIndex in [10,11,12,13,14]:
            productType = 'Canned Goods'
            supplierIndex = randint(0,10)
        elif productNameIndex in [15,16,17,18,19]:
            productType = 'Dairy'
            supplierIndex = randint(20,21,22,23,24)
        elif productNameIndex in [20,21,22,33,24]:
            productType = 'Hygiene'
            supplierIndex = randint(0,10)
        else:
            productType = 'Drinks'
            supplierIndex = randint(0,10)

        year = randint(2019, 2024)                  #isodate generator
        month = randint(1,12)
        
        if month in [1,3,5,7,8,10,12]:
            day = randint(1,31)
        elif month == 2:
            day = randint (1,28)
        else:
            day = randint(1,30)

        lastUpdate = datetime(year, month, day)

        finalDoc = {                                               #final product document saved in collection
            'productId': productId,
            'productName': productNames[productNameIndex],
            'productType': productType,
            'productDescription': 'PLACEHOLDER',
            'productPrice': possiblePrices[randint(0,9)],
            'supplier': suppliers[supplierIndex],
            'productStock': randint(10,50),
            'lastUpdate': lastUpdate
        }

        collection.insert_one(finalDoc)                              #adds document to collection

        ctr += 1
    
    #print(collection)

def insertTransactions():                           #function to insert transaction documents to collection
    conn = openConnection()
    db = conn['contempt_databases_project']
    transaction_collection = db['Transaction']
    product_collection = db['Product']
    
    # Fetch all products from the Product collection
    products = list(product_collection.find({}))
    if not products:
        print("No products found in the Product collection.")
        return

    ctr = 0

    while ctr < 10000:                                 #number dictates how many transaction documents are inserted to collection
        numOfItems = randint(1, 4)
        itemList = []                               #list of items purchased in transaction
        totalPrice = 0                              #totalPrice, calculated throughout the function

        while numOfItems > 0:                       #while loop to generate list of items bought in transaction
            product = choice(products)       # Select a random product
            quantity = randint(1, 5)               # Random quantity for the item
            price = product['productPrice']         # Use the product's price

            itemList.append({
                'productName': product['productName'],
                'productId' : product['productId'],
                'quantity': quantity,
                'price': price
            })

            totalPrice += price * quantity          # Update totalPrice with quantity and price
            numOfItems -= 1

        #year = randint(2023, 2024)
        year = 2024
        month = randint(1, 12)
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = randint(1, 31)
        elif month == 2:
            day = randint(1, 28)
        else:
            day = randint(1, 30)

        transactionDate = datetime(year, month, day)

        finalDoc = {
            'items': itemList,
            'totalPrice': totalPrice,
            'transactionDate': transactionDate,
            'cashierName': 'PLACEHOLDER',
        }

        transaction_collection.insert_one(finalDoc)  # Insert the transaction document into the Transaction collection

        ctr += 1
