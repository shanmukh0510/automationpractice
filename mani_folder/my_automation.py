from selenium import webdriver

locators = {
        "test_config": "//*[text()='Test Configuration']",
        "create_proj": "//span[@class='project-name-label cursorPointer']",
        "input_project": "//input[@placeholder='New Project name']",
        "pre_compliance": "//label[contains(text(), 'Pre-Compliance')]",
        "power_profile": "//label[text()='PowerProfile']/following-sibling::select",
        "supported_spec": "//label[text()='SupportedSpecification']/following-sibling::select",
        "get_default_sdf_r": "//input[@id='uploadType' and @name='uploadType' and @type='radio']",
        "get_default_sdf": "//button[@class='grl-button' and text()='Get Default ESDF']",
        "create_project": "//button[@class='grl-button' and text()='Create Project']",
        "test_case_count": "//div[@class='testCaseSelectionCount']"
    }
class DriverInti:
    def __init__(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

class WebUI:
    obj = DriverInti()
    url = "http://localhost:2004/"
    test_config_btn = "//span[text()='Test Configuration']"