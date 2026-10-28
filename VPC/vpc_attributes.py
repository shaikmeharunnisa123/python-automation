
import boto3

ec2 = boto3.client("ec2",region_name = "ap-south-2")

vpc_id = 'vpc-057f06541a9c6d9bb'

response = ec2.modify_vpc_attribute(
    EnableDnsSupport = {
        'Value' : True,
    },
    VpcId = vpc_id,
)

print(response)

ec2.modify_vpc_attribute(
    VpcId=vpc_id,
    EnableDnsHostnames={"Value": True},
)
print("DNS hostnames enabled succesfully.")


