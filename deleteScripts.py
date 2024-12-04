from utils import openConnection

def deleteProductById(productId):

    conn = openConnection()
    db = conn['contempt_databases_project']
    product_collection = db['Product']

    result = product_collection.delete_one({'productId': productId})

    if result.deleted_count > 0:
        print(f"Product with productId {productId} has been successfully deleted.")
    else:
        print(f"No product found with productId {productId}.")
    
    conn.close()


def deleteProductsByCriteria(criteria):
 
    conn = openConnection()
    db = conn['contempt_databases_project']
    product_collection = db['Product']

    result = product_collection.delete_many(criteria)

    print(f"{result.deleted_count} product(s) have been deleted based on the criteria: {criteria}.")
    
    conn.close()


def deleteTransactionById(transactionId):

    conn = openConnection()
    db = conn['contempt_databases_project']
    transaction_collection = db['Transaction']

    result = transaction_collection.delete_one({'_id': transactionId})

    if result.deleted_count > 0:
        print(f"Transaction with ID {transactionId} has been successfully deleted.")
    else:
        print(f"No transaction found with ID {transactionId}.")
    
    conn.close()


def deleteTransactionsByCriteria(criteria):

    conn = openConnection()
    db = conn['contempt_databases_project']
    transaction_collection = db['Transaction']

    result = transaction_collection.delete_many(criteria)

    print(f"{result.deleted_count} transaction(s) have been deleted based on the criteria: {criteria}.")
    
    conn.close()



    # Example calls for testing purposes:

    # Delete a single product by ID
    #deleteProductById(productId=3)

    # Delete multiple products by criteria
    #deleteProductsByCriteria(criteria={'productType': 'Fruit'})

    # Delete a single transaction by ID
    #deleteTransactionById(transactionId="63d4fa8f5d5b4c8dc3a1f76d")  # Replace with actual ObjectId

    # Delete multiple transactions by criteria
    #deleteTransactionsByCriteria(criteria={'cashierName': 'PLACEHOLDER'})
