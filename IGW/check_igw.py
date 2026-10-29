
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

response = ec2.describe_internet_gateways(
    Filters=[
        {
            "Name": "attachment.vpc-id",
            "Values": [vpc_id]
        }
    ]
)

gateways = response["InternetGateways"]

if gateways:
    for gateway in gateways:
        print("Internet Gateway ID:", gateway["InternetGatewayId"])
        print("Attachments:", gateway["Attachments"])
        print("Tags:", gateway.get("Tags", []))
else:
    print("No Internet Gateway attached to this VPC.")
