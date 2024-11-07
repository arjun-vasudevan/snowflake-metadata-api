import os
import snowflake.connector
from dotenv import load_dotenv


load_dotenv()

def get_connection():
    return snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT_IDENTIFIER'),
        role=os.getenv('SNOWFLAKE_ROLE'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE')
    )

# show all schemas
# conn = get_connection()
# cur = conn.cursor()
# cur.execute("SHOW SCHEMAS")
# for s in cur:
#     print(s)
# cur.close()
