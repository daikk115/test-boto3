import boto3
from botocore.exceptions import ClientError

client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

try:
     output = client.allocate_address(Domain='vpc')
     print type(output)
except ClientError as exc:
    print type(exc)