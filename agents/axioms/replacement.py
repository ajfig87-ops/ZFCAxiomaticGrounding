import ollama

class ReplacementAgent:
    """Embodies ZFC Axiom of Replacement: Images of sets under functions are sets."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Replacement:
"For any set x and any function F, the image {F(x)} is also a set."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this replacement principle."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "replacement", "response": response['message']['content']}
