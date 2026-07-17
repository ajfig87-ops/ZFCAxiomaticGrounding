import ollama
from agents.axioms.extensionality import ExtensionalityAgent

class FormalLanguageAgent:
    """Constructs a formal language from { and } with concatenation rules."""
    
    def __init__(self):
        self.ext = ExtensionalityAgent()
    
    def define_language(self):
        prompt = """Using only the symbols { and }, define a formal language with these properties:
1. Left-to-right concatenation rules
2. Produces unordered sets via Extensionality
3. Capable of encoding arithmetic
4. Self-referentially encodes ZFC axioms (starting with Empty Set)

Explore possible grammar and semantics. Look for fixed points or invariances."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"language_definition": response['message']['content']}
