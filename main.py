from fastapi import FastAPI
from agents.orchestrator import run_agent
from simulation.run import run_simulation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Aether AI OS running 🚀"}

@app.get("/run")
def run(q: str):
    return {"result": run_agent(q)}

@app.get("/world")
def world():
    return run_simulation()
