import random
from termcolor import colored
from colorama import init
from opening import welcome
init()
welcome()
# opening = "WELCOME TO THE GAME"
# border = "="*25
# border_side = "|"*2
# print(f"{colored(border,color='black')}\n{colored(border_side,color='black')} {colored(opening,color= 'light_magenta')} {colored(border_side,color='black')}\n{colored(border, color='black')} ")

while True:
    main = input("kamu mau main game? [y/n] ")
    if main == "y":
        break
    elif main == "n":
        exit()
    else:
        print("validasi yang anda masukan salah, silahkan coba lagi!")


nama = input("masukan nama anda: ")
while nama == "":
    nama = input("masukan nama anda: ")
print(f"\nhalo {colored(nama,color='blue')}, mau main game apa?")


while True:
        pilihan_game = str(input("1. CuyPY\n2. Tebak Angka\n\nsilahkan pilih mau nomor berapa? ")) 

        if pilihan_game == "1":
            print(f"anda memilih {pilihan_game}. CuyPY, selamat bermain!!\n")
            cuypy_position = random.randint(1,4)
            bentuk_goa = "[_]"
            cuypy = "0_0"
            goa_kosong = [bentuk_goa]*4
            goa = goa_kosong.copy()
            goa_join = " ".join(goa)
            goa[cuypy_position-1] = (f"[{colored(cuypy, color='light_red')}]")
            goa_join1 = " ".join(goa)
            while True:
                game_1 = str(input(f"CuyPY sedang bersembunyi disebuah goa, di goa manakah CuyPY bersembunyi?\n{goa_join}\n 1   2   3   4\ngoa nomor berapa yang mau anda pilih: "))
                while game_1 == "":
                    game_1 = str(input(f"silahkan baca teks di bawah ini\nCuyPY sedang bersembunyi disebuah goa, di goa manakah CuyPY bersembunyi?\n{goa_join}\n 1   2   3   4\ngoa nomor berapa yang mau anda pilih: "))
                while True:
                    konfirmasi = str(input("apakah anda yakin dengan jawaban itu? [y/n]\n"))

                    if konfirmasi == "y":
                        break
                    elif konfirmasi == "n":
                        print("silahkan pilih kembali jawaban anda! ")
                        break                
                    else:
                        print("validasi yang anda masukan salah, silahkan coba lagi!\n")

                if konfirmasi == "y":
                    break

            if game_1 == str(cuypy_position):
                print(f"selamat anda benar, cuypy berada di posisi {cuypy_position}\n{goa_join1}")
            else:
                print(f"jawaban anda salah, cuypy berada di posisi {cuypy_position}\n{goa_join1}")
            break
        
        elif pilihan_game == "2":
            print(f"anda memilih {pilihan_game}. Tebak Angka, selamat bermain!!\n")
            
            angka = random.randint(1,4)
        
        
            while True:
                game_2 = str(input("tebak angka berapakah yang cuypy punya? \njawaban anda : "))
                while game_2 == "":
                    game_2 = str(input("tebak angka berapakah yang cuypy punya? \njawaban anda :"))
                
                while True:                
                    konfirmasi = str(input("apakah anda yakin dengan jawaban anda? [y/n]\n"))
                    
                    if konfirmasi == "y":
                        break
                    elif konfirmasi == "n":
                        print("silahkan coba lagi!\n")
                        break
                    else:
                        print("validasi yang anda masukan tidak valid, silahkan masukan kembali dengan benar!")
                if konfirmasi == "y":
                    break

            if game_2 == str(angka):
                print(f"selamat anda benar!, angka yang cuypy miliki adalah {colored(angka, color='light_red')}")

            else: 
                print(f"salah, angka yang cuypy miliki adalah {colored(angka, color='light_red')}")
                break
        else:
            print("validasi anda tidak valid, silahkan coba lagi!")
            continue

thanks = colored("\nTerimakasih Sudah Bermain Game Di sini",color='yellow')    
print(thanks)
input()