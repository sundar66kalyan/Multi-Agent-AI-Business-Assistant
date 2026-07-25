from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from langchain_core.documents import Document


def load_documents(folder: str):

    """
    Load all PDF documents from a folder.
    """

    documents = []

    folder_path = Path(folder)

    if not folder_path.exists():
        return documents

    pdf_files = list(folder_path.glob("*.pdf"))

    for pdf in pdf_files:

        try:

            loader = PyPDFLoader(str(pdf))

            docs = loader.load()

            documents.extend(docs)

        except Exception as e:

            print(f"Failed to load {pdf.name}: {e}")

    return documents