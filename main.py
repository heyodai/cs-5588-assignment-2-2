from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import gradio as gr
import requests

app = FastAPI()


class Query(BaseModel):
    message: str


@app.post("/query/")
async def query_model(query: Query):
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": "Why is the sky blue?",
            },
        ],
    )
    return response["message"]["content"]

def chat_with_model(message):
    response = requests.post("http://localhost:8000/query/", json={"message": message})
    return response.json()["response"]


interface = gr.Interface(
    fn=chat_with_model,
    inputs="text",
    outputs="text",
    title="Chat with Model",
    description="Type a message to get a response from the model.",
)

if __name__ == "__main__":
    interface.launch()