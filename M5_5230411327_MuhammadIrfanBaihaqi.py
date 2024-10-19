allSong = []
indo = []
jawa = []
english = []
liststr = []
totalmusic = 0
# daftarpenyanyi = []

class Music:
    # totalmusic = 0
    def __init__(self, judul, penyanyi, genre) -> None:
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    @staticmethod
    def tampilMusic():
        no = 1
        print("DAFTAR MUSIC KESELURUHAN")
        # print(f"TOTAL MUSIC : {totalmusic}")
        for i in liststr:
            print(f"{no}. {i[0]} - {i[1]} - {i[2]}")
            no += 1
        

    @staticmethod
    def cariMusic():
        try:
            HapusBerdasarPenyanyi = input("Masukkan Penyanyi yang akan dihapus musiknya : ")
            for i in allSong:
                if HapusBerdasarPenyanyi == i.penyanyi:
                    print(f"{i.judul} - {i.penyanyi} - {i.genre}")
        except:
            print(f"Music dengan penyanyi tersebut tidak ada")


class Indo(Music):
    def __init__(self,judul,penyanyi,genre) -> None:
        super().__init__(judul,penyanyi,genre)

    @staticmethod
    def tampilMenu():
        print("===========Indonesian Song==========")
        print("1, Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")

    @staticmethod
    def display():
        print("DAFTAR MUSIC Indo")
        no = 1
        for music in indo:
            print(f"{no}. {music.judul} - {music.penyanyi} - {music.genre}")
            no+=1

    @staticmethod
    def addMusic():
        judul = input("Masukkan Judul Music: ")
        penyanyi = input("Masukkan Penyanyi: ")
        genre = "Indo"
        baru = [judul, penyanyi, genre] #SIAP DEBUG
        liststr.append(baru)
        objek = "" #siap debug
        objek = Indo(judul, penyanyi, genre)
        indo.append(objek)
        allSong.append(objek)
        # indo.sort()
        # allSong.sort()
        # totalmusic += 1
        # daftarpenyanyi.append(penyanyi)

    @staticmethod
    def deleteMusic():
        try:
            hapusJudul = input("Masukkan Judul music yang ingin dihapus: ")
            indo.remove(hapusJudul)
            allSong.remove(hapusJudul) 
            for i in len(liststr):
                if i[0] == hapusJudul:
                    liststr.pop(i)
            # indo.sort()
            # allSong.sort()
            # daftarpenyanyi.remove() #SIAP DEBUG
            # totalmusic -= 1
            print("Judul Music berhasil dihapus")

        except:
            print("Judul music tidak ada ")


class Jawa(Music):
    def __init__(self,judul,penyanyi,genre) -> None:
        super().__init__(judul,penyanyi,genre)

    @staticmethod
    def tampilMenu():
        print("===========Javanese Song==========")
        print("1, Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")

    @staticmethod
    def display():
        print("DAFTAR MUSIC Jawa")
        no = 1
        for music in jawa:
            print(f"{no}. {music.judul} - {music.penyanyi} - {music.genre}")
            no+=1

    @staticmethod
    def addMusic():
        judul = input("Masukkan Judul Music: ")
        penyanyi = input("Masukkan Penyanyi: ")
        genre = "Jawa"
        objek = judul #SIAP DEBUG
        objek = Jawa(judul, penyanyi, genre)
        jawa.append(objek)
        allSong.append(objek)
        baru = [judul, penyanyi, genre] #SIAP DEBUG
        liststr.append(baru)
        # jawa.sort()

        # totalmusic += 1        
        # daftarpenyanyi.append(penyanyi)

    @staticmethod
    def deleteMusic():
        try:
            hapusJudul = input("Masukkan Judul music yang ingin dihapus: ")
            jawa.remove(hapusJudul)
            allSong.remove(hapusJudul)
            # totalmusic -= 1
            for i in len(liststr):
                if i[0] == hapusJudul:
                    liststr.pop(i)
            print("Judul Music berhasil dihapus")
        except:
            print("Judul music tidak ada ")


class English(Music):
    def __init__(self,judul,penyanyi,genre) -> None:
        super().__init__(judul,penyanyi,genre)

    @staticmethod
    def tampilMenu():
        print("===========English Song==========")
        print("1, Display Song")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")

    @staticmethod
    def display():
        print("DAFTAR MUSIC Inggris")
        no = 1
        for music in english:
            print(f"{no}. {music.judul} - {music.penyanyi} - {music.genre}")
            no+=1

    @staticmethod
    def addMusic():
        judul = input("Masukkan Judul Music: ")
        penyanyi = input("Masukkan Penyanyi: ")
        genre = "English"
        objek = judul #SIAP DEBUG
        objek = English(judul, penyanyi, genre)
        indo.append(objek)
        allSong.append(objek)
        baru = [judul, penyanyi, genre] #SIAP DEBUG
        liststr.append(baru)
        # totalmusic += 1
        # daftarpenyanyi.append(penyanyi)

    @staticmethod
    def deleteMusic():
        try:
            hapusJudul = input("Masukkan Judul music yang ingin dihapus: ")
            english.remove(hapusJudul)
            allSong.remove(hapusJudul)
            # totalmusic -= 1
            for i in len(liststr):
                if i[0] == hapusJudul:
                    liststr.pop(i)
            print("Judul Music berhasil dihapus")
        except:
            print("Judul music tidak ada ")


    
