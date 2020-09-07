from boto3.dynamodb.conditions import Key, Attr
import boto3
from pprint import pprint 

try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('users')
	table.delete()

except Exception as ex:
	print(ex)
	exit(0)