import boto3
client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

dr = True
cidr = '11.11.11.0/24'

output = client.create_vpc(
    CidrBlock=cidr,
    InstanceTenancy='default'
)

print output

"""
Respone:

{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'req-0b7db2b4-420e-4217-9106-e8cdb4137f65', 'HTTPHeaders': {'date': 'Tue, 13 Sep 2016 09:52:24 GMT', 'content-length': '351', 'content-type': 'text/xml'}}, u'Vpc': {u'State': 'available', u'VpcId': 'vpc-5eed72c5', u'CidrBlock': '10.10.10.0/24', u'IsDefault': False, u'DhcpOptionsId': 'default'}}
"""
