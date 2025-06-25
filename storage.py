
import json
from pathlib import Path

def load_data(path: str):
    p = Path(path)
    if not p.exists():
        p.write_text("[]", encoding="utf-8")
    return json.loads(p.read_text(encoding="utf-8"))

def save_data(path: str, data):
    Path(path).write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )