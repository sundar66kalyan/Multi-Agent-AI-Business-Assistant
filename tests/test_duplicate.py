from pathlib import Path

from app.rag.duplicate_checker import DuplicateChecker

pdf = Path("data/documents/Employee Handbook.pdf")

print("=" * 60)
print("DUPLICATE TEST")
print("=" * 60)

first = DuplicateChecker.is_duplicate(pdf)

print("First Upload :", first)

second = DuplicateChecker.is_duplicate(pdf)

print("Second Upload:", second)