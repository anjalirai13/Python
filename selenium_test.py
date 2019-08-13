import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
try:
    browser.maximize_window()
    browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    time.sleep(20)
    browser.find_element_by_id('user-message').send_keys("This is automated using Python + Selenium")
    browser.find_element_by_class_name('btn-default').click()
    print(browser.find_element_by_id('display').text)

    # Add two numbers
    browser.find_element_by_id('sum1').send_keys(3)
    browser.find_element_by_id('sum2').send_keys(4)
    browser.find_element_by_xpath("//button[text()='Get Total']").click()
    print(browser.find_element_by_id('displayvalue').text)

    time.sleep(0.5)
    browser.find_element_by_link_text('Input Forms').click()
    browser.find_element_by_link_text('Checkbox Demo').click()
    time.sleep(1)
    browser.find_element_by_id('isAgeSelected').click()
    print(browser.find_element_by_id('txtAge').text)
    time.sleep(0.5)

    browser.find_element_by_id("check1").click()
    time.sleep(0.5)
    browser.find_element_by_link_text('Input Forms').click()
    browser.find_element_by_link_text('Radio Buttons Demo').click()
    time.sleep(3)
    browser.find_element_by_xpath("//input[@value='Female']").click()
    browser.find_element_by_xpath("//button[text()='Get Checked value']").click()
    time.sleep(3)

    browser.find_element_by_xpath("//input[@name='gender' and @value='Male']").click()
    browser.find_element_by_xpath("//input[@name='ageGroup' and @value='0 - 5']").click()
    browser.find_element_by_xpath("//button[text()='Get values']").click()
    print(browser.find_element_by_class_name('groupradiobutton').text)
    time.sleep(3)

    browser.find_element_by_link_text('Input Forms').click()
    browser.find_element_by_link_text('Select Dropdown List').click()
    time.sleep(3)
    select = Select(browser.find_element_by_id('select-demo'))
    select.select_by_value('Tuesday')
    print(browser.find_element_by_class_name('selected-value').text)
    time.sleep(5)
    multi_select = Select(browser.find_element_by_id('multi-select'))
    multi_select.select_by_visible_text('New York')
    browser.find_element_by_id('printMe').click()
    browser.find_element_by_id('printAll').click()
    print(browser.find_element_by_class_name('getall-selected').text)
    time.sleep(3)

    browser.find_element_by_link_text('Input Forms').click()
    browser.find_element_by_link_text('Input Form Submit').click()
    browser.find_element_by_name('first_name').send_keys("Anjali")
    browser.find_element_by_name('last_name').send_keys("Rai")
    browser.find_element_by_name('email').send_keys("xxxx@gmail.com")
    browser.find_element_by_name('phone').send_keys(999999999)
    browser.find_element_by_name('city').send_keys('Unknown Land')
    states = Select(browser.find_element_by_name('state'))
    states.select_by_visible_text('Michigan')
    browser.find_element_by_name('zip').send_keys("1232456")
    browser.find_element_by_name('website').send_keys("earthvader.com")
    browser.find_element_by_xpath("//input[@name='hosting' and @value='no']").click()
    browser.find_element_by_name('comment').send_keys("I need a lot of practice")
    browser.find_element_by_xpath('//button[text()="Send "]').click()
    time.sleep(3)

    browser.find_element_by_link_text('Input Forms').click()
    browser.find_element_by_link_text('Ajax Form Submit').click()
    browser.find_element_by_id('title').send_keys("Getting tired")
    browser.find_element_by_id('description').send_keys("Ufff too much to type")
    browser.find_element_by_id('btn-submit').click()
    time.sleep(5)

    browser.find_element_by_link_text('Input Forms').click()
    browser.find_element_by_link_text('JQuery Select dropdown').click()
    browser.find_element_by_class_name('select2-search select2-search--dropdown').click()
    browser.find_element_by_class_name('select2-search__field').send_keys('India')
    browser.find_element_by_class_name('select2-results__option select2-results__option--highlighted').send_keys(Keys.RETURN)
    time.sleep(10)
except:
    print("Exception Occured")
finally:
    browser.quit()