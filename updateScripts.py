from utils import *

def updateProductDetails(productId, updatedFields):
    conn = openConnection()
    db = conn['contempt_databases_project']
    collection = db['Product']

    query = {'productId': productId}  # Find the specific product by ID

    update = {
        '$set': updatedFields,  # Pass updated fields as a dictionary
        '$currentDate': {'lastUpdate': True}  # Automatically update the lastUpdate field
    }

    result = collection.update_one(query, update)

    print(f"Matched {result.matched_count} document(s). Modified {result.modified_count} document(s).")
    
#Sample call
#updateProductDetails(
#    productId=3,
#    updatedFields={
#       'productName': 'Updated Banana',
#        'productDescription': 'Now available as organic bananas!'
#    }
#)

def updateProductStock(productId, quantitySold):
    conn = openConnection()
    db = conn['contempt_databases_project']
    collection = db['Product']

    query = {'productId': productId}

    update = {
        '$inc': {'productStock': -quantitySold},  # Decrease stock
        '$currentDate': {'lastUpdate': True}  # Automatically update the lastUpdate field
    }

    result = collection.update_one(query, update)

    print(f"Matched {result.matched_count} document(s). Modified {result.modified_count} document(s).")
    
#Sample call
#updateProductStock(productId=3, quantitySold=5)

def updateTransactionDetails(transactionId, updatedFields):
    conn = openConnection()
    db = conn['contempt_databases_project']
    collection = db['Transaction']

    query = {'_id': transactionId}  # Match transaction by its unique ID

    update = {
        '$set': updatedFields,
        '$currentDate': {'transactionDate': True}  # Optionally update the transactionDate
    }

    result = collection.update_one(query, update)

    print(f"Matched {result.matched_count} document(s). Modified {result.modified_count} document(s).")

#updateTransactionDetails(
#        transactionId='some_transaction_id',  # Replace with actual ObjectId
#        updatedFields={
#            'cashierName': 'John Doe',
#            'totalPrice': 1200
#        }
#    )

def batchUpdateTransactions(query, updatedFields):
    conn = openConnection()
    db = conn['contempt_databases_project']
    collection = db['Transaction']

    update = {
        '$set': updatedFields,
        '$currentDate': {'transactionDate': True}  # Optionally update the transactionDate
    }

    result = collection.update_many(query, update)

    print(f"Matched {result.matched_count} document(s). Modified {result.modified_count} document(s).")

#    batchUpdateTransactions(
#        query={'transactionDate': {'$lt': datetime(2022, 1, 1)}},
#        updatedFields={'status': 'archived'}
#    )