import time
import pyfiglet


NAMA_KAMUH = 'AKU SIAPA'
SANDI_QMUH_SYG = 'AKU DIMANA'

def logincuy():
    usrcuy = str(input('affh bhs prtamah qmuh : '))
    if usrcuy.lower() == NAMA_KAMUH:
        hncrcuy = str(input('sffah pirst krusxh kmuhh : '))
        if hncrcuy.lower() == SANDI_QMUH_SYG:
            anjay_alok()
        else: print(pyfiglet.figlet_format('LU SIAPA KONTOL, NGAPAIN ANJING'))
        time.sleep(1000)
    else: print(pyfiglet.figlet_format('LU SIAPA KONTOL, NGAPAIN ANJING')) 
    time.sleep(1000)

def anjay_alok():
    kata_kata = pyfiglet.figlet_format('KONTOl')
    print(kata_kata)
    time.sleep(100)

logincuy()