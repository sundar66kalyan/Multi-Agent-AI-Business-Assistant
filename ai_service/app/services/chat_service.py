from groq import Groq
import os

print("=" * 80)
print("CHAT SERVICE LOADED FROM:")
print(os.path.abspath(__file__))
print("=" * 80)
from app.core.config import settings
from app.rag.vectordb import VectorDB


class ChatService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )
        
        print("=" * 60)
        print("GROQ KEY:", repr(settings.GROQ_API_KEY))
        print("KEY LENGTH:", len(settings.GROQ_API_KEY))
        print("=" * 60)

        self.db = VectorDB()

    def ask(self, question: str):

        docs = self.db.similarity_search(
            question,
            k=5
        )

        print("=" * 80)
        print("QUESTION:", question)
        print("DOCUMENTS FOUND:", len(docs))

        for i, doc in enumerate(docs, 1):
            print("-" * 60)
            print(f"Document {i}")
            print(doc.page_content[:300])

        print("=" * 80)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        print("=" * 80)
        print("CONTEXT SENT TO LLM")
        print(context)
        print("=" * 80)

        prompt = f"""
You are an intelligent business assistant.

Answer ONLY using the provided context.

If the answer is not present in the documents,
reply:

"I couldn't find that information in the knowledge base."

Context:

{context}

Question:

{question}

Answer:
"""

        print("=" * 80)
        print(prompt)
        print("=" * 80)

        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        print("=" * 80)
        print("LLM RESPONSE")
        print(response.choices[0].message.content)
        print("=" * 80)

        return {
            "answer": response.choices[0].message.content,
            "documents": len(docs)
        }