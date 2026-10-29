
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

response = ec2.describe_subnets(
    Filters=[
        {"Name": "vpc-id", "Values": [vpc_id]},
        {"Name": "cidr-block", "Values": ["10.0.1.0/24"]}
    ]
)

subnets = response["Subnets"]

if not subnets:
    print("Public subnet not found.")
else:
    subnet_id = subnets[0]["SubnetId"]

    ec2.create_tags(
        Resources=[subnet_id],
        Tags=[
            {"Key": "Name", "Value": "Python-Public-Subnet"},
            {"Key": "Project", "Value": "Boto3-Networking"},
            {"Key": "Type", "Value": "Public"}
        ]
    )

    print("Public subnet tagged successfully:", subnet_id)
