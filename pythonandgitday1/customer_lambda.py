def lambda_handler(event, context):
    customer_name = event["customer_name"]
    customer_age= event["customer_age"]

    return {
        'statusCode': 200,
        'body': f'Hello {customer_name}, you are {customer_age}!'
    }

event = { 
        
        "customer_name": "Ann Reshma",
        "customer_age": 25,
        
    }

result = lambda_handler(event,None)
print(result)
