# Snowflake Metadata API - Arjun Vasudevan

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Design Decisions](#design-decisions)
- [API Endpoints](#api-endpoints)
- [Setup and Installation](#setup-and-installation)
- [Running the API Server Locally](#running-the-api-server-locally)
- [Testing the API](#testing-the-api)

---

## Project Overview

The Snowflake Metadata API is designed to retrieve and expose metadata from Snowflake, including schemas, tables, and columns. It also provides summary statistics for each column in a specified table, adapting dynamically based on the data type.

The API includes the following endpoints:

- List all schemas in a database
- List all tables in a schema
- List all columns in a table, with details
- Get summary statistics for a table (based on column data types)

---

## Tech Stack

- **FastAPI**: FastAPI is used as the web framework for building the RESTful API, offering easy asynchronous capabilities and auto-generated API documentation.
- **Snowflake Connector**: This library is used to connect to Snowflake and run SQL queries directly.
- **Python (3.8+)**: Python programming language powers the project.
- **Pydantic**: Used for data validation and serialization.

---

## Design Decisions

1. **Single Query for Summary Statistics**: The summary endpoint uses a dynamically generated SQL query that aggregates statistics for each column type (numeric vs. non-numeric) in one go, minimizing the number of queries to Snowflake.
2. **Modular Architecture**: Each endpoint is designed in a modular fashion with separate route files, enabling maintainability and scalability.
3. **Dynamic SQL Generation**: For the summary endpoint, the SQL query is generated based on column data types fetched via `DESCRIBE TABLE`, allowing it to adapt to different table schemas automatically.

---

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
