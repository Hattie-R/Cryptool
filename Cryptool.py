import os
import pyAesCrypt
from ciphercaesar import encrypt, decrypt
import time


def CT(password):
    print("--------------------")
    for i in os.listdir():
        bufferSize = 512 * 1024
        pyAesCrypt.encryptFile(str(i), str(i) + ".aes", password, bufferSize)
        print("Crypted " + str(i) + ".aes")
        os.remove(i)
        os.rename(str(i) + ".aes", encrypt(i, 10) + ".aes")
        
def DC(password):
    print("--------------------")
    for i in os.listdir():
        try:
            os.rename(i, decrypt(i, 10))
            bufferSize = 512 * 1024
            pyAesCrypt.decryptFile(str(decrypt(i, 10)), str(os.path.splitext(decrypt(i, 10))[0]), password, bufferSize)
            print(str(os.path.splitext(decrypt(i, 10))[0]) + " has been DeCrypted! ")
            os.remove(decrypt(i, 10))
        except ValueError:
            os.rename(decrypt(i, 10), i)
            print('WRONG PASSWORD')

def main():
    print('_________                        __    ___________           .__   \n\_   ___ \_______ ___.__._______/  |_  \__    ___/___   ____ |  |  \n/    \  \/\_  __ <   |  |\____ \   __\   |    | /  _ \ /  _ \|  |  \n\     \____|  | \/\___  ||  |_> >  |     |    |(  <_> |  <_> )  |__\n \______  /|__|   / ____||   __/|__|     |____| \____/ \____/|____/\n        \/        \/     |__|                                      \n')
    dire = input(r'Path: ')
    os.chdir(dire)
    print("The Current working directory now is: {0}".format(os.getcwd()))
    q= input('What to do?\n(1)Encrypt\n(2)Decrypt\n')
    password = input("Enter password: ")
    if q == '1':
        CT(password)
    elif q == '2':
        DC(password)
    else:
        print('incorrect input')

    print(time.process_time())
    input('Enter to exit. ')


if __name__ == "__main__":
    main()
