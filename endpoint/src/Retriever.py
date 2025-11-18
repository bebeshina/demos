import numpy as np
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from src import templates


class Retriever:
    config : dict
    @staticmethod
    def cosine_sim_score(v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


    def __init__(self, config: dict=None):
        if config:
            self.config = config
        else:
            self.config = {"completion_model": "llama3.2",
                        "embedding_model": "mxbai-embed-large",
                        "vectorstore_path": "vectors"}
        self.completion_model = OllamaLLM(model=self.config.get("completion_model"))
        self.embed_model = OllamaEmbeddings(model=self.config.get("embedding_model"))
        self.VECTOR_DIR = self.config.get("vectorstore_path")
        self.persisted_vectorstore = FAISS.load_local(f"{self.VECTOR_DIR}", self.embed_model,
                                                      allow_dangerous_deserialization=True)
        self.qa_chain = create_stuff_documents_chain(self.completion_model, templates.prompt)
        self.qa = create_retrieval_chain(self.persisted_vectorstore.as_retriever(), self.qa_chain)

    def __call__(self, config: dict = None):
        if config:
            self.config = config
        else:
            self.config = {"completion_model": "llama3.2",
                           "embedding_model": "mxbai-embed-large",
                           "vectorstore_path": "vectors"}
        self.completion_model = OllamaLLM(model=self.config.get("completion_model"))
        self.embed_model = OllamaEmbeddings(model=self.config.get("embedding_model"))
        self.VECTOR_DIR = self.config.get("vectorstore_path")
        self.qa_chain = create_stuff_documents_chain(self.completion_model, templates.prompt)
        self.qa = create_retrieval_chain(self.persisted_vectorstore.as_retriever(), self.qa_chain)

    def __run_query__(self, query: str):
        result = self.qa.invoke({"input":query})
        v1 = self.embed_model.embed_query(result["input"])
        v2 = self.embed_model.embed_documents(result["answer"])[0]
        for doc in result["context"]:
            c_vec = self.embed_model.embed_documents(doc.page_content)[0]
            local_context_cosine = self.cosine_sim_score(v1, c_vec)
            print(f"context_score {doc.id}", local_context_cosine)
        score = self.cosine_sim_score(v1, v2)
        print(result)
        print(score)
        return result["answer"], score


