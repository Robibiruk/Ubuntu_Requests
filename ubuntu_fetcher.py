import requests
import os
import hashlib
from urllib.parse import urlparse

def get_filename_from_url(url):
    """Extract filename from URL, or generate one if not available."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_already_exists(filepath, content):
    """Check if a file with the same content already exists (avoid duplicates)."""
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, "rb") as f:
        existing_content = f.read()
        return hashlib.sha256(existing_content).hexdigest() == hashlib.sha256(content).hexdigest()

def fetch_image(url):
    """Fetch a single image from the web and save it locally."""
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        headers = {"User-Agent": "UbuntuFetcher/1.0 (Respectful Client)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Content-Type precaution (ensure it's an image)
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: {url} (not an image)")
            return

        # Extract filename
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if file_already_exists(filepath, response.content):
            print(f"↺ Duplicate skipped: {filename}")
            return

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs (comma-separated)
    urls = input("Please enter one or more image URLs (separated by commas): ")
    for url in urls.split(","):
        fetch_image(url.strip())

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
