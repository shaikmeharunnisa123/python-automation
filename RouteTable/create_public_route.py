import boto3
ec2 = boto3.client("ec2",region_name = "ap-south-2")

route_table_id = "rtb-0f031e5e502bdb143"
internet_gateway_id = "igw-0079fac1b1a6693f2"

response = ec2.create_route(
    RouteTableId = route_table_id,
    DestinationCidrBlock = "0.0.0.0/0",
    GatewayId = internet_gateway_id
)

print("Internet route created", response["Return"])