def menuUtamaTampil():
    print("=========Playlist Music=========")
    print("1. Indonesian Song")
    print("2. Javanese Song")
    print("3. English Song")
    print("4. Display All")
    print("5. Search Music")
    print("0. Keluar")

def menuIndo():
    while True:
        Indo.tampilMenu()
        pilih = input("Masukkan pilihan menu: ")
        if pilih == "1":
            Indo.display()
        elif pilih == "2":
            Indo.addMusic()
        elif pilih == "3":
            Indo.deleteMusic()
        elif pilih == "0":
            return True
        else:
            print("PILIHAN ANDA SALAH")


def menuJawa():
    while True:
        Jawa.tampilMenu()
        pilih = input("Masukkan pilihan menu: ")
        if pilih == "1":
            Jawa.display()
        elif pilih == "2":
            Jawa.addMusic()
        elif pilih == "3":
            Jawa.deleteMusic()
        elif pilih == "0":
            return True
        else:
            print("PILIHAN ANDA SALAH")

def menuEnglish():
    while True:
        English.tampilMenu()
        pilih = input("Masukkan pilihan menu: ")
        if pilih == "1":
            English.display()
        elif pilih == "2":
            English.addMusic()
        elif pilih == "3":
            English.deleteMusic()
        elif pilih == "0":
            return True
        else:
            print("PILIHAN ANDA SALAH")


def menuUtama():
    while True:
        menuUtamaTampil()
        pilih = input("Masukkan Pilihan Menu: ")
        if pilih == "1":
            menuIndo()
        elif pilih == "2":
            menuJawa()
        elif pilih == "3":
            menuEnglish()
        elif pilih == "4":
            Music.tampilMusic()
        elif pilih == "5":
            Music.cariMusic()
        elif pilih == "0":
            print("ANDA KELUAR PROGRAM")
            return True
        else:
            print("Masukkan Anda Salah")



# DEFAULT MUSIC DARI INDO
lp = Indo("Laskar Pelangi", "Nidji", "Indo")
hatihatijln = Indo("Hati-Hati di Jalan", "Tulus", "Indo")
terpesona = Indo("Terpesona", "Visky Salamor", "Indo")
clb = Indo("Cinta Luar Biasa", "Andmesh Kamaleng", "Indo")
akad = Indo("Akad", "Payung Teduh", "Indo")
allSong.append(lp)
allSong.append(hatihatijln)
allSong.append(terpesona)
allSong.append(clb)
allSong.append(akad)
indo.append(lp)
indo.append(hatihatijln)
indo.append(terpesona)
indo.append(clb)
indo.append(akad)
baru = ["Laskar Pelangi", "Nidji", "Indo"] #SIAP DEBUG
liststr.append(baru)
baru = ["Hati-Hati di Jalan", "Tulus", "Indo"]
liststr.append(baru)
baru = ["Terpesona", "Visky Salamor", "Indo"]
liststr.append(baru)
baru = ["Cinta Luar Biasa", "Andmesh Kamaleng", "Indo"]
liststr.append(baru)
baru = ["Akad", "Payung Teduh", "Indo"]
liststr.append(baru)

# DEFAULT MUSIC UNTUK JAWA
dl = Jawa("Dalan Liane", "Happy Asmara", "Jawa")
jtnd = Jawa("Joko Tingkir Ngombe Dawet", "Nella Kharisma", "Jawa")
ktmj = Jawa("Kartoyono Medot Janji", "Denny Caknan", "Jawa")
sudalu = Jawa("Sugeng Ndalu", "Denny Caknan", "Jawa")
suteki = Jawa("Suket Teki", "Denny Caknan", "Jawa")
allSong.append(dl)
allSong.append(jtnd)
allSong.append(ktmj)
allSong.append(sudalu)
allSong.append(suteki)
jawa.append(dl)
jawa.append(jtnd)
jawa.append(ktmj)
jawa.append(sudalu)
jawa.append(suteki)
baru = ["Dalan Liane", "Happy Asmara", "Jawa"]
liststr.append(baru)
baru = ["Joko Tingkir Ngombe Dawet", "Nella Kharisma", "Jawa"]
liststr.append(baru)
baru = ["Kartoyono Medot Janji", "Denny Caknan", "Jawa"]
liststr.append(baru)
baru = ["Sugeng Ndalu", "Denny Caknan", "Jawa"]
liststr.append(baru)
baru = ["Sugeng Ndalu", "Denny Caknan", "Jawa"]
liststr.append(baru)

# DEFAULT MUSIC UNTUK  ENGLISH
soy = English("Shape Of You", "Ed Sherran", "English")
sly = English("Someone Like You", "Adele", "English")
ritd = English("Rolling In The Deep", "Adele", "English")
bg = English("Bad Guy", "Billie Elish", "English")
bllight = English("Blinding Light", "The Weekend", "English")
allSong.append(soy)
allSong.append(sly)
allSong.append(ritd)
allSong.append(bg)
allSong.append(bllight)
english.append(soy)
english.append(sly)
english.append(ritd)
english.append(bg)
english.append(bllight)
baru = ["Shape Of You", "Ed Sherran", "English"]
liststr.append(baru)
baru = ["Someone Like You", "Adele", "English"]
liststr.append(baru)
baru = ["Rolling In The Deep", "Adele", "English"]
liststr.append(baru)
baru = ["Bad Guy", "Billie Elish", "English"]
liststr.append(baru)
baru = ["Blinding Light", "The Weekend", "English"]
liststr.append(baru)



menuUtama()

