import time, pytz, os, sys
from datetime import datetime

data_base = {}

def TimeNow():
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    localtimes = datetime.strftime(timeNow, "%Y-%m-%d  | %a %I.%M %p")
    return localtimes

def DisplayMenu():
    os.system("cls")
    view = """
|=============== << PANGERAN BEACH >> ==============|
|  KODE     JENIS KAMAR         HARGA PER MALAM     |
|===================================================|
|  S    |     Singel           |  Rp. 100.000       |
|  D    |     Double           |  Rp. 350.000       |
|  F    |     Family           |  Rp. 550.000       |
|===================================================|
    """
    print(view)

def MainSystem():
    client = int(input("Masukan jumlah kamar : "))
    get_timenow = "reservasi: "+str(len(list(data_base)) + 1 ) +" - "+ TimeNow()
    data_base[get_timenow] = {
        "kamar":[],
        "harga":[],
        "lama_inap":[]
    }
    loop = True
    count = 1
    while count <=  client:
        print("|===================================================|")
        lama = int(input("lama menginap :"))
        kamar = input("masukan jenis kamar [S/D/F] :")
        if kamar.lower() == "s":
            room_type = "Single"
            harga = 100000 * lama
            lama_inap = lama
        elif kamar.lower() == "d":
            room_type = "Double"
            harga = 350000 * lama
            lama_inap = lama
        elif kamar.lower() == "f":
            room_type = "Family"
            harga = 550000 * lama
            lama_inap = lama
        else:
            os.system("cls")
            print("|===================================================|")
            print("              PILIHAN TIDAK TERSEDIA")
            print("|===================================================|")
            time.sleep(2)
            os.system("cls")
            loop = False
        if loop:
            os.system("cls")
            count += 1
            data_base[get_timenow]["kamar"].append(room_type)
            data_base[get_timenow]["harga"].append(harga * lama_inap)
            data_base[get_timenow]["lama_inap"].append(lama_inap)
            print(f"o======> [kamar {count-1}]")
            print("> Tipe kamar :    ",room_type)
            print("> Harga      : Rp.",harga)
            print("> Lama inap  : ",lama_inap,"Malam")
            print("> Total harag: Rp.",harga * lama_inap)
        loop = True

def ListRoom():
    print("|======================== << PANGERAN BEACH >> =======================|")
    for i,x in enumerate(list(data_base)):
        print(f"{i+1}. {x}")
    print("=====================================================================")

def PriviewList(doagain=False):
    ListRoom()
    print("1. buka data")
    print("2. kembali ke menu")
    if doagain:
        client = 1
    else:
        client = int(input("masukan pilihan: "))
    os.system("cls")
    if client == 1:
        os.system("cls")
        ListRoom()
        number = int(input("pilihan nomor data dari menu di atas: "))
        data_name = list(data_base)[number-1] 
        print("|======================== << PANGERAN BEACH >> =======================|")
        print("No.\tJenis kamar\tHarga per malam\t\tlama inap(malam)\tJumlah harga")
        total_semua = 0
        for i, x in enumerate(list(data_base[data_name]["kamar"])):
            jenis_kamar = list(data_base[data_name]["kamar"])[i]
            total_biyaya = int(list(data_base[data_name]["harga"])[i])
            lama_menginap = int(list(data_base[data_name]["lama_inap"])[i])
            harga_kamar = total_biyaya / lama_menginap
            total_semua += total_biyaya
            print(f"{i+1} .["+str(jenis_kamar[0]).upper()+"]\t"+jenis_kamar+"\t\t\t"+str(harga_kamar)+"\t\t"+str(lama_menginap)+"\t\t\tRp."+str(total_biyaya))
        if total_semua >= 2000000:
            bonus = "handuk"
        else:
            bonus = "totebag"
        print ("\n\t\t\t\t\t\t\t\tTotal biyaya Keseluruhan: Rp. "+str(total_semua))
        print ("\n\t\t\t\t\t\t\t\tBonus yang didapat     : "+str(bonus))
        choice = input("apakah ada ingin melihat data lagi [y/n]: ")
        if choice.lower() == "y":
            PriviewList(doagain=False)
    elif client == 2:
        pass
    else:
        print("|===================================================|")
        print("              PILIHAN TIDAK TERSEDIA")
        print("|===================================================|")
        time.sleep(2)
        PriviewList()

def MainFunction():
    print("|======================== << PANGERAN BEACH >> =======================|")
    print("1. Reservasi")
    print("2. Liaht list")
    print("3. exit")
    client = int(input("Masukan pilihan : "))
    if client == 1:
        DisplayMenu()
        MainSystem()
        input("tekan [enter] untuk melanjutkan")
        os.system("cls")
    elif client == 2:
        PriviewList()
        input("tekan [enter] untuk melanjutkan")
    elif client == 3:
        print("|===================================================|")
        print("\t\t\tSYSTEM EXIT\t\t\t")
    else:
        os.system("cls")
        print("|===================================================|")
        print("              PILIHAN TIDAK TERSEDIA")
        print("|===================================================|")
        time.sleep(2)

while True:
    os.system("cls")
    MainFunction()

