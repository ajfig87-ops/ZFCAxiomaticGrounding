import json
from datetime import datetime
from pathlib import Path

class AgentMemory:
    """Persistent memory for training across runs."""
    
    def __init__(self):
        self.memory_file = Path("data/agent_memory.json")
        self.memory_file.parent.mkdir(exist_ok=True)
        self.load()
    
    def load(self):
        if self.memory_file.exists():
            with open(self.memory_file) as f:
                self.history = json.load(f)
        else:
            self.history = []
    
    def save(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.history, f, indent=2)
    
    def add_run(self, agent_name: str, input_prompt: str, output: str):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": agent_name,
            "input": input_prompt,
            "output": output
        }
        self.history.append(entry)
        self.save()
        print(f"✅ Run logged for {agent_name}")
