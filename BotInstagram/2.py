from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs")

    def login(self):
        driver = self.driver
        driver.get("https://www.intagram.com")
        time.sleep(4)
        campo_usuario = driver.find_element(By.XPATH, '//input[@name="username"]')
        campo_usuario.send_keys(self.username)
        time.sleep(1)
        campo_senha = driver.find_element(By.XPATH, '//input[@name="password"]')
        campo_senha.send_keys(self.password)
        time.sleep(1)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(6)
            
        botao_agoranao = driver.find_element(By.XPATH, '//button[contains(text(), "Agora não")]')
        botao_agoranao.click()
        time.sleep(5)
        botao_agoranao2 = driver.find_element(By.XPATH, '//button[contains(text(), "Agora não")]') 
        botao_agoranao2.click()
        time.sleep(4)

        #######################################
        hashtag_list = ['tecnologia']

        tag = -1
        #######################################

        for hashtag in hashtag_list:
            tag = tag + 1
            driver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
            time.sleep(20)
            primeira_thumb = driver.find_element(By.CLASS_NAME, '_aagu')
            time.sleep(8)
            primeira_thumb.click()
            time.sleep(12) 
       
            for _ in range(1, 50):
                try:
                    if driver.find_element(By.XPATH, '//div[contains(text(), "Seguir")]'):
                        driver.find_element(By.XPATH, '//div[contains(text(), "Seguir")]').click()
                        time.sleep(20)
                        driver.find_element(By.XPATH, '//div[@class=" _aaqg _aaqh"]').click()
                        time.sleep(40)
                    else:
                        driver.find_element(By.XPATH, '//div[@class=" _aaqg _aaqh"]').click()
                        time.sleep(40)
                except:
                    driver.find_element(By.XPATH, '//div[@class=" _aaqg _aaqh"]').click()
                    time.sleep(40)

                    
        print("Seu código FUNCIONOU!")



lillrussoBot = InstagramBot('numero_telefone', 'senha_instagram')
lillrussoBot.login()
