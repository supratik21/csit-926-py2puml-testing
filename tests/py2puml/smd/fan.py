from dataclasses import dataclass, field
from typing import List

@dataclass
class Class01:
    name: str

@dataclass
class Class02:
    name: str

@dataclass
class Class03:
    name: str

@dataclass
class Class04:
    name: str

@dataclass
class Class05:
    name: str

@dataclass
class Class06:
    name: str

@dataclass
class Class07:
    name: str

@dataclass
class Class08:
    name: str

@dataclass
class Class09:
    name: str

@dataclass
class Class10(Class01):
    name: str
    property: List[Class05]
