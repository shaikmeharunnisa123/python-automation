

import boto3

# Connect to EC2 in your AWS region
ec2 = boto3.client("ec2", region_name="ap-south-2")

vpc_id = "vpc-057f06541a9c6d9bb"

# 1. Check VPC DNS settings
vpc = ec2.describe_vpcs(
    VpcIds=[vpc_id]
)

print("\n--- VPC DETAILS ---")

for item in vpc["Vpcs"]:
    print("VPC ID:", item["VpcId"])
    print("CIDR:", item["CidrBlock"])
    print("DNS Support:", item["IsDefault"] if False else "Check below")

dns = ec2.describe_vpc_attribute(
    VpcId=vpc_id,
    Attribute="enableDnsSupport"
)

print("DNS Resolution Enabled:", dns["EnableDnsSupport"]["Value"])

# 2. Check subnets
print("\n--- SUBNET DETAILS ---")

subnets = ec2.describe_subnets(
    Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
)

for subnet in subnets["Subnets"]:
    print(
        "Subnet:", subnet["SubnetId"],
        "| CIDR:", subnet["CidrBlock"],
        "| Public IP Mapping:", subnet["MapPublicIpOnLaunch"]
    )

# 3. Check route tables
print("\n--- ROUTE TABLE DETAILS ---")

route_tables = ec2.describe_route_tables(
    Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
)

for table in route_tables["RouteTables"]:
    print("\nRoute Table:", table["RouteTableId"])

    for route in table["Routes"]:
        print(
            "Destination:", route.get("DestinationCidrBlock"),
            "| Gateway:", route.get("GatewayId"),
            "| State:", route.get("State")
        )

    for association in table["Associations"]:
        print("Main Route Table:", association.get("Main", False))

# 4. Check Internet Gateway
print("\n--- INTERNET GATEWAY ---")

igws = ec2.describe_internet_gateways(
    Filters=[{"Name": "attachment.vpc-id", "Values": [vpc_id]}]
)

for igw in igws["InternetGateways"]:
    print("Internet Gateway:", igw["InternetGatewayId"])
    print("Attached VPC:", vpc_id)

print("\nNetwork verification completed!")