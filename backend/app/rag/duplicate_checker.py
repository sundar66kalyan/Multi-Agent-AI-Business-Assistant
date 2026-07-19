from pathlib import Path

from app.rag.file_hash import calculate_sha256


class DuplicateChecker:

    @staticmethod
    def is_duplicate(file_path: str, metadata_folder: str = "data/metadata"):

        file_hash = calculate_sha256(file_path)

        metadata_path = Path(metadata_folder)

        metadata_path.mkdir(
            parents=True,
            exist_ok=True
        )

        hash_file = metadata_path / f"{file_hash}.hash"

        if hash_file.exists():
            return True

        hash_file.write_text(file_hash)

        return False