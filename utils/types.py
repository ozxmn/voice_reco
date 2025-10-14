# utils/types.py
from dataclasses import dataclass
import numpy as np

@dataclass
class RecordingResult:
    name: str
    audio: np.ndarray
    discarded: bool

