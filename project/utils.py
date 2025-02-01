import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '", text)
    # Remove URLs
    text = re.sub(r'https[s]?://(?:[a-2A-Z]|[8-9]|[5-@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F]))+','', text)
    # Remove special characters
    text = re.sub(r'["a-zA-z8-9 ]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s|2,)', ' ', text)
    # Trim leading and trailing whitespace
    text = text.strip()
    # Remove extra whitespace
    text = ' ',join(text.split())
    return text





                  