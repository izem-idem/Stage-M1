#voir la video1
import webbrowser
import selenium
import sys
import os
from selenium import webdriver
#voir la video 2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Firefox a besoin d'un geckodriver.

driver_loc="/usr/bin/chromedriver" # voir la vidéo1
binary_loc="/usr/bin/google-chrome"
option= webdriver.ChromeOptions()
option.binary_location=binary_loc

'''import csv
f = open("/home/izemmouhoubi/Documents/SraRunTable.csv")
csv_f = csv.reader(f)
f.close()
carac=[]
for row in csv_f:
    if row[2] == "WGS":
        carac.append(row[0])

stringer=""
for x in carac:
    stringer=stringer+" or "+x

chaine=stringer[4:]

'''
chaine=""

try:
    if sys.argv[1].find("SRR") == -1:
        print("veuillez entrer un SRR svp")

    elif sys.argv[1].find("SRR") == 0 and len(sys.argv[1])>5: # vérifie que c'est bien un SRR
        chaine=sys.argv[1]
        driver = webdriver.Chrome(executable_path=driver_loc,options=option)
        driver.get("https://www.ncbi.nlm.nih.gov/sra/?term="+chaine)
        project_button= driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div[5]/div/div[5]/div/div[1]/div[2]/span/div[1]/a[1]")
        project_name = str(project_button.get_attribute('href')).split("/")[4] #je recupére le prjna en question.
        time.sleep(1)
        driver.get("https://sra-explorer.info/")
        textbar = driver.find_element_by_xpath("//*[@id=\"searchText\"]")
        search_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[1]/div/div/div[2]/button")
        textbar.send_keys(project_name) #tu remplis la barre
        time.sleep(2)
        search_button.click()# tu clique
        time.sleep(2) #on attend que le 1er resultat se charge
        seq_button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/table/thead/tr/th[1]/input").click()
        collect_button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/button").click()
        time.sleep(2)
        caddy_button = driver.find_element_by_xpath("/html/body/div[1]/div/a[2]").click()
        time.sleep(2)
        delie_button= driver.find_element_by_xpath("//*[@id=\"fastqAccordion\"]/div[1]/div[1]/h4/a").click()
        time.sleep(30)
        download_button =driver.find_element_by_xpath("//*[@id=\"fastqURLs\"]/div/p[2]/button[2]").click()
        time.sleep(3)
        sra_button= driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/ul/li[2]/a").click()
        time.sleep(2)
        delie_sra_button=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/h4/a").click()
        time.sleep(2)
        download_sra_button=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div/p[2]/button[2]").click()
        print("process terminé")
        driver.close()
        driver.quit()
        choix = input("combien de SRR voulez vous télecharger (one/all/2-X)? :")
        type= input("vous voulez télecharger le fastq ou bien le sra (fq / sra) ? :")
        try:
            os.mkdir("Downloads")
        except:
            print("le dossier existe déja")
        if choix == "one":
            if type == "fq":
                f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_fastq_urls.txt")
                lines=f.readlines()
                f.close()
                for line in lines:
                    if line.split("/")[7] == chaine:
                        os.chdir("Downloads")
                        os.system("wget "+line)
                        os.chdir("..")
                    break
                print("telechargement terminé !")
            elif type =="sra":
                f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_sra_urls.txt")
                lines=f.readlines()
                bigstring=[]
                f.close()
                for line in lines:
                    if line.split("/")[10] == chaine:
                        os.system("wget "+line)
                    break
                print("telechargement terminé !")
        elif choix == "all":
            if type == "fq":
                f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_fastq_urls.txt")
                lines=f.readlines()
                f.close()
                for line in lines:
                    os.chdir("Downloads")
                    os.system("wget "+line)
                    os.chdir("..")
                print("telechargement terminé !")
            elif type == "sra":
                f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_sra_urls.txt")
                lines=f.readlines()
                f.close()
                for line in lines:
                    os.system("wget "+line)
                print("telechargement terminé !")
        else:
            if type == "fq":
                f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_fastq_urls.txt")
                lines=f.readlines()
                f.close()
                count=0
                for line in lines:
                    if count == choix:
                        break
                    else:
                        os.chdir("Downloads")
                        os.system("wget "+line)
                        count+=1
                        os.chdir("..")
            elif type == "sra":
                f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_sra_urls.txt")
                lines=f.readlines()
                f.close()
                count=0
                for line in lines:
                    if count == choix:
                        break
                    else:
                        os.system("wget -L "+line)
                        count+=1
                    break
                print("telechargement terminé ! ")

