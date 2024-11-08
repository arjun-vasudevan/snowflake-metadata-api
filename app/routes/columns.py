from fastapi import APIRouter, HTTPException

from app.snowflake_connector import get_connection


router = APIRouter()

# /columns endpoint to get the columns of a table
@router.get("/columns/{database_name}/{schema_name}/{table_name}")
def get_columns(database_name: str, schema_name: str, table_name: str):
    try:
        with get_connection(database_name) as conn:
            cur = conn.cursor()
            cur.execute(f"DESCRIBE TABLE {database_name}.{schema_name}.{table_name}")

            all_columns = [{
                "name": row[0],
                "type": row[1],
                "description": '' if row[9] is None else row[9]
            } for row in cur.fetchall()]

            return {"columns": all_columns}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
