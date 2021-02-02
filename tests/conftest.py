import json
import platform
import pytest
from selenium import webdriver


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    chrome_version_win = "88"
    chrome_version_mac = "88"
    chrome_version_linux = "88"
    geckodriver_version_win = "28"
    geckodriver_version_mac = "28"
    geckodriver_version_linux = "27"

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        if 'Win' in platform.platform():
            browser = webdriver.Firefox(executable_path="../resources/geckodriver_win_{}.exe".format(geckodriver_version_win))
        elif 'darwin' in platform.platform():
            browser = webdriver.Firefox(executable_path="../resources/geckodriver_mac_{}".format(geckodriver_version_mac))
        elif 'macOS' in platform.platform():
            browser = webdriver.Firefox(executable_path="../resources/geckodriver_mac_{}".format(geckodriver_version_mac))
        elif 'linux' in platform.platform():
            browser = webdriver.Firefox(executable_path="../resources/geckodriver_linux_{}".format(geckodriver_version_linux))
        else:
            raise Exception("geckodriver is not configured for your Operation System! "
                            "Your Operating System is: {}".format(platform.platform()))
    elif config['browser'] == 'Chrome':
        if 'Win' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_win_{}.exe".format(chrome_version_win))
        elif 'darwin' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac))
        elif 'macOS' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac))
        elif 'linux' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_linux_{}".format(chrome_version_linux))
        else:
            raise Exception("chromedriver is not configured for your Operation System! "
                            "Your Operating System is: {}".format(platform.platform()))
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        if 'Win' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_win_{}.exe".format(chrome_version_win), options=opts)
        elif 'darwin' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac), options=opts)
        elif 'macOS' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac), options=opts)
        elif 'linux' in platform.platform():
            browser = webdriver.Chrome("../resources/chromedriver_linux_{}".format(chrome_version_linux), options=opts)
        else:
            raise Exception("chromedriver is not configured for your Operation System! "
                            "Your Operating System is: {}".format(platform.platform()))
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    browser.maximize_window()
    # Make its calls wait for elements to appear
    browser.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield browser

    # Quit the WebDriver instance for the cleanup
    browser.quit()



