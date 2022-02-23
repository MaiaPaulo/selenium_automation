
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
login = input("Login: ")
senha = input("Senha: ")
browser = webdriver.Chrome("C:\\Users\paulo.smaia\Downloads\chromedriver_win32(1)\chromedriver.exe")
browser.fullscreen_window()
browser.get('http://www.snirh.gov.br/sso/login.jsf?response_type=code&client_id=rq2a439qzx5hq5i&scope=PROFILE%20PERMISSOES%20RESTRICOES&state=rx9crkVyUJUweT-4XnYa_952Tz2McfCa2Y3wjnyM&ip=10.134.4.2&redirect_uri=http://www.snirh.gov.br/cnarh40/restrito/exportar_dados.jsf')
time.sleep(3)
username = browser.find_element_by_id("login:fs:cpf")
username.send_keys(login)
password = browser.find_element_by_id("login:fs:senha")
password.send_keys(senha)
login_attempt = browser.find_element_by_xpath('/html/body/main/div/div/div/section/form/div[2]/section/footer[1]/input')
login_attempt.click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="menuLateral:menuForm"]/nav/ul/li[1]/a/strong').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="menuLateral:menuForm:menuSection:nInterferencia:exportaDados:link"]/i').click()
time.sleep(10)
browser.find_element_by_xpath('//*[@id="export:p1:componente"]/section/div/div/div[2]/div/div[1]').click()
browser.quit()

#options = webdriver.ChromeOptions()
#prefs = {"download.default_directory" : "C:\\Users\\paulo.smaia\\Documents\\seleniumdownload"
#options.add_experimental_option("prefs",prefs);


