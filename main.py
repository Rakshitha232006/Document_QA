import streamlit as st

from document_qna import get_answer


st.title("Document Q & A")

st.write(
    "THIS APPLICATION WILL BE USED TO ANSWER QUESTIONS "
    "BASED ON CONTEXT PROVIDED."
)


uploaded_file = st.file_uploader(
    "Upload your file",
    type=["txt", "pdf", "docx"]
)


question = st.text_input(
    "Input your question"
)


if st.button("Submit"):

    if uploaded_file is None:
        st.warning("Please upload a file.")

    elif not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Finding the answer..."):

            answer = get_answer(
                uploaded_file,
                question
            )

        st.subheader("Answer")
        st.write(answer)