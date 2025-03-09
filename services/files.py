import io
from typing import List
import uuid
import boto3
import boto3.session
from fastapi import UploadFile

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

async def get_url(file: List[UploadFile]):
    uploded_files = []
    filenames = []
    for f in file:
        file_content = await f.read()
        f.filename = str(uuid.uuid4()) + ".jpg"
        filenames.append(f.filename)
        
        s3.upload_fileobj(
            Fileobj=io.BytesIO(file_content),
            Bucket='patriot-music',
            Key=f.filename
        )
        
        uploded_files.append({"filename": f.filename, "status": "uploaded"})
        
    async def get(get_url):
        return ["https://storage.yandexcloud.net/patriot-music/" + uploded_files[f]["filename"] for f in range(len(uploded_files))]