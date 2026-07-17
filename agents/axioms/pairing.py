import ollama

class PairingAgent:
    """Embodies ZFC Axiom of Pairing: For any sets a and b, there exists a set {a,b}."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Pairing:
"For any two sets a and b, there exists a set whose elements are exactly a and b."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this constructive principle."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "pairing", "response": response['message']['content']}
