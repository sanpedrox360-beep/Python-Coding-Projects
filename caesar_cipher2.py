#About Caesar encryption and decryption
import random

def crypter(x, k):
    return (x+k)%26

def decrypter(x, k):
    return (x-k)%26

def main():
    caracteres = input("Saisir votre mot/phrase: ")
    caracteres = caracteres.strip()
    print("Quel est votre choix?\n  1-Crypter\n  2-Décrypter")
    choix = input()
    match(choix):
        case "1":
            method = "crypt"
        case "2":
            method = "decrypt"
        case _:
            method = None
            print("Choix invalide")
            return

    if method == "crypt":
        print("Connaissez vous la clé ?")
        cle_connue = input()

        if cle_connue.lower() == "oui":
            cle = int(input("Saisir la clé: "))
        elif cle_connue.lower() == 'non':
            cle = random.randint(0, 25)
        else:
            print("Réponse invalide. Génération d'une clé aléatoire.")
            cle = random.randint(0, 25)

        caracteres_chiffres = ''
        for car in caracteres:
            if car.isalpha():
                if car.isupper():
                    nb = ord(car) - 65
                    nb_crypt = crypter(nb, cle)
                    car_crypt = chr(nb_crypt + 65)
                    caracteres_chiffres += car_crypt
                elif car.islower():
                    nb = ord(car) - 97
                    nb_crypt = crypter(nb, cle)
                    car_crypt = chr(nb_crypt + 97)
                    caracteres_chiffres += car_crypt
            else:
                caracteres_chiffres += car  # keep spaces/punctuation unchanged
        print(f'Caractères chiffrés: {caracteres_chiffres}\nClé: {cle}')

    elif method == 'decrypt':
        print("Connaissez vous la clé ?")
        cle_connue = input()

        if cle_connue.lower() == "oui":
            cle = int(input("Saisir la clé: "))
            caracteres_dechiffres = ''
            for car in caracteres:
                if car.isalpha():
                    if car.isupper():
                        nb = ord(car) - 65
                        nb_decrypt = decrypter(nb, i)
                        car_decrypt = chr(nb_decrypt + 65)
                        caracteres_dechiffres += car_decrypt
                    elif car.islower():
                        nb = ord(car) - 97
                        nb_decrypt = decrypter(nb, i)
                        car_decrypt = chr(nb_decrypt + 97)
                        caracteres_dechiffres += car_decrypt
                else:
                    caracteres_dechiffres += car  # keep spaces/punctuation unchanged
            print(f'Caractères déchiffrés: {caracteres_dechiffres}')
        elif cle_connue.lower() == "non":
            for i in range(26):
                caracteres_dechiffres = ''
                print(f'Avec la clé: {i}')
                for car in caracteres:
                    if car.isalpha():
                        if car.isupper():
                            nb = ord(car) - 65
                            nb_decrypt = decrypter(nb, i)
                            car_decrypt = chr(nb_decrypt + 65)
                            caracteres_dechiffres += car_decrypt
                        elif car.islower():
                            nb = ord(car) - 97
                            nb_decrypt = decrypter(nb, i)
                            car_decrypt = chr(nb_decrypt + 97)
                            caracteres_dechiffres += car_decrypt
                    else:
                        caracteres_dechiffres += car  # keep spaces/punctuation unchanged
                print(f'Caractères déchiffrés: {caracteres_dechiffres}\n')


if __name__ == "__main__":
    main()
