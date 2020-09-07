import boto3


try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('users')

	table.delete_item(
	    Key={
	        'username': 'janedoe',
	        'first_name': 'Jane'
	    }
	)
except Exception as ex:
	print(ex)
	exit(0)