from agents.planner import plan_task
from agents.executor import execute_task

def run_agent(user_input):
    plan = plan_task(user_input)
    result = execute_task(plan)
    return result
