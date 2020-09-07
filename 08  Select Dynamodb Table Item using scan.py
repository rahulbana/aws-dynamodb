from boto3.dynamodb.conditions import Key, Attr
import boto3
from pprint import pprint 

try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('users')

	response = table.scan(
	    FilterExpression=Attr('age').lt(27)
	)
	response = response['Items']

	print("Row count: ", len(response))
	print("All Items")
	pprint(response)

except Exception as ex:
	print(ex)
	exit(0)