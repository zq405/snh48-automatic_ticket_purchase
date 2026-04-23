#商城地址 https://shop.48.cn/Tickets
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

options = Options()
options.page_load_strategy = "none"

ha = webdriver.Chrome(options=options)
wait = WebDriverWait(ha, 15)

ha.get('https://shop.48.cn/tickets/item/8004') #引号里更换想购买的公演场次
time.sleep(5)


登录=ha.find_element(By.XPATH,'//*[@id="addcart"]/div/div[3]/div[1]/ul/li[3]/span/a')
登录.click()

time.sleep(5)

密码=ha.find_element(By.XPATH,'//*[@id="login"]/div[1]/div/div[1]/div/ul/li[1]/a')
密码.click()

username=ha.find_element(By.NAME,'username')
username.send_keys('用户名') 

password = ha.find_element(By.NAME, 'password')
password.send_keys('密码')


登录1 = ha.find_element(By.XPATH, '//*[@id="loginbtn2"]')
登录1.click()
time.sleep(5)

位置=ha.find_element(By.XPATH,'//*[@id="seattype4"]')#座位选择,把数字改为想要的位置,VIP:1, 站票:4,座票:3
位置.click()

buy_btn=ha.find_element(By.XPATH,'//*[@id="buy"]')
ha.execute_script("arguments[0].click();", buy_btn) #点击购买
'''
#等待
click_time = 0
target_time = datetime.datetime(2026, 4, 23, 19, 20, 0)

print("开始等待抢票时间...")

while True:

    # 已成功点击就退出
    if click_time > 0:
        break

    now = datetime.datetime.now()

    # 时间未到：低频等待
    if now < target_time:
        time.sleep(0.2)
        continue

    # 时间到了：开始高频抢
    try:
        buy_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="buy"]'))
        )

        ha.execute_script("arguments[0].click();", buy_btn)

        click_time += 1
        print("✅ 抢票成功")
        break

    except Exception as e:
        # 失败继续抢，不退出
        time.sleep(0.05)
        continue
'''
