import ollama
from agents.real_numbers import RealNumbersAgent

class StudentAgent:
    """The Student learns from axioms and the Real Numbers teacher, seeking new Diophantine invariances."""
    
    def __init__(self):
        self.real_teacher = RealNumbersAgent()
    
    def learn_and_explore(self, question: str):
        """Student learns from teacher and pushes for new invariances."""
        teacher_insight = self.real_teacher.construct_reals(question)
        
        prompt = f"""You are the Student.
You have learned from the ZFC axiom agents and the Real Numbers teacher.

Teacher insight: {teacher_insight}

Now, as the Student, seek new Diophantine invariances.
Ask questions, propose conjectures, and explore boundaries.

Question: {question}"""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {
            "role": "student",
            "teacher_insight": teacher_insight,
            "student_exploration": response['message']['content']
        }
