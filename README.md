## 📄 `README.md`

```markdown
# Ubuntu Image Fetcher

> *"I am because we are"* — Ubuntu philosophy  

This project is part of the **Ubuntu_Requests** assignment.  
It’s a Python tool that respectfully connects to the wider web community, fetches images, and organizes them for later sharing.  

The script demonstrates Ubuntu values in programming:
- **Community** → connects to the global web, sharing in its resources  
- **Respect** → handles errors gracefully, no crashes  
- **Sharing** → saves images neatly in `Fetched_Images/`  
- **Practicality** → a simple, useful tool for collecting and organizing images  

---

## ✨ Features
- Fetches images from one or more URLs (comma-separated input)  
- Creates a `Fetched_Images/` folder automatically  
- Prevents saving duplicate images (using SHA256 hash comparison)  
- Checks HTTP headers (only saves files if they are actual images)  
- Graceful error handling for connection issues  
- Polite `User-Agent` for respectful requests  

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
- Python 3.7+  
- `requests` library  

Install dependencies:
```bash
pip install requests
````

---

## ▶️ Usage

Run the script:

```bash
python ubuntu_fetcher.py
```

Example run:

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

## 🌍 Example URLs

Here are some safe images you can test with:

* Ubuntu wallpaper → `https://assets.ubuntu.com/v1/8dd99b80-suru-dark.png`
* Python logo → `https://www.python.org/static/community_logos/python-logo.png`
* NASA APOD sample → `https://apod.nasa.gov/apod/image/1901/IC405_Abolfath_3952.jpg`
* Placeholder image → `https://via.placeholder.com/300.png`

---

## 🔒 Safety Precautions

* Only saves files if the server responds with `Content-Type: image/...`
* Respects timeouts and connection failures without crashing
* Skips duplicates to save space
* Uses a polite `User-Agent`

---

## 📜 Ubuntu Principles in Action

* **Community** → downloading from the web connects us to the global community
* **Respect** → errors are handled gracefully, respecting both user and server
* **Sharing** → images are neatly stored for reuse and collaboration
* **Practicality** → the script solves a real-world problem in a simple way

---

## 📝 License

This project is for educational purposes.
Inspired by the Ubuntu philosophy: *"A person is a person through other persons."*

```
