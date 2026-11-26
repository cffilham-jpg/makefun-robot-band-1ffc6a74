"""Write the robot band's one-line entry as deterministic UTF-8 text.
The Roombas pairs recognizable robots with a concrete charger-eating joke.
"""

import os
from pathlib import Path


LINE = "The Roombas — hit single \"I Ate Your Charger\""

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 200:
    raise ValueError("The entry line must be at most 200 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
