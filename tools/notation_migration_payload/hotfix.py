from pathlib import Path
import sys

script = Path(sys.argv[1])
text = script.read_text(encoding="utf-8")

stale_old = '''        if path.suffix.lower() not in {".md", ".tex", ".txt", ".py", ".yml", ".yaml"}:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
'''
stale_new = '''        relative = path.relative_to(ROOT).as_posix()
        if relative in {
            "proof/MANIFEST.txt",
            ".github/workflows/notation-proof-package-migration.yml",
        } or "notation_migration_payload" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".tex", ".txt", ".py", ".yml", ".yaml"}:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
'''
if stale_old not in text:
    raise SystemExit("phase-3 stale-link block not found")
text = text.replace(stale_old, stale_new, 1)

projection_old = '''    # Update remaining signed-center projections after earlier renames.
    text = text.replace("v.center.a", "v.center.alpha")
    text = text.replace("v.center.d", "v.center.delta")
    text = text.replace("x.center.a", "x.center.alpha")
    text = text.replace("x.center.d", "x.center.delta")
'''
projection_new = '''    # Signed-center projections were normalized above by boundary-aware regexes.
'''
if projection_old not in text:
    raise SystemExit("duplicate signed-center projection block not found")
text = text.replace(projection_old, projection_new, 1)

script.write_text(text, encoding="utf-8")
