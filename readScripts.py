from utils import *

#Pipeline function for highest selling products

def getHighestSelling():
    conn = openConnection()
    
    db = conn['contempt_databases_project']
    transaction_collection = db["Transaction"]
    
    pipeline = [
        {
            "$unwind": "$items"
        },
        {
            "$group": {
                "_id": "$items.productId",
                "totalQuantity": {"$sum": "$items.quantity"}
            }
        },
        {
            "$sort": {"totalQuantity": -1}
        },
        {
            "$limit": 1
        },
        {
            "$lookup": {
                "from": "Product",
                "localField": "_id",
                "foreignField": "productId",
                "as": "productDetails"
            }
        },
        {
            "$unwind": "$productDetails"
        },
        {
            "$project": {
                "productId": "$_id",
                "productName": "$productDetails.productName",
                "totalQuantitySold": "$totalQuantity"
            }
        }
    ]
    
    result = transaction_collection.aggregate(pipeline)
    
    print("Highest Selling Product")
    for doc in result:
        print (doc)
        
from utils import *

# Pipeline function for low-stock items
def getLowStockItems(threshold=20):
    conn = openConnection()

    db = conn["contempt_databases_project"]  # Database name
    product_collection = db["Product"]

    pipeline = [
        {
            "$match": {
                "productStock": {"$lt": threshold}
            }
        },
        {
            "$sort": {
                "productStock": 1,
                "lastUpdate": -1
            }
        },
        {
            "$lookup": {
                "from": "transaction",
                "let": {"product_id": "$productId"},
                "pipeline": [
                    {"$unwind": "$items"},
                    {"$match": {"$expr": {"$eq": ["$items.productId", "$$product_id"]}}}
                ],
                "as": "relatedTransactions"
            }
        },
        {
            "$project": {
                "productId": 1,
                "productName": 1,
                "supplier": 1,
                "productStock": 1,
                "lastUpdate": 1,
                "relatedTransactionCount": {"$size": "$relatedTransactions"}
            }
        }
    ]

    result = product_collection.aggregate(pipeline)

    print("Low-Stock Items")
    for doc in result:
        print(doc)
        
def getTopSuppliers():
    conn = openConnection()
    
    db = conn['contempt_databases_project'] # input database name here
    collection = db['Product'] # input collection name here
    
    # Pipeline function for percentage of sales of a specific product belonging to a certain product category (Gian)
    # Use case example: Head & Shoulders vis-a-vis shampoo product sales in January 2025
    
    pipeline =[
    {
        '$group': {
            '_id': '$supplier', 
            'product_supplied': {
                '$sum': 1
            }
        }
    }, {
        '$limit': 5
    }, {
        '$sort': {
            'product_supplied': -1
        }
    }, {
        '$project': {
            '_id': 0, 
            'top_supplier': '$_id', 
            'product_supplied': '$product_supplied'
        }
    }
]
    
    results = collection.aggregate(pipeline)
    
    print("Top Suppliers")
    for doc in results:
        print (doc)
    
#aggregation_3() # Output all documents of aggregation 3.

def getSalesGrowth():
    conn = openConnection()

    db = conn["contempt_databases_project"]  # Database name
    product_collection = db["Transaction"]

    pipeline =[
    {
        '$unwind': {
            'path': '$items'
        }
    }, {
        '$match': {
            'items.productId': 16
        }
    }, {
        '$group': {
            '_id': '$transactionDate', 
            'totalSales': {
                '$sum': '$totalPrice'
            }
        }
    },
    {
        '$sort':{
            '_id':1
        }
    }, {
        '$project': {
            '_id': 0, 
            'Product_sold_when': '$_id', 
            'totalSales': 1
        }
    }
]
    # Execute the aggregation pipeline
    results = product_collection.aggregate(pipeline)
    print("Sales Growth")
    print("Sales Growth Points")
    for doc in results:
        print (doc)