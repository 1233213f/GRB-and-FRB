import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter


chrome_options = webdriver.ChromeOptions()
url = 'https://swift.gsfc.nasa.gov/results/batgrbcat/'
chrome_options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

grb = ['909','907','901','875','867','865','864','859','857','837','812','805','796','793','792','783','767','761','760','733','726','719','718','710','695','692','691','667','662','633','630','629','623','620','619','615','610','600','594','584','573','569','554','546','523','487','465','455','447','445','440','433','430','416','401','390','383','365','357','347','340','339','317','311','301','284','281','274','263','255','254','215','205','186','179','175','159','149','148','139','102','86','79','64','47','38','36','35','32','19','18','2']
grb1 = ['100111A','100117A','100213A','100522A','100625A','100702A','100704A','100727A','100728B','101023A','110212A','110318A','110420A','110503A','110519A','110715A','111020A','111103B','111107A','120213A','120305A','120326A','120327A','120521A','120729A','120803B','120804A','121027A','121117A','130420A','130427B','130502A','130515A','130521A','130527A','130603B','130609A','130701A','130725B','130831A','131004A','131030A','140102A','140209A','140502A','140903A','141212A','150120A','150212A','150222A','150314A','150403A','150423A','150710A','150831A','151006A','151031A','160119A','160220B','160327A','160419A','160424A','160726A','160821B','161004B','161219B','170101A','170127B','170317A','170419B','170428A','171011A','171211A','180325A','180404B','180418A','180630A','180727A','180728A','180828A','190204A','190604B','190630C','191011A','191221B','200131A','200215A','200216B','200227A','200519A','200522A','200829A']
t=[12.9, 0.3, 2.4, 35.3, 0.33, 0.16, 197.5, 84, 12.1, 80.8, 3.3, 16, 11.8, 10, 27.2, 0.4, 167, 26.6, 48.9, 0.1, 69.6, 62.9, 0.45, 71.5, 37.5, 0.81, 62.6, 30, 123.5, 27, 3, 0.29, 11, 44, 0.18, 7, 4.38, 10, 32.5, 1.54, 41.1, 65, 21.3, 16.9, 0.3, 0.3, 1.2, 11.4, 15.9, 14.79, 40.9, 0.22, 0.15, 1.15, 203.9, 5, 116, 31.4, 28, 8.8, 6.3, 0.7, 0.48, 15.9, 6.94, 2.43, 0.51, 11.94, 77.2, 0.2, 2.27, 2.32, 7.2, 94.1, 111.5, 2.29, 18.85, 1.1, 8.68, 14, 26.4, 220.2, 38.4, 7.37, 48, 32.74, 11.7, 81.3, 32.8, 71.88, 0.62, 13.04]


# time.sleep(1)
for i in range(63, 92):
    driver.get(url)
    if t[i] > 2:

        driver.find_element_by_xpath('//*[@id="section"]/table/tbody/tr['+grb[i]+']/td[4]').click()
        driver.find_element_by_xpath('/html/body/pre/a[6]').click()
        driver.find_element_by_xpath('/html/body/pre/a[15]').click()
        driver.find_element_by_xpath('/html/body/pre/a[15]').click()
        # /html/body/pre/a[15]
        # /html/body/pre/a[14]
    else:
        # /html/body/pre/a[20]
        driver.find_element_by_xpath('//*[@id="section"]/table/tbody/tr[' + grb[i] + ']/td[4]').click()
        driver.find_element_by_xpath('/html/body/pre/a[6]').click()
        driver.find_element_by_xpath('/html/body/pre/a[15]').click()
        driver.find_element_by_xpath('/html/body/pre/a[20]').click()
    driver.save_screenshot(grb1[i]+".png") ### 把网页保存为图片

