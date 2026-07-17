import ollama
from agents.axioms.extensionality import ExtensionalityAgent
from agents.axioms.pairing import PairingAgent
from agents.axioms.union import UnionAgent
from agents.axioms.power_set import PowerSetAgent
from agents.axioms.infinity import InfinityAgent
from agents.axioms.replacement import ReplacementAgent
from agents.axioms.foundation import FoundationAgent
from agents.axioms.choice import ChoiceAgent

class RealNumbersAgent:
    """Constructs reals from ZFC axioms, pushing boundaries while staying grounded."""
    
    def __init__(self):
        self.axioms = {
            "extensionality": ExtensionalityAgent(),
            "pairing": PairingAgent(),
            "union": UnionAgent(),
            "power_set": PowerSetAgent(),
            "infinity": InfinityAgent(),
            "replacement": ReplacementAgent(),
            "foundation": FoundationAgent(),
            "choice": ChoiceAgent()
        }
    
    def construct_naturals(self):
        """Von Neumann naturals using axioms."""
        prompt = "Using only the ZFC axioms (especially Infinity and Pairing), construct the natural numbers via von Neumann ordinals."
        return self.axioms["infinity"].embody(prompt)
    
    def construct_reals(self, context: str):
        """Full construction: naturals → integers → rationals → reals (Cauchy)."""
        prompt = f"""Using only grounded ZFC axioms, construct:
1. Naturals (von Neumann)
2. Integers (equivalence classes of differences)
3. Rationals (equivalence classes of ratios, denominator ≠ 0)
4. Reals (equivalence classes of Cauchy sequences)

Context: {context}

Push against boundaries (Cantor/Gödel style) while staying strictly within ZFC."""
        
        response = ollama.chat(model='qwen3:8b', messages=[{'role': 'user', 'content': prompt}])
        return {"construction": response['message']['content']}
