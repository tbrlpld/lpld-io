import os

import boto3
import dotenv


settings = dotenv.dotenv_values(".env")

print(settings)


session = boto3.session.Session()
client = session.client(
    's3',
    region_name=settings["AWS_S3_REGION_NAME"],
    endpoint_url=settings["AWS_S3_ENDPOINT_URL"],
    aws_access_key_id=settings["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=settings["AWS_SECRET_ACCESS_KEY"],
)


response = client.list_objects(Bucket=settings["AWS_STORAGE_BUCKET_NAME"])
for obj in response["Contents"]:
    print(obj["Key"])
