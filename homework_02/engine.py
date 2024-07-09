"""
create dataclass `Engine`
"""
from dataclasses import dataclass

# @dataclass(frozen=True)
# @dataclass(slots=True)
@dataclass
class Engine:
    volume: int
    pistons: int
