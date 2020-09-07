from boto3.dynamodb.conditions import Key, Attr
import boto3
from pprint import pprint 

try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('users')

	scan = table.query(
						KeyConditionExpression=Key('username').eq('aravsingh')
					  )
	response = scan['Items']

	print("Row count: ", len(response))
	print("All Items")
	pprint(response)

except Exception as ex:
	print(ex)
	exit(0)