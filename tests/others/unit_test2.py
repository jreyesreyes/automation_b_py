import unittest
import src.frm_common.browser


class MyTestCase(unittest.TestCase):

    def test_browser(self):
        b = src.frm_common.browser.New('chrome', 'https://talent-platform-fe-staging.herokuapp.com/')
        b.open()
        print(b.current_url())
        title = b.title()
        print(title)
        b.close()
        assert "Talent" in title


if __name__ == '__main__':
    unittest.main()
