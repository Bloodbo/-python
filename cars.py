print('1-Volkswagen touareg \n 2-BMW e60 \n 3-Mercedes-benz s-class w221 \n 4-Volvo V70 2 gen \n 5-AUDI A6 C7')
choice = int(input('пожалуйсто сделайте свой выбор:'))
vybor = input('Хотите ли вы посмотреть об данном авто в интернете на рынке Балтии? = ')
import webbrowser
webbrowser.register('Chrome',None,webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
if choice>5:
    print('error')
if choice == 1:
    print('Volkswagen Touareg II – внедорожник 5 дв. E-класса, полный привод. Автомат. Бензиновые, дизельные и гибридные двигатели мощностью от 204 до 360 лошадиных сил.')
    print('одна из самых надежных конфигураций V8 TDI или V6 TDI')
    print('средняя цена в регионах Балтии примерно от 23000 ЕВРО, состоние: б/у')
    if vybor == 'Да' or vybor == 'да':
        print('спасибо/thanks')
        webbrowser.get('Chrome').open_new_tab('https://www.ss.lv/lv/transport/cars/volkswagen/touareg/filter/')
        webbrowser.get('Chrome').open_new_tab('https://www.drom.ru/catalog/volkswagen/touareg/2013/')
if choice == 2:
    print('Поколение E60 представило различные новые электронные функции, \n в том числе информационно-развлекательную систему iDrive, проекционный дисплей, активный круиз-контроль, активное рулевое управление, адаптивные фары, ночное видение, предупреждение о выходе из полосы движения и голосовое управление. \n E60 был первым автомобилем 5-й серии, который был доступен с бензиновым двигателем с турбонаддувом, \n 6-ступенчатой ​​автоматической коробкой передач и рекуперативным торможением.')
    print('одна из надежных конфигураций по мнению бмв клаб 530d')
    print('средняя цена в регионах Балтии: 5895 euro')
    if vybor == 'Да' or vybor == 'да':
        print('спасибо/thanks')
        webbrowser.get('Chrome').open_new_tab('https://www.ss.lv/lv/transport/cars/bmw/5-series/filter/')
        webbrowser.get('Chrome').open_new_tab('https://www.drom.ru/catalog/bmw/5-series/g_2007_5139/')
if choice == 3:
    print('Линейка S-Class W221 2005-2009 гг. включает несколько модификаций с бензиновыми и дизельными моторами V6, V8 и V12 мощностью от 272 до 612 л.с.')
    print('одна из надёжных  конфигураций 320 dci, в этом поколении получились фатально неудачными бензиновые двигатели,хотя они дарят эмоции от управление и контроля авто')
    print('\n средняя цена в регионах Балтии: 1200 EUR')
    if vybor == 'Да' or vybor == 'да':
        print('спасибо/thanks')
        webbrowser.get('Chrome').open_new_tab('https://www.ss.com/lv/transport/cars/mercedes/s-class/')
        webbrowser.get('Chrome').open_new_tab('https://www.drom.ru/catalog/mercedes-benz/s-class/g_2005_5273/')
if choice == 4:
    print('После небольшого изменения внешнего вида \n универсал Volvo V70 второго поколения получил модифицированную переднюю часть: решетку радиатора, переднюю оптику, бампер. \n Минимальной реконструкции подверглась задняя часть. Внутри обновилась центральная консоль и панель приборов, автомобиль получил измененную обивку сидений, включая высококачественную кожу, а также новые варианты индивидуализации. \n В арсенале силовых агрегатов появился новый пятицилиндровый бензиновый двигатель 2.4 T5, мощность которого составляет 260 л.с. ')
    print('Конечно же конфигурация D5 одна из самых НЕ проблемных')
    print('\n средняя цена в регионах Балтии: 2350 EUR')
    if vybor == 'Да' or vybor == 'да':
        print('спасибо/thanks')
        webbrowser.get('Chrome').open_new_tab('https://www.ss.com/lv/transport/cars/volvo/v70/filter/')
        webbrowser.get('Chrome').open_new_tab('https://auto.ru/catalog/cars/volvo/v70/4602617/4602618/')
if choice == 5:
    print('Audi A6 IV (C7) Рестайлинг – седан E-класса, передний и полный привод. Механика, робот и автомат. \n Бензиновые и дизельные двигатели мощностью от 150 до 333 лошадиных сил')
    print('одни из самых надежных конфигураций 2.0 tdi на автомате и 3.0 TDI')
    print('\n средняя цена в регионах Балтии: 17118 EUR')
    if vybor == 'Да' or vybor == 'да':
        print('спасибо/thanks')
        webbrowser.get('Chrome').open_new_tab('https://www.ss.com/lv/transport/cars/volvo/v70/filter/')
        webbrowser.get('Chrome').open_new_tab('https://auto.ru/catalog/cars/volvo/v70/4602617/4602618/')
