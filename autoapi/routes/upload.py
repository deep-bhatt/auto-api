from fastapi import APIRouter, UploadFile
import pandas as pd

router = APIRouter()

@router.post('/upload', tags=['Dataset Upload'])
def create_upload_file(file: UploadFile):
    """
    1. inputs file
    2. inserts field names & field types in `field` table
    3. inserts field id and field values in `dataset` table
    """

    df = pd.read_csv(file.file)
    df_columns = df.columns.to_list()
    return {"fileType": file.content_type, "fileSize": file.size}
