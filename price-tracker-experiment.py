from selenium import webdriver
from selenium.webdriver.common.keys import Keys

norma_browser = webdriver.Chrome('/Users/leonsick/Desktop/Developer/Webautomation Chrome/ChromeDriver/chromedriver')
aldi_browser = webdriver.Chrome('/Users/leonsick/Desktop/Developer/Webautomation Chrome/ChromeDriver/chromedriver')
rewe_browser = webdriver.Chrome('/Users/leonsick/Desktop/Developer/Webautomation Chrome/ChromeDriver/chromedriver')

#browser.get(url='https://www.amazon.de/')
#searchBar = browser.find_element_by_id('twotabsearchtextbox')
#searchBar.send_keys('Macbook Pro 16 Zoll')
#searchBar.send_keys(Keys.ENTER)

## Hackfleisch Preisvergleich
print("Hackfleisch Preisvergleich")
norma_browser.get('https://www.norma-online.de/de/angebote/ab-freitag,-06.03.20/wochenend-spezial-t-109464/rinder-hackfleisch-i-110253/')
norma_price = norma_browser.find_element_by_xpath('//*[@id="js-checkregio"]/div[1]/div/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li').text
norma_size = norma_browser.find_element_by_xpath('//*[@id="js-checkregio"]/div[1]/div/div[2]/div[1]/div[3]/div/div/div[1]').text
print("Norma Preis:" + norma_price + ", Norma Größe:" + norma_size)

aldi_browser.get('https://www.aldi-sued.de/de/sortiment/lebensmittel/frischfleisch/detailseite/ps/p/meine-metzgereihackfleisch-vom-rind/')
aldi = aldi_browser.find_element_by_xpath('//*[@id="c1276013"]/div/div[2]/div[2]/div/span[7]').text
print("Aldi Preis:" + aldi + ", Aldi Größe: 500g")

rewe_browser.get('https://shop.rewe.de/p/wilhelm-brandenburg-rinderhackfleisch-500g/2969360')
rewe = rewe_browser.find_element_by_xpath('//*[@id="pdr-product-details-component"]/section/div[1]/div[3]/div[1]/div[1]/div/div/mark').text
print("Rewe Preis:" + rewe + ", Rewe Größe: 500g")

#browser.get('https://www.selenium.dev')
#links = browser.find_element_by_link_text('Downloads')
#links.click()
#doc = browser.find_element_by_link_text('documentation')
#doc.click()

#elem.click()
#wasserpegel = browser.find_element_by_id('text-3')
#wasserpegel.click()
#elem_href = elem.get_attribute('href')
#print(elem_href)

