import ollama
from agents.real_numbers import RealNumbersAgent
from agents.memory import AgentMemory

class StudentAgent:
    def __init__(self):
        self.real_teacher = RealNumbersAgent()
        self.memory = AgentMemory()
    
    def learn_and_explore(self, question: str):
        teacher_insight = self.real_teacher.construct_reals(question)
        self.memory.add_run("RealNumbersAgent", question, str(teacher_insight))
        
        prompt = f"""You are the Student. Previous explorations: {self.memory.history[-5:]}  # recent history
        
You have learned from the ZFC axiom agents and the Real Numbers teacher.

Teacher insight: {teacher_insight}

Now, as the Student, seek new Diophantine invariances.
Ask questions, propose conjectures, and explore boundaries.

Question: {question}"""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        self.memory.add_run("StudentAgent", question, response['message']['content'])
        
        return {
            "role": "student",
            "teacher_insight": teacher_insight,
            "student_exploration": response['message']['content']
        }
