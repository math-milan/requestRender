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