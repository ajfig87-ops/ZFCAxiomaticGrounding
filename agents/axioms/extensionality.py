import ollama

class ExtensionalityAgent:
    """Embodies ZFC Axiom of Extensionality: Sets are equal iff they have the same elements."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Extensionality:
"Two sets are equal if and only if they have the same elements."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this invariance."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "extensionality", "response": response['message']['content']}
