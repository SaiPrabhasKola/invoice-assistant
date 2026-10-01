from fastapi import FastAPI

app = FastAPI(title="InvoiceAssistant")

@app.get("/")
def root():
    return {"message":"Invoice Assistant is running"}

