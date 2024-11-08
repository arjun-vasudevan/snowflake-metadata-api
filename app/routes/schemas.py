from fastapi import APIRouter, HTTPException

from app.snowflake_connector import get_connection


router = APIRouter()

# /schemas endpoint to get the schemas of a database
@router.get("/schemas/{database_name}")
def get_schemas(database_name: str):
    try:
        with get_connection(database_name) as conn:
            cur = conn.cursor()
            cur.execute(f"SHOW SCHEMAS IN DATABASE {database_name}")
            return {"schemas": [row[1] for row in cur.fetchall()]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
