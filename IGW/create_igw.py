
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

# 1. Create an Internet Gateway
response = ec2.create_internet_gateway()

igw_id = response["InternetGateway"]["InternetGatewayId"]

print("Internet Gateway created:", igw_id)

# 2. Add tags to the Internet Gateway
ec2.create_tags(
    Resources=[igw_id],
    Tags=[
        {"Key": "Name", "Value": "Python-IGW"},
        {"Key": "Project", "Value": "Boto3-Networking"}
    ]
)

# 3. Attach the Internet Gateway to the existing VPC
ec2.attach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id
)

print("Internet Gateway attached to VPC:", vpc_id)
