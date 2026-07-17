import ollama

class PowerSetAgent:
    """Embodies ZFC Axiom of Power Set: For any set, there exists its power set."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Power Set:
"For any set x, there exists a set y whose elements are exactly the subsets of x."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this power set principle."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "power_set", "response": response['message']['content']}
