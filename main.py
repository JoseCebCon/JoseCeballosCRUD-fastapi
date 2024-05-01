from fastapi import FastAPI, HTTPException
from db.db import client
from controllers.libroCRUD import router as usuarios_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

#app.add_middleware{
    
#}

app.include_router(usuarios_router, tags=["libros"], prefix="/libros")
# MongoDB connection URL
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()



