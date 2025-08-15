import webbrowser
webbrowser.register('Chrome',None,webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
print('1-BBC \n 2-coinmarketcap \n 3-itstep')
vybor=int(input('сделайте свой выбор:'))
if vybor==2:
    webbrowser.get('Chrome').open_new_tab('https://coinmarketcap.com/ru/rankings/exchanges/')
    print('спасибо,что сделали свой выбор вы переадресованы на криптобиржу.')
if vybor==1:
    webbrowser.get('Chrome').open_new_tab('https://www.bbc.com')
    print('спасибо,что сделали свой выбор вы переадресованы на независимый источник новостей BBC.')
if vybor==3:
    webbrowser.get('Chrome').open_new_tab('https://mystat.itstep.org/ru/main/dashboard/page/index')
    print('спасибо,что сделали свой выбор вы переадресованы на международную Акадеимию ШАГ.')
if vybor>3:breakpoint









# webbrowser.open('https://mystat.itstep.org/ru/main/dashboard/page/index', new=1, autoraise=True) #comments открывает шаг в интернет експолорере
