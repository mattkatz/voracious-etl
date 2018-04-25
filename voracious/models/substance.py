from voracious.models.entity import Entity
from dataclasses import dataclass

@dataclass
class Substance(Entity):

    name: str
    rating: int
