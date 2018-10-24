from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome('./chromedriver.exe')
try:
    driver.implicitly_wait(5)
    driver.get('https://movie.douban.com/top250?tdsourcetag=s_pcqq_aiomsg&qq-pf-to=pcqq.group')
    driver.switch_to.window(driver.current_window_handle)
    # window_list=driver.current_window_handle
    # driver.switch_to.window(window_list)
    while True:
        movies=driver.find_elements_by_css_selector('.grid_view li')
        for movie in movies:
            movie_link=movie.find_element_by_css_selector('.hd a span')
            movie_link.click()
            # driver.switch_to.window(window_list)
            movie_top = driver.find_element_by_css_selector('.top250 span')
            movie_name = driver.find_element_by_css_selector('h1 span')
            movie_degree = driver.find_element_by_css_selector('.rating_self .ll')
            print('排名:', movie_top.text, '影片名称:', movie_name.text, '豆瓣评分：',movie_degree.text)
            driver.close()


        # next_page = WebDriverWait(driver, 5).until(
        #     ec.element_to_be_clickable((By.CSS_SELECTOR, '.article .paginator .next')))
        # next_page_class = next_page.get_attribute('class')
        # if 'next' in next_page_class:
        #     break
        # else:
        #     next_page.click()
        #     time.sleep(3)
finally:
    time.sleep(5)
    driver.quit()


