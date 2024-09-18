### Assignment 2-2: Building and Deploying the Prototype of the Triangle Model

See `main.py` for code.

To install dependencies:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run:
```sh
ollama run llama3 # Run the llama3 server
uvicorn main:app --reload # Run the FastAPI server
```