except:
    print("veuillez insérer un SRR valide")

#y= WebDriverWait(driver,WAIT_ELE).until(EC.presence_of_element_located(By.XPATH))  #permet d'attendre que la page se charge pour éviter que ton code se crash si la page est lente au chargment (les instruc ne seront pas faites)
#outer= y.get_attribute("outerHTML")
#print("outerHTML")
#webbrowser.open("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR930/008/SRR9307278/SRR9307278_1.fastq.gz",new=0)

reponse=input("voulez vous créer les scripts Magic Blast(yes/no)?:")
import MagicBlast
if reponse == "no":
    print("vous trouverez vos fichiers dans le dir suivant"+ os.getcwd())
elif reponse == "yes":
    print("création des fichiers Blast")
    f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_sra_urls.txt")
    lines=f.readlines()
    f.close()
    bigstring=[]
    #malade=['SRR6449156', 'SRR6449157', 'SRR6449158', 'SRR6449159', 'SRR6449160', 'SRR6449161', 'SRR6449162', 'SRR6449163', 'SRR6449164', 'SRR6449165', 'SRR6449166', 'SRR6449167', 'SRR6449168', 'SRR6449169', 'SRR6449170', 'SRR6449171', 'SRR6449172', 'SRR6449173', 'SRR6449174', 'SRR6449175', 'SRR6449176', 'SRR6449177', 'SRR6449178', 'SRR6449179', 'SRR6449180', 'SRR6449181', 'SRR6449182', 'SRR6449183', 'SRR6449184', 'SRR6449185', 'SRR6449186', 'SRR6449187', 'SRR6449188', 'SRR6449189', 'SRR6449190', 'SRR6449191', 'SRR6449192', 'SRR6449193', 'SRR6449194', 'SRR6449195', 'SRR6449196', 'SRR6449197', 'SRR6449198', 'SRR6449199', 'SRR6449200', 'SRR6449201', 'SRR6449202', 'SRR6449203', 'SRR6449204', 'SRR6449205', 'SRR6449206', 'SRR6449207', 'SRR6449208', 'SRR6449209', 'SRR6449210', 'SRR6449211', 'SRR6449212']
    for line in lines:
        code=line.split("/")[10]
        bigstring.append(code)
    MagicBlast.writemagicblast(bigstring)
    MagicBlast.writeunmapped(bigstring)

djaweb=input("Voulez-vous créer les fichers de conversion bam ? (yes/no):")
if djaweb=="no":
    print("process terminé")
else:
    print("création des fichiers de conversion bam ...")
    import convert
    f=open("/home/izemmouhoubi/Téléchargements/sra_explorer_sra_urls.txt")
    lines=f.readlines()
    f.close()
    bigstring=[]
    for line in lines:
        code=line.split("/")[10]
        bigstring.append(code)
    convert.convertobam(bigstring)

idjaba=input("voulez vous transférer vos script de conversion sur le cluster genologin (entrer adresse / no): ")
if idjaba == "no":
    print("process terminé")
else:
    print("début du transfert des fichiers sur le répértoire: "+idjaba)
    os.system("rsync -avzP /home/izemmouhoubi/IdeaProjects/WGS/pathseq_script/ adossantos@genologin.toulouse.inra.fr:"+idjaba)











