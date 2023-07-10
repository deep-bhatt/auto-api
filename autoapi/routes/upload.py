from fastapi import APIRouter, UploadFile
from autoapi.services import upload
import pandas as pd

router = APIRouter()

@router.post('/upload', tags=['Dataset Upload'])
async def create_upload_file(file: UploadFile):
    """
    1. inputs a CSV file
    2. inserts field names & field types in `field` table
    3. inserts field id and field values in `dataset` table
    """

    df = pd.read_csv(file.file)
    upload.insert_field(df)
    upload.insert_dataset(df)

    return { "status": True, "message": "dataset created" }
