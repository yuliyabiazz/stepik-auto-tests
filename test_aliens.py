import pytest
import time
import math
from selenium import webdriver

@pytest.mark.parametrize('lesson', ["236895","236896","236897","236898",
                                    "236899","236903","236904","236905"])
def test_guest_fill_in_correct_answer(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    browser.find_element_by_css_selector("button.submit-submission").click() 

    optional = browser.find_element_by_tag_name("pre").text
        
    assert optional == "Correct!", "Answer is not correct."

