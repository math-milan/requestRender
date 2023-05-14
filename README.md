# requestRender
A PyPI package that provides a simple headless Selenium web browser for scraping wrapper around reactive websites.

# How to install it
```
pip install requestRender
```
You also need the have Chrome installed to run this, because it uses Selenuim with Chrome as a headless Browser.

# How to use it?
```
import requests
import requestRender

# Start a session
session = requests.Session()
# Start the browser
browser = requestRender.requestRender.RequestRender(session)
# Get the response from the website
response = session.get("https://www.midjourney.com")  
# Render the response to get the render the javascript content
html = browser.renderResponse(response)
# Save the html to a file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
```

# What needs to Improve

1. The logging off the Browser needs be disabeld.
2. A methode to determin if a website has loaded fully. At the moment the software just waits a 3 Seconds.