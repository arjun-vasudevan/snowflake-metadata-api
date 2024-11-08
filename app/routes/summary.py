from fastapi import APIRouter, HTTPException

from app.routes.columns import get_columns
from app.snowflake_connector import get_connection


router = APIRouter()


# Generate a query to get summary statistics for a table depending on the column data types
def generate_query(database_name: str, schema_name: str, table_name: str):
    # Call the /columns endpoint to get the columns of the table
    columns = get_columns(database_name, schema_name, table_name)["columns"]
    statistics = []

    for column in columns:
        column_name, datatype = column["name"], column["type"]

        # Generate the appropriate SQL aggreagations based on the column data type
        if datatype.startswith(("NUMBER", "DECIMAL", "NUMERIC", "INT", "FLOAT", "DOUBLE", "REAL")):
            statistics.append(f"""
                COUNT({column_name}) AS {column_name}_non_null_count,
                AVG({column_name}) AS {column_name}_mean,
                MIN({column_name}) AS {column_name}_min,
                MAX({column_name}) AS {column_name}_max
            """)
        else:
            statistics.append(f"""
                COUNT({column_name}) AS {column_name}_non_null_count,
                COUNT(DISTINCT {column_name}) AS {column_name}_distinct_count
            """)

    # Join the statistics into a single query
    final_query = f"""
        SELECT {', '.join(statistics)}
        FROM {database_name}.{schema_name}.{table_name}
    """

    return final_query, columns


# /summary endpoint to get summary statistics for a table
@router.get("/summary/{database_name}/{schema_name}/{table_name}")
def get_summary(database_name: str, schema_name: str, table_name: str):
    final_query, columns = generate_query(database_name, schema_name, table_name)

    try:
        with get_connection(database_name) as conn:
            cur = conn.cursor()
            cur.execute(final_query)
            result = cur.fetchone()

            # Put the statistics in a list for each column
            summary_statistics = []
            col_index = 0

            for column in columns:
                column_name, datatype = column["name"], column["type"]

                # Parse the appropriate statistics based on the column data type
                if datatype.startswith(("NUMBER", "DECIMAL", "NUMERIC", "INT", "FLOAT", "DOUBLE", "REAL")):
                    summary_statistics.append({
                        "column_name": column_name,
                        "type": datatype,
                        "non_null_count": result[col_index],
                        "mean": result[col_index + 1],
                        "min": result[col_index + 2],
                        "max": result[col_index + 3]
                    })
                    col_index += 4
                else:
                    summary_statistics.append({
                        "column_name": column_name,
                        "type": datatype,
                        "non_null_count": result[col_index],
                        "distinct_count": result[col_index + 1]
                    })
                    col_index += 2

            return {"summary_statistics": summary_statistics}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
