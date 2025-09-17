## 📄 `README.md`

# 🌍 Ubuntu Image Fetcher

> *"I am because we are"* — Ubuntu philosophy  

This project is part of the **Ubuntu_Requests** assignment.  
It’s a Python tool that respectfully connects to the wider web community, fetches images, and organizes them for later sharing.  

---

## ✨ Features
- 📥 Download one or more images from given URLs (comma-separated input)  
- 🗂️ Automatically creates a `Fetched_Images/` folder  
- 🔒 Skips duplicate images (using SHA256 hash checks)  
- ✅ Checks HTTP headers to ensure only images are saved  
- 🛡️ Graceful error handling for failed connections  
- 🙏 Uses a polite `User-Agent` for respectful requests  

---

## 📂 Repository Structure
```

Ubuntu\_Requests/
├── ubuntu\_fetcher.py   # Main script
├── README.md           # Documentation
└── Fetched\_Images/     # Created automatically when images are downloaded

````

---

## ⚙️ Requirements
You need:  
- **Python 3.7+** installed  
- The `requests` library  

Install `requests` with:
```bash
pip install requests
````

If you’re using **pip3**:

```bash
pip3 install requests
```

---

## ▶️ Usage

Run the script from your terminal:

```bash
python ubuntu_fetcher.py
```

Or (depending on your setup):

```bash
python3 ubuntu_fetcher.py
```

When prompted, enter one or more image URLs, separated by commas.

### Example Run

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by commas): 
https://assets.ubuntu.com/v1/8dd99b80-suru-dark.png, https://www.python.org/static/community_logos/python-logo.png

✓ Successfully fetched: suru-dark.png
✓ Image saved to Fetched_Images/suru-dark.png
✓ Successfully fetched: python-logo.png
✓ Image saved to Fetched_Images/python-logo.png

Connection strengthened. Community enriched.
```

---

## 🌍 Example URLs to Try

Here are some safe image links you can test with:

```text
https://assets.ubuntu.com/v1/8dd99b80-suru-dark.png
https://www.python.org/static/community_logos/python-logo.png
https://apod.nasa.gov/apod/image/1901/IC405_Abolfath_3952.jpg
https://via.placeholder.com/300.png
```

You can copy and paste multiple, separated by commas:

```text
https://assets.ubuntu.com/v1/8dd99b80-suru-dark.png, https://www.python.org/static/community_logos/python-logo.png
```

---

## 🔒 Safety Precautions

* Saves only if the response has `Content-Type: image/...`
* Skips duplicates by comparing file hashes
* Respects connection timeouts
* Handles errors gracefully instead of crashing

---

## 📜 Ubuntu Principles in Action

* **Community** → downloading from the web connects us globally
* **Respect** → polite requests and clean error handling
* **Sharing** → images neatly stored for later use
* **Practicality** → a simple, useful real-world tool

---

## 📝 License

This project is for educational purposes.
Inspired by Ubuntu: *"A person is a person through other persons."*
