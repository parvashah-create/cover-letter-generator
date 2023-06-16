import io
import PyPDF2

def pdf_loader(pdf):
    # Create a BytesIO object with the PDF data
    pdf_file = io.BytesIO(pdf)
    
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(pdf_file)
    
    # Initialize an empty string to store the extracted text
    extracted_text = ""
    
    # Iterate over each page in the PDF
    for page_num in range(len(reader.pages)):
        # Get the current page
        page = reader.pages[page_num]
        
        # Extract text from the page
        text = page.extract_text()
        
        # Append the extracted text to the result
        extracted_text += text
    
    # Return the extracted text
    return extracted_text