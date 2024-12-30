import streamlit as st
# import pyperclip

def generate_email_html(banner_url, email_text, left_image_url=None, left_image_width=200, right_image_url=None):
    # Remove any formatting from the text
    email_text = email_text.replace('\n', ' ').replace('\r', ' ')
    # Split the email text into paragraphs
    paragraphs = email_text.split('. ')
    # Wrap each paragraph with <p> tags
    formatted_text = ''.join([f'<p>{para.strip()}.</p>' for para in paragraphs if para.strip()])
    
    # Add left image if provided
    if left_image_url:
        formatted_text = f'<img src="{left_image_url}" alt="Left Image" style="float: left; margin-right: 10px; width: {left_image_width}px; height: auto;">' + formatted_text
    
    # Add right image if provided
    if right_image_url:
        formatted_text = f'<img src="{right_image_url}" alt="Right Image" style="float: right; margin-left: 10px; width: 200px; height: auto;">' + formatted_text
    
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="margin: 0; padding: 0; width: 100%; font-family: Arial, sans-serif;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" width="700" style="border-collapse: collapse; margin: 0 auto; background-color: #f9f9f9;">
            <tr>
                <td align="center" style="padding: 20px 0;">
                    <img src="{banner_url}" alt="Banner Image" style="display: block; width: 100%; height: auto;">
                </td>
            </tr>
            <tr>
                <td style="padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                    {formatted_text}
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    return html_code

st.title("Email HTML Generator")

banner_checkbox = st.checkbox("Banner URL")
left_image = st.checkbox("Left Image")
right_image = st.checkbox("Right Image")

banner_url = None
left_image_url = None
left_image_width = 200
right_image_url = None

if banner_checkbox:
    banner_url = st.text_input("Enter the URL of the banner image:")

if left_image:
    left_image_url = st.text_input("Enter the URL of the left image:")
    left_image_width = st.text_input("Enter the width of the left image (in pixels):", value="200")

if right_image:
    right_image_url = st.text_input("Enter the URL of the right image:")

email_text = st.text_area("Paste the text for the email:")

if st.button("Generate HTML"):
    if banner_checkbox and not banner_url:
        st.error("Please provide the banner URL.")
    elif left_image and not left_image_url:
        st.error("Please provide the URL for the left image.")
    elif right_image and not right_image_url:
        st.error("Please provide the URL for the right image.")
    elif email_text:
        html_code = generate_email_html(banner_url, email_text, left_image_url, left_image_width, right_image_url)
        st.code(html_code, language='html')
        # pyperclip.copy(html_code)
        st.success("HTML code has been copied to clipboard!")

if st.button("Preview HTML"):
    if banner_checkbox and not banner_url:
        st.error("Please provide the banner URL.")
    elif left_image and not left_image_url:
        st.error("Please provide the URL for the left image.")
    elif right_image and not right_image_url:
        st.error("Please provide the URL for the right image.")
    elif email_text:
        html_code = generate_email_html(banner_url, email_text, left_image_url, left_image_width, right_image_url)
        st.markdown(html_code, unsafe_allow_html=True)
    else:
        st.error("Please provide the email text.")
        