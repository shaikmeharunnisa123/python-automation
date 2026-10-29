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

for table in response["RouteTables"]:
    
    is_main = False

    for association in table["Associations"]:
        if association.get("Main", False):
            is_main = True
            break

    if not is_main:
        RT_id = table["RouteTableId"]
        ec2.create_tags(
            Resources = [RT_id],
            Tags = [
                    {"Key" : "Name", "Value" : "Python-RT"},
                    {"Key" : "Project", "Value" : "Boto3-Networking"},
                ],

        )

print("Route table named successfully")
print(RT_id)
# print(response)