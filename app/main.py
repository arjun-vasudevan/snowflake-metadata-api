from fastapi import FastAPI
from app.routes import schemas, tables, columns, summary

app = FastAPI()

# Include the routers from the routes directory, all starting with /api
app.include_router(schemas.router, prefix="/api")
app.include_router(tables.router, prefix="/api")
app.include_router(columns.router, prefix="/api")
app.include_router(summary.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Snowflake Metadata API is running."}

@app.get("/api")
def api():
    return {"message": "Welcome to the Snowflake Metadata API."}
