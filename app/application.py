from pages.black_ri_homepage import BlackHomepage
from pages.black_ri_header import BlackHeader


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.black_ri_homepage = BlackHomepage(self.driver)
        self.black_ri_header = BlackHeader(self.driver)

