


print('Rumus Bangun Ruang Bola ⚽')

def volume_bola():
    print("Menghitung Volume Bola !")
    r = float(input("Masukan Jari Jari Bola : "))
    v = 4/3 * 3.14 *(r**3)
    print('\n','--','Volume : ',v)

def luas_permukaan():
    print("Mencari Luas Permukaan !")
    r = float(input("Masukan Jari-Jari Bola : "))
    l = 4 * 3.14 * (r**2)
    print('\n','--',"Luas Permukaan : ",l)

def setengah_volume():
    print("Mencari Volume Setengah Bola !")
    r = float(input("Masukan Jari-Jari Bola : "))
    if r % 7 == 0:
        vs = (2/3 * 22/7) * (r**3)
        print('\n','--',"Volume 1/2 Bola : ",vs)
    else:
        vs = (2/3 * 3.14) * (r**3)
        print('\n','--',"Volume 1/2 Bola : ",vs)

def setengah_luas():
    print('Mencari Luas Permukaan Setengah Bola !')
    r = float(input('Masukan Jari-Jari : '))
    l = (2 * 22/7) * (r**2)
    print('\n','--','Luas Setengah Bola : ',l)

while True:
    userInput = int(input(
        '\n\nPilih Rumus : \n\n1.Volume Bola\n2.Luas Permukaan Bola\n3.Volume Setengah Bola\n4.Luas Setengah Bola\n0.Keluar Program\n\nPilih : '))
    if(userInput == 1):
        volume_bola()
    elif(userInput == 2):
        luas_permukaan()
    elif(userInput == 3):
        setengah_volume()
    elif(userInput == 4):
        setengah_luas()
    else:
        break