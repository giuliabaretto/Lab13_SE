from dataclasses import dataclass

@dataclass
class Gene:
    id : str
    funzione: str
    essenziale : str
    cromosoma : int

    def __str__(self):
        return f"Gene {self.id}, {self.funzione}, {self.essenziale}, {self.cromosoma}"

    def __eq__(self, other):
        return self.id == other.id and self.funzione == other.funzione

    def __hash__(self):
        return hash(self.id)

