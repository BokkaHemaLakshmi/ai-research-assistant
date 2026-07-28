import streamlit as st
import requests
import os

st.set_page_config(
    page_title="AI Research Assistant & RAG",
    page_icon="📚",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

st.title("📚 AI Research Assistant & Document Intelligence")
st.markdown("Upload research papers, automatically classify them using TensorFlow, and query insights powered by RAG.")

# Sidebar Navigation
page = st.sidebar.selectbox("Navigation", ["Upload & Classify", "Research Query (RAG)"])

if page == "Upload & Classify":
    st.header("📄 Document Ingestion & Classification")
    uploaded_file = st.file_uploader("Choose a PDF research paper", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Upload and Process"):
            with st.spinner("Processing document..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                try:
                    response = requests.post(f"{API_URL}/api/v1/documents/upload", files=files)
                    if response.status_code == 200:
                        data = response.json()
                        st.success(data["message"])
                        
                        col1, col2, col3 = st.columns(3)
                        col1.metric("Predicted Category", data["predicted_category"])
                        col2.metric("Total Pages", data["total_pages"])
                        col3.metric("Total Chunks", data["total_chunks"])
                    else:
                        st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
                except Exception as e:
                    st.error(f"Could not connect to backend API: {e}")

elif page == "Research Query (RAG)":
    st.header("🔍 Intelligent Research Query")
    query = st.text_input("Ask a question about your uploaded documents:")
    
    if st.button("Search & Generate Answer"):
        if query.strip():
            with st.spinner("Retrieving context and generating answer..."):
                try:
                    response = requests.post(f"{API_URL}/api/v1/query", json={"query": query})
                    if response.status_code == 200:
                        ans_data = response.json()
                        st.subheader("Answer")
                        st.write(ans_data.get("answer", "No answer generated."))
                    else:
                        st.warning("RAG query endpoint is ready for wiring up next!")
                except Exception as e:
                    st.error(f"Error connecting to backend: {e}")
        else:
            st.warning("Please enter a valid query.")