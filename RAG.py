import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="C++ RAG Chatbot", page_icon="🤖")

st.title("🤖 C++ RAG Chatbot")
st.write("Ask any question related to C++.")

# -----------------------------
# Load and Process Documents
# -----------------------------
@st.cache_resource
def load_vector_db():
    loader = TextLoader("cppdata.txt", encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )

    final_documents = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(final_documents, embeddings)

    return db

db = load_vector_db()

# -----------------------------
# User Query
# -----------------------------
query = st.text_input("Ask a question about C++")

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        docs = db.similarity_search(query, k=3)

        st.subheader("Relevant Results")

        for i, doc in enumerate(docs, start=1):
            st.markdown(f"### Result {i}")
            st.write(doc.page_content)