from fastapi import APIRouter, UploadFile
from autoapi.core.database import DatabaseConnection
from autoapi.services import upload
from autoapi.services import common
import pandas as pd

router = APIRouter()

@router.post('/upload', tags=['Dataset Upload'])
async def create_upload_file(file: UploadFile):
    """
    1. inputs a CSV file
    2. inserts field names & field types in `field` table
    3. inserts field id and field values in `dataset` table
    4. makes APIs for selecting the data.
    """

    df = pd.read_csv(file.file)
    upload.insert_field(df)
    upload.insert_dataset(df)

    # now I need to make APIs
    # steps:

    return { "status": True, "message": "dataset & apis are now created" }
