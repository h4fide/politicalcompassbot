import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")

url = 'https://www.politicalcompass.org/test/en'


answers = [
    {1: 1, 2:2, 3:3, 4:0, 5:1, 6:2, 7:3},
    {1: 1, 2:2, 3:3, 4:0, 5:1, 6:2, 7:3, 8:0, 9:1, 10:2, 11:3, 12:0, 13:1, 14:2},
    {1: 1, 2:2, 3:3, 4:0, 5:1, 6:2, 7:3, 8:0, 9:1, 10:2, 11:3, 12:0, 13:1, 14:2, 15:3, 16:0, 17:1, 18:2},
    {1: 1, 2:2, 3:3, 4:0, 5:1, 6:2, 7:3, 8:0, 9:1, 10:2, 11:3, 12:0},
    {1: 1, 2:2, 3:3, 4:0, 5:1},
    {1: 1, 2:2, 3:3, 4:0, 5:1, 6:2}]


qinpage = [
    {'page_1': 7}, {'page_2': 14}, {'page_3': 18},
    {'page_4': 12},{'page_5': 5}, {'page_6': 6}]


def format_answers(answers: list):
    newans = []
    pg1 = {1:answers[0][1], 2:answers[1][2], 3:answers[2][3], 4:answers[3][4], 5:answers[4][5], 6:answers[5][6], 7:answers[6][7]}
    pg2 = {1:answers[7][8], 2:answers[8][9], 3:answers[9][10], 4:answers[10][11], 5:answers[11][12], 6:answers[12][13], 7:answers[13][14], 8:answers[14][15], 9:answers[15][16], 10:answers[16][17], 11:answers[17][18], 12:answers[18][19], 13:answers[19][20], 14:answers[20][21]}
    pg3 = {1:answers[21][22], 2:answers[22][23], 3:answers[23][24], 4:answers[24][25], 5:answers[25][26], 6:answers[26][27], 7:answers[27][28], 8:answers[28][29], 9:answers[29][30], 10:answers[30][31], 11:answers[31][32], 12:answers[32][33], 13:answers[33][34], 14:answers[34][35], 15:answers[35][36], 16:answers[36][37], 17:answers[37][38], 18:answers[38][39]}
    pg4 = {1:answers[39][40], 2:answers[40][41], 3:answers[41][42], 4:answers[42][43], 5:answers[43][44], 6:answers[44][45], 7:answers[45][46], 8:answers[46][47], 9:answers[47][48], 10:answers[48][49], 11:answers[49][50], 12:answers[50][51]}
    pg5 = {1:answers[51][52], 2:answers[52][53], 3:answers[53][54], 4:answers[54][55], 5:answers[55][56]}
    pg6 = {1:answers[56][57], 2:answers[57][58], 3:answers[58][59], 4:answers[59][60], 5:answers[60][61], 6:answers[61][62]}
    for i in range(1,7):
        newans.append(eval('pg'+str(i)))
    return newans

def wait_for_page_load(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='fr']")))
    
def answer_questions(driver, page: int, answers: list):
    wait_for_page_load(driver)
    q = driver.find_elements_by_xpath("//div[@class='fr']")
    print(f'Page {page+1}')
    for j in range(len(q)):
        i = q[j]   
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='fr']"))
            )

            elem = f".//input[@value='{answers[page][j+1]}']"
            i.find_element_by_xpath(elem).click()
        finally:
            print('Question: ', j+1, 'Answered')        
    driver.find_element_by_xpath("//button[@type='submit']").click()


def results(answers: list): 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    for k in range(len(answers)):
        answer_questions(driver, k, answers)
    current_url = driver.current_url.split('?')[1]
    print(current_url)
    driver.quit()
    return current_url
