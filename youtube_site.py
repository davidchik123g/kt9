import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_search_button(self) -> None:
        self.driver.tap([(895, 344)])
        search_button = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.EditText").instance(0)')
        search_text = "Appium Tutorial"
        search_button.send_keys(search_text)
        time.sleep(2)
        assert search_button.get_attribute("text") == search_text
        self.driver.tap([(55, 358)])

    def test_launch_app(self) -> None:
        main_screen = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.view.View").instance(11)')
        assert main_screen.is_displayed()

    def test_youtube_shorts(self) -> None:
        self.driver.tap([(537, 2276)])
        time.sleep(2)
        shorts_player = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("ytp-caption-window-container")')
        self.driver.tap([(532, 1308)])
        try:
            shorts_player.is_displayed()
            assert False, "YouTube Shorts продолжает воспроизводиться"
        except Exception:
            pass
        self.driver.tap([(41, 340)])

    def test_comments(self) -> None:
        self.driver.tap([(542, 831)])
        time.sleep(4)
        self.driver.tap([(514, 1606)])
        time.sleep(3)
        comment_items = self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.view.View").instance(21)')
        assert len(comment_items) > 0
        self.driver.tap([(1000, 1133)])
        self.driver.swipe(18, 1014, 307, 1014)

    def test_change_video_settings(self) -> None:
        self.driver.tap([(542, 831)])
        time.sleep(3)
        self.driver.tap([(537, 881)])
        time.sleep(1)
        self.driver.tap([(1023, 468)])
        time.sleep(3)
        self.driver.tap([(890, 1225)])
        time.sleep(4)
        current_speed = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                               value='new UiSelector().text("Normal")')
        new_speed = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                               value='new UiSelector().text("1.25")')
        self.driver.tap([(991, 1322)])
        time.sleep(4)
        assert new_speed != current_speed
        self.driver.tap([(858, 1817)])
        self.driver.swipe(18, 1014, 307, 1014)






if __name__ == '__main__':
    unittest.main()
