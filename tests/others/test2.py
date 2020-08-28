from src.frm_common.browser import Browser

b = Browser('chrome', 'https://talent-platform-fe-staging.herokuapp.com/')
b.open()
print(b.current_url())
print(b.title())
assert "Talent" in b.title()
b.close()


