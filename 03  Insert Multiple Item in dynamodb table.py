import boto3


try:
	# Get the service resource.
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('users')

	data = [
		{'username': 'amansingh', 'first_name': 'Aman', 'last_name': 'Singh', 'age': 22, 'account_type': 'primary_user'},
		{'username': 'priyasinha', 'first_name': 'Priya', 'last_name': 'Sinha', 'age': 28, 'account_type': 'primary_user'},
		{'username': 'aravsingh', 'first_name': 'Arav', 'last_name': 'Singh', 'age': 19, 'account_type': 'super_user'},
		{'username': 'sharmageeta', 'first_name': 'Geeta', 'last_name': 'Sharma', 'age': 26, 'account_type': 'primary_user'},
	]
	with table.batch_writer() as batch:
		for item in data:
			batch.put_item(
			   Item=item
			)

except Exception as ex:
	print(ex)
	exit(0)