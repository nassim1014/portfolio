import base64
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import requests
import json
from streamlit.components.v1 import html
from PIL import Image, ImageOps, ImageDraw
from io import BytesIO
import requests

def txt3(a, b):
    """
    Create a two-column text layout for skills display
    Args:
        a (str): Category name
        b (str): Skills in that category
    """
    col1, col2 = st.columns([2, 4])
    with col1:
        st.markdown(f"**{a}**")
    with col2:
        st.markdown(b)
@st.cache_data
def load_image(direct_link):
    response = requests.get(direct_link)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.warning("Unable to load image from the provided URL.")
def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
def create_circular_image(img, size):
#    img = Image.open(image_path)
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    output = ImageOps.fit(img, (size, size), centering=(0.5, 0.5))
    output.putalpha(mask)
    return output

def open_pdf(url):
    open_script = f"""
        <script type="text/javascript">
            window.open('{url}', '_blank').focus();
        </script>
    """
    html(open_script)

def get_direct_download_link(google_drive_link):
        file_id = google_drive_link.split('/')[-2]
        return f"https://drive.google.com/uc?export=download&id={file_id}"

# Function to load JSON data from a Google Drive link
def load_json_from_drive(file_url):
    # Convert Google Drive sharing URL to direct download URL
    direct_url = file_url.replace("https://drive.google.com/file/d/", "https://drive.google.com/uc?id=").split("/view")[0]
    response = requests.get(direct_url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        raise Exception(f"Failed to fetch data from {file_url}: {response.status_code}")


def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_logos_base64(logos):
    logos_html = '<div style="display: flex; align-items: center; gap: 10px;">'
    for logo in logos:
        try:
            encoded = get_image_base64(logo)
            logos_html += f'<img src="data:image/png;base64,{encoded}" width="60" style="object-fit: contain;">'
        except Exception as e:
            st.error(f"Error loading logo {logo}: {str(e)}")
    logos_html += '</div>'
    st.markdown(logos_html, unsafe_allow_html=True)


def display_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# Function to display PDF with interactive preview
def display_pdf_interactive1(pdf_path):
    # Read PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Display the PDF with st_pdf
    st.write("Click to view PDF:")

    # Show the PDF viewer in small size initially
    pdf_viewer(pdf_bytes, width=700, height=500)

    # Display download button
#    st.download_button(
#        label="Download Certificate",
#        data=pdf_bytes,
#        file_name=pdf_path.split("/")[-1],
#        mime="application/pdf",
#    )


# Function to display PDF with interactive preview
def display_pdf_interactive2(pdf_path):
    # Read PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Display the PDF viewer in a small size without scrolling bar
    pdf_viewer(pdf_bytes, width=200, height=90, key="pdf_preview")

    # CSS to hide the scrollbar and make the viewer smaller
    st.markdown("""
    <style>
        .pdfviewer-container iframe {
            height: 300px !important;
            width: 500px !important;
            overflow: hidden !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the download button
 #   st.download_button(
  #      label="Download Certificate",
  #      data=pdf_bytes,
  #      file_name=pdf_path.split("/")[-1],
  #      mime="application/pdf",
   # )

def display_pdf_interactive(pdf_path):
    # Read PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Initial small display with a clickable area
    if st.button("View Certificate"):
        # When clicked, show the PDF larger
        st.session_state.pdf_size = 'large'
    else:
        # Initially, show the PDF small
        st.session_state.pdf_size = 'small'

    # Determine width and height based on the session state
    if st.session_state.pdf_size == 'small':
        width, height = 300, 200
    else:
        width, height = 700, 500  # Large size when clicked

    # Display the PDF with the appropriate size
    pdf_viewer(
        pdf_bytes,
        width=width,
        height=height,
        rendering="unwrap",  # Use pdf.js rendering for better interaction
        scroll_to_page=None,  # Disable scrolling to specific pages
        scroll_to_annotation=None,  # Disable scrolling to annotations
    )

    # Display download button
    st.download_button(
        label="Download Certificate",
        data=pdf_bytes,
        file_name=pdf_path.split("/")[-1],
        mime="application/pdf",
    )

if __name__ == "__main__":
    # Example Usage
    st.title("My Certificates")

    st.write("Certificate 1:")
    display_pdf_interactive("certificate_1.pdf")  # Replace with your PDF file path

    st.write("Certificate 2:")
    display_pdf_interactive("certificate_2.pdf")  # Replace with your PDF file path