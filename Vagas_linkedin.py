## 1. Todas as importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from time import sleep

## 2. Todos os parâmetros




## 3. Todas as funções e classes




## 4. Execução do código
if __name__ == '__main__':
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br')
    wait = ui.WebDriverWait(driver, 60)
    
    resultados = driver.find_elements(By.CLASS_NAME, 'base-card__full-link')
    
    lista_descricao = []
    
    for resultado in resultados:
        sleep(2)
        resultado.click()
        wait
        
        try:
            descricao = driver.find_element(By.CLASS_NAME, 'show-more-less-html__markup')
            wait
            if descricao.text == '':
                resultado.click()
                wait
                descricao = driver.find_element(By.CLASS_NAME, 'show-more-less-html__markup')
                wait
        except:
            print('Erro')
            pass
        lista_descricao.append(descricao.text)
        driver.execute_script("arguments[0].scrollIntoView();", resultado)    
    
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt', 'w', encoding="utf-8") as f:
        f.write(descricao_salvar)
    
    driver.quit()
