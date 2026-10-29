
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock="10.0.2.0/24"
)

subnet = response["Subnet"]
subnet_id = subnet["SubnetId"]

print("Private subnet created successfully!")
print("Subnet ID:", subnet_id)
print("CIDR Block:", subnet["CidrBlock"])
print("Availability Zone:", subnet["AvailabilityZone"])

ec2.create_tags(
    Resources=[subnet_id],
    Tags=[
        {"Key": "Name", "Value": "Python-Private-Subnet"},
        {"Key": "Project", "Value": "Boto3-Networking"},
        {"Key": "Type", "Value": "Private"}
    ]
)

print("Private subnet tagged successfully!")
