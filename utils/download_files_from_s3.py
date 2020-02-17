import os
from typing import List

import boto3
from botocore.exceptions import ClientError


def download_files_from_s3(file_names: List[str], path_on_s3: str, bucket: str, path_to_save: str) -> (
        List[str]):
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    try:
        s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        for file_name in file_names:
            with open(os.path.join(path_to_save, file_name), 'wb') as wf:
                print(f'Downloading {file_name}...')
                s3.download_fileobj(bucket, path_on_s3 + file_name, wf)
        return list(map(lambda f: os.path.join(path_to_save, f), file_names))

    except ClientError as e:
        print(e)
        return []
