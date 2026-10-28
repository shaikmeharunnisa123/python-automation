import boto3

ec2 = boto3.client("ec2",region_name = "ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

response = ec2.describe_route_tables(
    Filters = [
        {
            "Name" : "vpc-id",
            "Values" : [vpc_id]
        }
    ]
)

print(response)