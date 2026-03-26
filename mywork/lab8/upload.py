import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-ced5jz'
file_name = 'cloud.jpg'

with open(file_name, 'rb') as f:
    s3.put_object(
        Bucket=bucket,
        Key="public-cloud.jpg",
        Body=f,
        ACL='public-read'
    )

print("Upload complete")