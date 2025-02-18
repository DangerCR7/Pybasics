import streamlit as st
from pdf2docx import Converter
from docx2pdf import convert
import os
import tempfile

# Function to convert PDF to Word
def pdf_to_word(pdf_file):
    try:
        # Create a temporary file for the output Word document
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
            output_file = tmp_file.name

        # Convert PDF to Word
        cv = Converter(pdf_file)
        cv.convert(output_file, start=0, end=None)
        cv.close()

        return output_file
    except Exception as e:
        st.error(f"Error converting PDF to Word: {e}")
        return None

# Function to convert Word to PDF
def word_to_pdf(docx_file):
    try:
        # Create a temporary file for the output PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            output_file = tmp_file.name

        # Convert Word to PDF
        convert(docx_file, output_file)

        return output_file
    except Exception as e:
        st.error(f"Error converting Word to PDF: {e}")
        return None

# Streamlit App
st.title("📄 Document Converter")
st.write("Convert PDF to Word (DOCX) and vice versa, or other document formats.")

# Sidebar for file upload
st.sidebar.header("Upload File")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx"])

if uploaded_file is not None:
    file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.sidebar.write(file_details)

    # Conversion options
    st.subheader("Conversion Options")
    if uploaded_file.type == "application/pdf":
        if st.button("Convert PDF to Word"):
            with st.spinner("Converting..."):
                # Save the uploaded file to a temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                    tmp_pdf.write(uploaded_file.getvalue())
                    pdf_path = tmp_pdf.name

                # Convert PDF to Word
                output_file = pdf_to_word(pdf_path)
                if output_file:
                    st.success("Conversion successful!")
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label="Download Word File",
                            data=f,
                            file_name="converted.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    os.unlink(output_file)  # Clean up temporary file
                os.unlink(pdf_path)  # Clean up temporary PDF file

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        if st.button("Convert Word to PDF"):
            with st.spinner("Converting..."):
                # Save the uploaded file to a temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
                    tmp_docx.write(uploaded_file.getvalue())
                    docx_path = tmp_docx.name

                # Convert Word to PDF
                output_file = word_to_pdf(docx_path)
                if output_file:
                    st.success("Conversion successful!")
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label="Download PDF File",
                            data=f,
                            file_name="converted.pdf",
                            mime="application/pdf"
                        )
                    os.unlink(output_file)  # Clean up temporary file
                os.unlink(docx_path)  # Clean up temporary DOCX file

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")