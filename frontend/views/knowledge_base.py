import streamlit as st
from dashboard.api import DashboardAPI


def show_knowledge_base():
    """Knowledge Base Page"""

    st.title("📚 Knowledge Base")
    st.caption("Manage documents used by the AI Assistant")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Upload",
            "📚 Documents",
            "🔍 Search",
            "📊 Statistics",
        ]
    )

    # ====================================================
    # Upload - FIXED
    # ====================================================

    with tab1:

        st.subheader("Upload PDF")

        uploaded = st.file_uploader(
            "Choose a PDF",
            type=["pdf"]
        )

        if uploaded:

            st.success(f"Selected: {uploaded.name}")

            # Show file info
            col1, col2 = st.columns(2)
            with col1:
                st.metric("File Name", uploaded.name)
            with col2:
                file_size = len(uploaded.getvalue()) / 1024  # KB
                st.metric("File Size", f"{file_size:.2f} KB")

            if st.button(
                "📤 Upload Document",
                use_container_width=True
            ):

                with st.spinner("Uploading and processing document..."):
                    try:

                        # ✅ FIXED: Better response handling
                        response = DashboardAPI.upload_pdf(uploaded)

                        if response.get("success", False):
                            st.success(response.get("message", "Document uploaded successfully."))
                            
                            # Display metrics if available
                            pages = response.get("pages", 0)
                            chunks = response.get("chunks", 0)
                            
                            if pages or chunks:
                                st.divider()
                                st.subheader("📊 Processing Results")
                                
                                col1, col2 = st.columns(2)
                                with col1:
                                    st.metric("📄 Pages", pages)
                                with col2:
                                    st.metric("🧩 Chunks", chunks)

                        else:
                            # ✅ FIXED: Better error message extraction
                            message = (
                                response.get("detail")
                                or response.get("message")
                                or response.get("error")
                                or "Upload failed."
                            )
                            st.warning(f"⚠️ {message}")

                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

    # ====================================================
    # Documents
    # ====================================================

    with tab2:

        st.subheader("Indexed Documents")

        try:

            # Fetch documents from API
            docs = DashboardAPI.get_documents()

            if docs and docs.get("success", True):
                
                # Display total documents count
                st.metric(
                    "📚 Indexed Documents",
                    docs.get("total_documents", 0)
                )

                st.divider()

                # Display documents dataframe
                if docs.get("documents"):

                    st.dataframe(
                        docs["documents"],
                        use_container_width=True
                    )

                else:

                    st.info("📭 No documents indexed yet. Upload a PDF to get started.")

            else:

                st.warning(docs.get("error", "Failed to load documents."))

        except Exception as e:

            st.warning(f"Documents API not connected: {str(e)}")

    # ====================================================
    # Search
    # ====================================================

    with tab3:

        st.subheader("🔍 Search Knowledge Base")

        query = st.text_input(
            "Enter your search query",
            placeholder="e.g., What is the leave policy?"
        )

        if st.button(
            "🔍 Search",
            use_container_width=True
        ):

            if query:

                try:

                    # Search documents
                    result = DashboardAPI.search_documents(query)

                    if result.get("success"):

                        results = result.get("results", [])

                        if results:
                            st.success(f"Found {len(results)} results")

                            for idx, item in enumerate(results):
                                with st.container(border=True):
                                    st.write(f"**Result {idx + 1}**")
                                    st.write(item.get("content", "No content available"))
                                    st.caption(f"📄 Document: {item.get('document', 'Unknown')}")
                                    st.caption(f"📑 Page: {item.get('page', 'N/A')}")
                        else:
                            st.info("🔍 No results found for your query.")

                    else:

                        st.warning(result.get("error", "Search failed"))

                except Exception as e:

                    st.warning(f"Search API unavailable: {str(e)}")

            else:

                st.info("Please enter a search query.")

    # ====================================================
    # Statistics
    # ====================================================

    with tab4:

        st.subheader("📊 Knowledge Base Statistics")

        try:

            dashboard = DashboardAPI.get_dashboard()

            if dashboard.get("success"):

                analytics = dashboard.get("dashboard", {}).get("analytics", {})

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "📄 Documents",
                        analytics.get("documents", 0)
                    )

                with col2:
                    st.metric(
                        "🧩 Chunks",
                        analytics.get("chunks", 0)
                    )

                with col3:
                    st.metric(
                        "💰 Finance Records",
                        analytics.get("finance_records", 0)
                    )

            else:

                st.warning("Unable to load statistics.")

        except Exception as e:

            st.warning(f"Statistics unavailable: {str(e)}")