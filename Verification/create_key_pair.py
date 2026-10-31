import boto3

ec2 = boto3.client("ec2", region_name="ap-south-2")

key_name = "todo-app-key"

response = ec2.create_key_pair(
    KeyName=key_name,
    KeyType="rsa"
)

private_key = response["KeyMaterial"]

with open(f"{key_name}.pem", "w") as file:
    file.write(private_key)

print("Key Pair created successfully!")
print("Key Name:", response["KeyName"])
print("Private key saved as:", f"{key_name}.pem")