import pprint

import boto3

client = boto3.client('ec2',
		aws_access_key_id='c543fa29eeaf4894a1078ec0860baefd',
                aws_secret_access_key='d2246a2235ca40ffa7fbf817ae1108ba',
                region_name='RegionOne',
		endpoint_url='http://192.168.122.75:8788')

output = client.describe_instances()

output = output.get("Reservations")[0].get("Instances")[0]
result = {}
result['PrivateIp'] = output.get("PrivateIpAddress")
result['PublicIp'] = output.get("PublicIpAddress")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)

"""
Result:

{   u'Reservations': [   {   u'Groups': [],
                             u'Instances': [   {   u'AmiLaunchIndex': 0,
                                                   u'ImageId': 'ami-2624df94',
                                                   u'InstanceId': 'i-a9c95d89',
                                                   u'InstanceType': 'm1.tiny',
                                                   u'KernelId': 'aki-512bee3f',
                                                   u'KeyName': '',
                                                   u'LaunchTime': datetime.datetime(2016, 11, 25, 8, 59, 17, tzinfo=tzutc()),
                                                   u'NetworkInterfaces': [   {   u'Attachment': {   u'AttachTime': datetime.datetime(2016, 11, 25, 8, 59, 50, 941180, tzinfo=tzutc()),
                                                                                                    u'AttachmentId': 'eni-attach-fe61dbd0',
                                                                                                    u'DeleteOnTermination': True,
                                                                                                    u'DeviceIndex': 0,
                                                                                                    u'Status': 'attached'},
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                                    u'GroupName': 'default'}],
                                                                                 u'MacAddress': 'fa:16:3e:7b:b3:08',
                                                                                 u'NetworkInterfaceId': 'eni-fe61dbd0',
                                                                                 u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                                                                                 u'PrivateIpAddress': '12.13.1.4',
                                                                                 u'PrivateIpAddresses': [   {   u'Primary': True,
                                                                                                                u'PrivateIpAddress': '12.13.1.4'}],
                                                                                 u'SourceDestCheck': True,
                                                                                 u'Status': 'in-use',
                                                                                 u'SubnetId': 'subnet-ac04352a',
                                                                                 u'VpcId': 'vpc-287f7839'}],
                                                   u'Placement': {   u'AvailabilityZone': 'nova'},
                                                   u'PrivateDnsName': 'r-5au4r1t5-0',
                                                   u'PrivateIpAddress': '12.13.1.4',
                                                   u'PublicDnsName': '',
                                                   u'RamdiskId': 'ari-b7e05ed6',
                                                   u'RootDeviceName': '/dev/vda',
                                                   u'RootDeviceType': 'instance-store',
                                                   u'SecurityGroups': [   {   u'GroupId': 'sg-287f7839',
                                                                              u'GroupName': 'default'}],
                                                   u'SourceDestCheck': True,
                                                   u'State': {   u'Code': 16,
                                                                 u'Name': 'running'},
                                                   u'SubnetId': 'subnet-ac04352a',
                                                   u'VpcId': 'vpc-287f7839'}],
                             u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                             u'ReservationId': 'r-5au4r1t5'},
                         {   u'Groups': [],
                             u'Instances': [   {   u'AmiLaunchIndex': 0,
                                                   u'ImageId': 'ami-2624df94',
                                                   u'InstanceId': 'i-2471e9c4',
                                                   u'InstanceType': 'm1.tiny',
                                                   u'KernelId': 'aki-512bee3f',
                                                   u'KeyName': '',
                                                   u'LaunchTime': datetime.datetime(2016, 11, 25, 9, 0, 5, tzinfo=tzutc()),
                                                   u'NetworkInterfaces': [   {   u'Attachment': {   u'AttachTime': datetime.datetime(2016, 11, 25, 9, 0, 8, 78767, tzinfo=tzutc()),
                                                                                                    u'AttachmentId': 'eni-attach-cf04c068',
                                                                                                    u'DeleteOnTermination': True,
                                                                                                    u'DeviceIndex': 0,
                                                                                                    u'Status': 'attached'},
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                                    u'GroupName': 'default'}],
                                                                                 u'MacAddress': 'fa:16:3e:52:4e:15',
                                                                                 u'NetworkInterfaceId': 'eni-cf04c068',
                                                                                 u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                                                   u'ImageId': 'ami-2624df94',
                                                   u'InstanceId': 'i-a1c11cd0',
                                                   u'InstanceType': 'm1.tiny',
                                                   u'KernelId': 'aki-512bee3f',
                                                   u'KeyName': '',
                                                   u'LaunchTime': datetime.datetime(2016, 11, 25, 9, 11, 40, tzinfo=tzutc()),
                                                   u'NetworkInterfaces': [   {   u'Attachment': {   u'AttachTime': datetime.datetime(2016, 11, 25, 9, 11, 41, 311296, tzinfo=tzutc()),
                                                                                                    u'AttachmentId': 'eni-attach-af85f409',
                                                                                                    u'DeleteOnTermination': True,
                                                                                                    u'DeviceIndex': 0,
                                                                                                    u'Status': 'attached'},
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                                    u'GroupName': 'default'}],
                                                                                 u'MacAddress': 'fa:16:3e:86:52:4c',
                                                                                 u'NetworkInterfaceId': 'eni-af85f409',
                                                                                 u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                                                                                 u'PrivateIpAddress': '12.13.1.8',
                                                                                 u'PrivateIpAddresses': [   {   u'Primary': True,
                                                                                                                u'PrivateIpAddress': '12.13.1.8'}],
                                                                                 u'SourceDestCheck': True,
                                                                                 u'Status': 'in-use',
                                                                                 u'SubnetId': 'subnet-ac04352a',
                                                                                 u'VpcId': 'vpc-287f7839'}],
                                                   u'Placement': {   u'AvailabilityZone': ''},
                                                   u'PrivateDnsName': 'r-c02fvv4o-0',
                                                   u'PrivateIpAddress': '12.13.1.8',
                                                   u'PublicDnsName': '',
                                                   u'RamdiskId': 'ari-b7e05ed6',
                                                   u'SecurityGroups': [   {   u'GroupId': 'sg-287f7839',
                                                                              u'GroupName': 'default'}],
                                                   u'SourceDestCheck': True,
                                                   u'State': {   u'Code': 0,
                                                                 u'Name': 'error'},
                                                   u'SubnetId': 'subnet-ac04352a',
                                                   u'VpcId': 'vpc-287f7839'}],
                             u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                             u'ReservationId': 'r-c02fvv4o'},
                         {   u'Groups': [],
                             u'Instances': [   {   u'AmiLaunchIndex': 0,
                                                   u'ImageId': 'ami-2624df94',
                                                   u'InstanceId': 'i-0eeb0714',
                                                   u'InstanceType': 'm1.tiny',
                                                   u'KernelId': 'aki-512bee3f',
                                                   u'KeyName': '',
                                                   u'LaunchTime': datetime.datetime(2016, 11, 25, 8, 59, 49, tzinfo=tzutc()),
                                                   u'NetworkInterfaces': [   {   u'Attachment': {   u'AttachTime': datetime.datetime(2016, 11, 25, 8, 59, 52, 196279, tzinfo=tzutc()),
                                                                                                    u'AttachmentId': 'eni-attach-e09c9847',
                                                                                                    u'DeleteOnTermination': True,
                                                                                                    u'DeviceIndex': 0,
                                                                                                    u'Status': 'attached'},
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                                    u'GroupName': 'default'}],
                                                                                 u'MacAddress': 'fa:16:3e:2e:9c:fc',
                                                                                 u'NetworkInterfaceId': 'eni-e09c9847',
                                                                                 u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                                                                                 u'PrivateIpAddress': '12.13.1.3',
                                                                                 u'PrivateIpAddresses': [   {   u'Primary': True,
                                                                                                                u'PrivateIpAddress': '12.13.1.3'}],
                                                                                 u'SourceDestCheck': True,
                                                                                 u'Status': 'in-use',
                                                                                 u'SubnetId': 'subnet-ac04352a',
                                                                                 u'VpcId': 'vpc-287f7839'}],
                                                   u'Placement': {   u'AvailabilityZone': 'nova'},
                                                   u'PrivateDnsName': 'r-k0fogw80-0',
                                                   u'PrivateIpAddress': '12.13.1.3',
                                                   u'PublicDnsName': '',
                                                   u'RamdiskId': 'ari-b7e05ed6',
                                                   u'RootDeviceName': '/dev/vda',
                                                   u'RootDeviceType': 'instance-store',
                                                   u'SecurityGroups': [   {   u'GroupId': 'sg-287f7839',
                                                                              u'GroupName': 'default'}],
                                                   u'SourceDestCheck': True,
                                                   u'State': {   u'Code': 16,
                                                                 u'Name': 'running'},
                                                   u'SubnetId': 'subnet-ac04352a',
                                                   u'VpcId': 'vpc-287f7839'}],
                             u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                             u'ReservationId': 'r-k0fogw80'},
                         {   u'Groups': [],
                             u'Instances': [   {   u'AmiLaunchIndex': 0,
                                                   u'ImageId': 'ami-2624df94',
                                                   u'InstanceId': 'i-3d49ba19',
                                                   u'InstanceType': 'm1.tiny',
                                                   u'KernelId': 'aki-512bee3f',
                                                   u'KeyName': '',
                                                   u'LaunchTime': datetime.datetime(2016, 11, 25, 9, 5, 7, tzinfo=tzutc()),
                                                   u'NetworkInterfaces': [   {   u'Attachment': {   u'AttachTime': datetime.datetime(2016, 11, 25, 9, 5, 17, 402364, tzinfo=tzutc()),
                                                                                                    u'AttachmentId': 'eni-attach-9fe76481',
                                                                                                    u'DeleteOnTermination': True,
                                                                                                    u'DeviceIndex': 0,
                                                                                                    u'Status': 'attached'},
                                                                                 u'Description': '',
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                 u'Description': '',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                 u'Groups': [   {   u'GroupId': 'sg-287f7839',
                                                                                                    u'GroupName': 'default'}],
                                                                                 u'MacAddress': 'fa:16:3e:c4:ce:76',
                                                                                 u'NetworkInterfaceId': 'eni-9fe76481',
                                                                                 u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                                                                                 u'PrivateIpAddress': '12.13.1.7',
                                                                                 u'PrivateIpAddresses': [   {   u'Primary': True,
                                                                                                                u'PrivateIpAddress': '12.13.1.7'}],
                                                                                 u'SourceDestCheck': True,
                                                                                 u'Status': 'in-use',
                                                                                 u'SubnetId': 'subnet-ac04352a',
                                                                                 u'VpcId': 'vpc-287f7839'}],
                                                   u'Placement': {   u'AvailabilityZone': ''},
                                                   u'PrivateDnsName': 'r-f9wtmt0l-0',
                                                   u'PrivateIpAddress': '12.13.1.7',
                                                   u'PublicDnsName': '',
                                                   u'RamdiskId': 'ari-b7e05ed6',
                                                   u'RootDeviceName': '/dev/vda',
                                                   u'RootDeviceType': 'instance-store',
                                                   u'SecurityGroups': [   {   u'GroupId': 'sg-287f7839',
                                                                              u'GroupName': 'default'}],
                                                   u'SourceDestCheck': True,
                                                   u'State': {   u'Code': 0,
                                                                 u'Name': 'error'},
                                                   u'SubnetId': 'subnet-ac04352a',
                                                   u'VpcId': 'vpc-287f7839'}],
                             u'OwnerId': '3b91bb4e974a4729b3596f8cebb9b559',
                             u'ReservationId': 'r-f9wtmt0l'}],
    'ResponseMetadata': {   'HTTPHeaders': {   'content-length': '16617',
                                               'content-type': 'text/xml',
                                               'date': 'Fri, 25 Nov 2016 10:49:13 GMT'},
                            'HTTPStatusCode': 200,
                            'RequestId': 'req-798f37bc-ea01-4be8-9934-b567ebabcbbb'}}

"""
