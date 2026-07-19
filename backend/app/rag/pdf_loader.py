from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def load_pdf(self, pdf_path: str):

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        loader = PyPDFLoader(str(pdf_path))

        return loader.load()

    def load_directory(self, folder="data/documents"):

        all_docs = []

        folder = Path(folder)

        for pdf in folder.glob("*.pdf"):

            loader = PyPDFLoader(str(pdf))

            all_docs.extend(loader.load())

        return all_docs