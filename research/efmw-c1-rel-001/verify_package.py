"""Check archived file integrity without network access or scientific packages."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
manifest = root / "MANIFEST.sha256"
count = 0
for line in manifest.read_text().splitlines():
    digest, name = line.split("  ", 1)
    path = root / name
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit("FAIL archive digest: " + name)
    count += 1
lock = json.loads((root / "SCOPE_LOCK.json").read_text())
for name, digest in lock["sha256"].items():
    if hashlib.sha256((root / name).read_bytes()).hexdigest() != digest:
        raise SystemExit("FAIL input lock: " + name)
sources = json.loads((root / "sources/CONNECTOR_SOURCES.json").read_text())
for source in sources:
    data = (root / source["local_path"]).read_bytes()
    git_hash = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if git_hash != source["git_blob_sha1"]:
        raise SystemExit("FAIL source Git blob: " + source["local_path"])
print(f"PASS: {count} manifest entries; {len(lock['sha256'])} locked inputs; {len(sources)} Git blob identities")
