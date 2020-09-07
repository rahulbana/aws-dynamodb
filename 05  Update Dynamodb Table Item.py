import boto3


try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('users')

	table.update_item(
	    Key={
	        'username': 'aravsingh',
	        'first_name': 'Arav'
	    },
	    UpdateExpression='SET age = :val1',
	    ExpressionAttributeValues={
	        ':val1': 26
	    }
	)
except Exception as ex:
	print(ex)
	exit(0)