from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://smart-invest.su/user/login")
driver.find_element_by_id('edit-name').send_keys('daria.honcharuk@gmail.com')
driver.find_element_by_id('edit-pass').send_keys('invest1234')
driver.find_element_by_id('edit-submit').click()
titles = driver.find_elements_by_tag_name('h2')
counter = 0
for i in titles:
    i.click()
for i in range(1, (len(titles)) + 1):
    driver.switch_to.window(driver.window_handles[i])
    name = driver.current_url.split('/')[-1]
    with open(f'./templates/{name}.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
        f.close()



