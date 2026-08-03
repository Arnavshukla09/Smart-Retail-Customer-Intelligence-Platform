from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import vision, nlp, chatbot, analytics

app = FastAPI(title="Smart Retail & Customer Intelligence Platform API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(vision.router)
app.include_router(nlp.router)
app.include_router(chatbot.router)
app.include_router(analytics.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Retail API Gateway"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
