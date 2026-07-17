import ollama

class ChoiceAgent:
    """Embodies ZFC Axiom of Choice: Every family of non-empty sets has a choice function."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Choice:
"For any collection of non-empty sets, there exists a choice function that selects one element from each set."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this choice principle (existence of selectors without explicit construction)."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "choice", "response": response['message']['content']}
