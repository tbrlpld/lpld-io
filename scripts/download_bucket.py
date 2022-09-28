import pathlib

import boto3  # type: ignore
import dotenv

settings = dotenv.dotenv_values(".env")
bucket_name = settings.get("AWS_STORAGE_BUCKET_NAME", "")

if not bucket_name:
    print("No bucket name defined.")
    exit(1)

target_directory = pathlib.Path("/data") / bucket_name
target_directory.mkdir(exist_ok=True)

session = boto3.session.Session()
client = session.client(
    "s3",
    region_name=settings["AWS_S3_REGION_NAME"],
    endpoint_url=settings["AWS_S3_ENDPOINT_URL"],
    aws_access_key_id=settings["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=settings["AWS_SECRET_ACCESS_KEY"],
)

response = client.list_objects(Bucket=bucket_name)
for obj in response["Contents"]:
    filepath = obj["Key"]
    local_filepath = target_directory / filepath

    # Create sub-directories if necessary
    local_filepath.parent.mkdir(exist_ok=True)

    print(f"Downloading: { filepath }\nTo: { local_filepath }\n")
    client.download_file(
        bucket_name,
        filepath,
        str(local_filepath),
    )
