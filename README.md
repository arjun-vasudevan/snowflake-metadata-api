# Snowflake Metadata API - Arjun Vasudevan


## API Endpoints

### 1. **List All Schemas in a Database**

- **Endpoint**: `/api/schemas/{database_name}`
- **Method**: `GET`
- **Description**: Returns a list of schemas in the specified database.

### 2. **List All Tables in a Schema**

- **Endpoint**: `/api/tables/{database_name}/{schema_name}`
- **Method**: `GET`
- **Description**: Returns a list of tables within the specified schema.

### 3. **List All Columns in a Table**

- **Endpoint**: `/api/columns/{database_name}/{schema_name}/{table_name}`
- **Method**: `GET`
- **Description**: Returns a list of columns in the specified table, including their name, type, and description.

### 4. **Get Summary Statistics for a Table**

- **Endpoint**: `/api/summary/{database_name}/{schema_name}/{table_name}`
- **Method**: `GET`
- **Description**: Returns summary statistics for each column in the specified table:
  - **Numeric columns**: Non-null count, mean, min, and max.
  - **Non-numeric columns**: Non-null count and unique count.

---

## Setup and Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/yourusername/snowflake-metadata-api.git
cd snowflake-metadata-api
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the API Server**:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- The API will be accessible at `http://localhost:8000`
- Swagger spec can be viewed at `http://localhost:8000/docs`

4. **Access the API**:

By visiting the following URLs in your browser, you can access the API endpoints:
- List All Schemas: `http://localhost:8000/api/schemas/{database_name}`
- List All Tables: `http://localhost:8000/api/tables/{database_name}/{schema_name}`
- List All Columns: `http://localhost:8000/api/columns/{database_name}/{schema_name}/{table_name}`
- Get Summary Statistics: `http://localhost:8000/api/summary/{database_name}/{schema_name}/{table_name}`

Using `curl`:
```bash
curl http://localhost:8000/api/schemas/{database_name}
curl http://localhost:8000/api/tables/{database_name}/{schema_name}
curl http://localhost:8000/api/columns/{database_name}/{schema_name}/{table_name}
curl http://localhost:8000/api/summary/{database_name}/{schema_name}/{table_name}
```
