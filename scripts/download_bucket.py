import os
import pathlib

import boto3  # type: ignore

bucket_name = os.environ["AWS_STORAGE_BUCKET_NAME"]

target_directory = pathlib.Path("/data") / bucket_name
target_directory.mkdir(exist_ok=True)

session = boto3.session.Session()
client = session.client(
    "s3",
    region_name=os.environ["AWS_S3_REGION_NAME"],
    endpoint_url=os.environ["AWS_S3_ENDPOINT_URL"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

response = client.list_objects(Bucket=bucket_name)
print(response["Contents"])
for obj in response["Contents"]:
    filepath = obj["Key"]

    if filepath.endswith("/"):
        # We can ignore the directory entries we get in the response. The directories
        # get created as parents of files anyhow.
        continue

    local_filepath = target_directory / filepath

    # Create sub-directories if necessary
    local_filepath.parent.mkdir(exist_ok=True)

    print(f"Downloading: { filepath }\nTo: { local_filepath }\n")
    client.download_file(
        bucket_name,
        filepath,
        str(local_filepath),
    )
