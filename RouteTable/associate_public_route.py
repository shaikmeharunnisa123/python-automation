import boto3
ec2 = boto3.client("ec2",region_name = "ap-south-2")

route_table_id = "rtb-0f031e5e502bdb143"
public_subnet_id = "subnet-061967c796b938910"

response =  ec2.associate_route_table(
    RouteTableId = route_table_id,
    SubnetId = public_subnet_id
)

print("Public route table associated successfully!")
print("Association ID : ", response["AssociationId"])


