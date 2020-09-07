import boto3
from pprint import pprint 

try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('users')

	response = table.scan()
	response = response['Items']

	print("Row count: ", len(response))
	print("All Items")
	pprint(response)

except Exception as ex:
	print(ex)
	exit(0)