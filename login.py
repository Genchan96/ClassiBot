import requests 
from selenium import webdriver
from time import sleep
import codecs
import discord
from discord.ext import tasks
from datetime import datetime 
import asyncio

client = discord.Client()

channel_sent = None
#browser = webdriver.Chrome(executable_path=r'C:\Users\chromedriver.exe')
# PhantomJSのドライバー取得
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)
loginUrl= "https://sas.benesse.ne.jp/classi/s/"
browser.get(loginUrl)

username = "SASSI1940874278"
password = "5456crzz"

userNameField = browser.find_element_by_xpath("//*[@id='student_form']/div/div[1]/input")
userNameField.send_keys(username)

passwordField = browser.find_element_by_xpath("//*[@id='usr_password']")
passwordField.send_keys(password)

submitButton = browser.find_element_by_xpath("//*[@id='student_form']/div/button")
submitButton.click()

profile = "https://platform.classi.jp/group2/?year=2021"
browser.get(profile)

url = "https://platform.classi.jp/group2/?year=2021"
# URLの読み込み
browser.get(url)
for i in range(1):
    bc_value = browser.find_element_by_xpath("/html/body/section/div/div/div/section[2]/div[1]/div[2]/message-editable-box/div/group-message-content/div/div/div").text
    
    print(bc_value)
# ブラウザ終了
browser.quit()


#定期実行時間1時間←これ同じ文章繰り返すだけ説でもなんか関数外すと動かないからとりまこのまま

@tasks.loop(seconds=3600)
async def send_message_every_3600sec():
    await channel_sent.send("**【Classiに新しい投稿がありました】**\r\n"+bc_value + "https://platform.classi.jp/group2/?year=2021")
    f = open('test.txt', 'w')

    f.write(bc_value)

    f.close()
@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(780378057469853752)
    send_message_every_3600sec.start() #定期実行するメソッドの後ろに.start()をつける
#bot起動
client.run("トークン")




