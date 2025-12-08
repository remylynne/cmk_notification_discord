from dataclasses import dataclass
from typing import Optional



@dataclass
class Field:
    name: str
    value: str

@dataclass
class Footer:
    text: str
    icon_url: Optional[str] = None

@dataclass
class Embed:
    title: str
    color: int
    description: str = ""
    fields: Optional[list[Field]] = None
    footer: Optional[Footer] = None

@dataclass
class Message:
    embeds: list[Embed]