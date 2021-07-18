import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

nama_aplikasi = "Linbot \n"
versi_aplikasi = "1.0 \n"
tanggal_rilis = "29 Juni 2020 \n"
developed_by = "Ananda Rauf Maududi \n"

print ("--------------------------------------------------------------------------------\n")
print (nama_aplikasi)
print("Version :",versi_aplikasi)
print("Tanggal rilis :",tanggal_rilis)
print("Developed by :",developed_by)
print ("--------------------------------------------------------------------------------\n")
def MenuMarketing():
    print ("Menu pilihan marketing :")
    print
    print ("1. Marketing")
    print ("2. Keluar")

def marketing():
    browser = webdriver.Chrome('webdriver/chromedriver.exe')
    browser.get('https://www.linkedin.com/uas/login')
    file = open('configdataakunlinkend.txt')
    bacafile = file.readlines()
    username = bacafile[0]
    password = bacafile[1]
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username)
    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password)
    elementID.submit()
    kunjungiprofilelinked = open('listtargetmarketing.txt')
    bacatxtprofile = kunjungiprofilelinked.readlines()
    target1 = bacatxtprofile[0]
    browser.get(target1)
    browser.get('https://www.linkedin.com/messaging/thread/new/')
    namatarget = "Ananda Rauf Maududi"
    targetID = browser.find_element_by_id('ember60-search-field')
    targetID.send_keys(namatarget,Keys.ENTER)
    targetID = browser.find_element_by_css_selector('message')
    pesantarget = "Test bot"
    targetID.send_keys(pesantarget)
    targetID.submit()
    
    
    
    



def keluar():
    print("Kamu keluar menu")
    exit()
    print("Selamat datang di Linbot \n")
    print("Terima kasih telah menggunkan program ini ^-^")
MenuMarketing()
pilih = int(input("Silahkan pilih nomor untuk memulai marketing :\n"))

if pilih == 1:
            marketing()
elif pilih == 2:
              keluar()

else :
        print ("Maaf nomor kode barang anda pilih tidak ada")

    
