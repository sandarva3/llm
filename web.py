from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


# print(f"The driver is: {driver}")
# print(f"The webdriver is: {webdriver}")
# print(f"The webdriver.Chrome is: {webdriver.Chrome()}")


def goto(name):
    driver.get(f"https://{name}.ai")
    print("Went to the website.")
    time.sleep(7)
    text_area = driver.find_element(By.ID, "chat-input-box")
    text_area.send_keys("Reply in very short and concise.")
    print("LOADING...")
    time.sleep(4)
    while True:
        sen = input("YOU: ")

        # for i in sen:
        #     text_area.send_keys(i)
        #     time.sleep(0.01)
        text_area.send_keys(sen)

        #print("Typed the sentence.")
        #time.sleep(1)
        print("  ")
        print("  ")
        # text_area.send_keys("Trying to send you some text.")
        # button = driver.find_element(By.CSS_SELECTOR, "button.bg-primary:last-of-type")
        # print("Clicking the button")
        # time.sleep(3)
        # button.click()
        #print("Pressing Enter.")
        text_area.send_keys(Keys.ENTER)
        # a = input("Enter 1 to exit: ")
        # if a == 1:
        #     driver.quit()
        #     break
        # print("Sleeping.")
        time.sleep(7)

        ai = driver.find_elements(By.CSS_SELECTOR, r"p.mb-2.last\:mb-0:last-child")
        response = ai[-1].text
        print("BOT: ", end="")
        for i in response:
            print(i, end="", flush=True)
            time.sleep(0.03)
        print("  ")
        print("  ")
        # for i in response:
        #     print(response, end="")
        #     time.sleep(0.02)

url = "blackbox"
goto(url)
