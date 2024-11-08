from fastapi import APIRouter, HTTPException

from app.snowflake_connector import get_connection


router = APIRouter()

# /tables endpoint to get the tables of a schema
@router.get("/tables/{database_name}/{schema_name}")
def get_tables(database_name: str, schema_name: str):
    try:
        with get_connection(database_name) as conn:
            cur = conn.cursor()
            cur.execute(f"SHOW TABLES IN SCHEMA {database_name}.{schema_name}")
            return {"tables": [row[1] for row in cur.fetchall()]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
