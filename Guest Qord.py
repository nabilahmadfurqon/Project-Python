import random

def tebak_kata():
    kata_kata = ['python', 'programming', 'openai', 'chatgpt', 'machinelearning']
    kata = random.choice(kata_kata)
    kesempatan = 3 

    print(f"Ini kata-kata yang bisa kalian tebak: {', '.join(kata_kata)}")
    print("Selamat datang di permainan Tebak Kata!")
    print(f"Anda memiliki {kesempatan} kesempatan untuk menebak kata.")

    while kesempatan > 0:
        tebakan = input("Masukkan tebakan kata: ").lower()
        
        if tebakan == kata:
            print("Selamat! Anda berhasil menebak kata:", kata)
            return
        else:
            kesempatan -= 1 
            print("Tebakan salah! Kesempatan tersisa:", kesempatan)

    print("Anda kehabisan kesempatan! Kata yang benar adalah:", kata)

tebak_kata()
