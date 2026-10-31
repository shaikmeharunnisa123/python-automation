import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

response = ec2.describe_key_pairs()

print("Available EC2 Key Pairs:")

for key in response["KeyPairs"]:
    print("Key Name:", key["KeyName"])
    print("Key Type:", key["KeyType"])