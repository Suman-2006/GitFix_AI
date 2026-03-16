from fastapi import FastAPI

app = FastAPI()


@app.post("/webhook")
def github_webhook(payload: dict):

    print("Webhook received")

    return {"status": "ok"}