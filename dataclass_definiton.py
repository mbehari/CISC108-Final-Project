from dataclasses import dataclass
from designer import *

@dataclass
class World:
    title_message: DesignerObject
    correct_message: DesignerObject
    musical_notes: list[DesignerObject]
    total_score: int
    counter: DesignerObject

