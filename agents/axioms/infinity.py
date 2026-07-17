import ollama

class InfinityAgent:
    """Embodies ZFC Axiom of Infinity: There exists an infinite set."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Infinity:
"There exists a set x that contains the empty set and is closed under the successor operation."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this inductive infinite principle."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "infinity", "response": response['message']['content']}
