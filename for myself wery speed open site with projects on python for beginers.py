import webbrowser
webbrowser.register('Chrome',None,webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
webbrowser.get('Chrome').open_new_tab('https://www.dataquest.io/blog/python-projects-for-beginners/')
print('вы переадресованы на забугорный сайт для проектов для новичков в языке программировании питон')