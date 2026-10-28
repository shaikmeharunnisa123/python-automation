
import boto3

ec2 = boto3.client("ec2",region_name = "ap-south-2")

vpc_id = 'vpc-057f06541a9c6d9bb'

response1 = ec2.describe_vpc_attribute(
    VpcId = vpc_id,
    Attribute = "enableDnsSupport",
)



response2 = ec2.describe_vpcs(VpcIds=[vpc_id])

for vpc in response2["Vpcs"]:
    print("VPC Id : ",vpc["VpcId"])
    print("CIDR Block : ",vpc["CidrBlock"])
    print("State : ",vpc["State"])
