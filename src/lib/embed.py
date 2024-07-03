from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, CacheBackedEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from langchain.vectorstores import FAISS
from langchain.storage import LocalFileStore

def embed_file (file):
  file_content = file.read()
  file_path = f"./.cache/files/{file.name}"
  
  with open(file_path, "wb") as f:
    f.write(file_content)
  
  cache_dir = LocalFileStore(f"./.cache/embeddings/{file.name}")
  splitter = CharacterTextSplitter.from_tiktoken_encoder(
      separator="\n", 
      chunk_size=600,
      chunk_overlap=100,
  )

  embedder = OpenAIEmbeddings()
  cached_embedder = CacheBackedEmbeddings.from_bytes_store(embedder, cache_dir)

  loarder = UnstructuredFileLoader(f"./.cache/files/{file.name}")
  docs = loarder.load_and_split(text_splitter=splitter)
  vector_store = FAISS.from_documents(docs, cached_embedder)
  retriever = vector_store.as_retriever()
  return retriever