from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lock down the origins to your exact React server address
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173", #Might not need if i only use localhost to access from browser
]

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=origins,      # Only allows requests from your React app
    allow_credentials=True,     # Safely allows login cookies/sessions
    allow_methods=["*"],        # Allows standard operations (GET, POST, etc.)
    allow_headers=["*"],        # Allows standard headers
)

@app.get("/hello")
def read_root():
    # The key must be exactly "message" wrapped in a dictionary
    return {"message": "Hello there!"}


