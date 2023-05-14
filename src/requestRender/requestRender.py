from selenium import webdriver
import chromedriver_autoinstaller
import requests
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time

class RequestRender:
    def __init__(self, session : requests.Session, headless : bool = True) -> None:
        """
        Constructstor for the RequestRender

        :session: A request Session to parse cookies to the Webbrowser
        :headless: If true the browser is stared as headless
        :return: returns nothing
        """
        self._session, self._headless = session, headless

        chromedriver_autoinstaller.install()    # Check if the current version of chromedriver exists
                                                # and if it doesn't exist, download it automatically,
                                                # then add chromedriver to path
        self.__start_driver()

    def __start_driver(self):
        """
        Start the Webdriver

        :return: returns nothing
        """
        chrome_options = Options()
        chrome_options.headless = self._headless
        chrome_options.add_argument("--log-level=OFF")
        self._driver = webdriver.Chrome(chrome_options=chrome_options)

    def __get_root_url(self, url: str) -> str:
        return urlparse(url).scheme + "://" + urlparse(url).netloc

    def __load_cookies(self, root_domain : str = None):
        """
        Load the cookies 
        :return: returns nothing
        """
        for item in self._session.cookies:
            if root_domain is None or self.__get_root_url(item.domain) in root_domain: continue
            self._driver.add_cookie({'httpOnly': False, 'name': item.name, 'value': item.value})

    def renderResponse(self, response : requests.Response) -> str:
        """
        Render a Website with all javascript Content
        :response: A request Response
        :return: Returns a string that contains the page source html
        """
        self._driver.get(urlparse(response.url).scheme + "://" + urlparse(response.url).netloc)
        self.__load_cookies()
        self._driver.get(response.url)
        time.sleep(3)   # TODO this must change and is just a dume hack but i dnot know how to do it better! Please let me know how!!
        return self._driver.page_source
    
    def renderUrl(self, url : str) -> str:
        """
        Render a Website with all javascript Content
        :url: A url that gets renderd.
        :return: Returns a string that contains the page source html
        """
        self._driver.get(self.__get_root_url(url))
        self.__load_cookies(url)
        self._driver.get(self.__get_root_url(url))
        time.sleep(3)   # TODO this must change and is just a dume hack but i dnot know how to do it better! Please let me know how!!
        return self._driver.page_source