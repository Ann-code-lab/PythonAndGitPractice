customer_name = "Ann Reshma"
customer_age = 25
customer_id = "C001"
customer_transactions = [100, 200, 300, 400, 50000]
customer_transactions.append(50757)

print("Customer Name:", customer_name)
print("Customer Age:", customer_age)
print("Customer ID:", customer_id)
print("Number of Transactions:", len(customer_transactions))
print("Total Transaction Amount:", sum(customer_transactions))
print("No:of Transcations:",len(customer_transactions))
print("Fisrst Transcation Amount:", customer_transactions[0])
print ("Second Transaction Amount:", customer_transactions[1])
print("Last Transaction Amount:", customer_transactions[-1])
print("SecondLast Transaction Amount:", customer_transactions[-2])

