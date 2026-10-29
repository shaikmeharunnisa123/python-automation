
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

response = ec2.create_subnet(
    VpcId=vpc_id,
    CidrBlock="10.0.1.0/24"
)

subnet = response["Subnet"]

print("Public subnet created successfully!")
print("Subnet ID:", subnet["SubnetId"])
print("CIDR Block:", subnet["CidrBlock"])
print("Availability Zone:", subnet["AvailabilityZone"])
print("State:", subnet["State"])