import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

dr = True
cidr = '10.10.10.0/24'

output = client.create_vpc(
    CidrBlock=cidr,
    InstanceTenancy='default'
)

print output
