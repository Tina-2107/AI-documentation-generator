from dataclasses import dataclass
from typing import Any


@dataclass
class CodeChunk:
    id: str
    content: str
    metadata: dict[str, Any]