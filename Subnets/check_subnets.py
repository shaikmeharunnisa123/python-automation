import boto3
ec2 = boto3.client("ec2",region_name = "ap-south-2" )

vpc_id = 'vpc-057f06541a9c6d9bb'
response = ec2.describe_subnets(
    Filters = [
        {       "Name" : "vpc-id",
                "Values" : [vpc_id]
        }
    ]
        
)

Subnets = response['Subnets']

if not Subnets:
    print("No subnets found in this VPC")
else:
    print(response)