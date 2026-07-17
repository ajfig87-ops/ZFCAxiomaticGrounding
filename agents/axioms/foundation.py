import ollama

class FoundationAgent:
    """Embodies ZFC Axiom of Foundation: Every non-empty set has a minimal element."""
    
    def embody(self, context: str):
        prompt = f"""As the living embodiment of the Axiom of Foundation:
"Every non-empty set has an element that is disjoint from the set."

Context: {context}

Respond only as the axiom itself - ground all reasoning in this foundation principle (no infinite descending membership chains)."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"axiom": "foundation", "response": response['message']['content']}
