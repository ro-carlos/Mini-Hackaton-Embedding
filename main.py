import os
import chromadb
from sentence_transformers import SentenceTransformer

# Modelo para generar embeddings (puedes cambiarlo por otro)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Crear el cliente de ChromaDB (opcional: cambiar path para persistencia)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Crear la colección donde almacenaremos los documentos
collection = chroma_client.get_or_create_collection(name="markdown_docs")

# Directorio donde están los archivos Markdown
markdown_dir = "./markdown_pages"

# Leer los archivos y guardarlos en ChromaDB
for filename in os.listdir(markdown_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(markdown_dir, filename)

        # Leer el contenido del archivo
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Convertir el texto en un embedding
        embedding = model.encode(content).tolist()

        # Agregar a la base de datos con metadata (nombre del archivo)
        collection.add(
            ids=[filename],
            embeddings=[embedding],
            metadatas=[{"filename": filename, "content": content}]
        )

print("✅ Archivos indexados en ChromaDB")
