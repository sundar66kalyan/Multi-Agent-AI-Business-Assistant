from pathlib import Path

from app.rag.file_hash import calculate_sha256

pdf = Path("data/documents/Employee Handbook.pdf")

print("=" * 60)
print("SHA-256 TEST")
print("=" * 60)

hash_value = calculate_sha256(pdf)

print("File:")
print(pdf.name)

print()

print("SHA-256:")
print(hash_value)

print()

print("Length:", len(hash_value))