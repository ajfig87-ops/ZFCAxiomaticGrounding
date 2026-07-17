import ollama

class UnionAgent:
    """Embodies ZFC Axiom of Union: For any set of sets, there exists the union."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Union:
"For any set x of sets, there exists a set y whose elements are exactly the elements of the elements of x."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this union principle."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "union", "response": response['message']['content']}
