# requestRender
This PyPI package offers a straightforward, headless Selenium web browser designed for scraping reactive websites. It proves beneficial when you require the use of requests but need to render certain sites to retrieve their JavaScript or PHP rendered content. An alternative project capable of accomplishing this task is request-html; however, it is currently unmaintained and non-functional. This is my bad attempt to provide a package with a similar function

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

# What needs to improve

1. The logging off the Browser needs be disabeld.
2. A methode to determin if a website has loaded fully. At the moment the software just waits a 3 Seconds.
