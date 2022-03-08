import colorama
import pyfiglet
from colorama import Fore
colorama.init(autoreset=True)
# hitung_netmask
angka_x_pertama_oktet_terakhir = 128
angka_x_kedua_oktet_terakhir = 64
angka_x_ketiga_oktet_terakhir = 32
angka_x_keempat_oktet_terakhir = 16
angka_x_kelima_oktet_terakhir = 8
angka_x_keenam_oktet_terakhir = 4
angka_x_ketujuh_oktet_terakhir = 2
angka_x_kedelapan_oktet_terakhir = 1
print("\n" * 1)
baner = pyfiglet.figlet_format("Subnettor", font="slant")
print(Fore.LIGHTBLUE_EX+baner)
oktet_1_ipaddress = int(input(Fore.LIGHTGREEN_EX+"  Oktet Pertama IP Address"+Fore.LIGHTBLUE_EX+"  >>>"+Fore.WHITE+"   "))
oktet_2_ipaddress = int(input(Fore.LIGHTGREEN_EX+"  Oktet Kedua IP Address"+Fore.LIGHTBLUE_EX+"    >>>"+Fore.WHITE+"   "))
oktet_3_ipaddress = int(input(Fore.LIGHTGREEN_EX+"  Oktet Ketiga IP Address"+Fore.LIGHTBLUE_EX+"   >>>"+Fore.WHITE+"   "))
oktet_4_ipaddress = int(input(Fore.LIGHTGREEN_EX+"  Oktet Keempat IP Address"+Fore.LIGHTBLUE_EX+"  >>>"+Fore.WHITE+"   "))
cari_netmask = int(input(Fore.LIGHTGREEN_EX+"  CIDR"+Fore.LIGHTBLUE_EX+"                      >>>"+Fore.WHITE+"   "))
print("\n" * 1)
if cari_netmask == 24:
    x = 0
    y = 8
    jumlah_subnet = 2 ** x
    total_host = 2 ** y
    host_per_subnet = 2 ** y - 2
    blok_subnet = 256 - 0
    ip_network = oktet_4_ipaddress - oktet_4_ipaddress
    ip_broadcast = 255 - 0
    rumus = "(banyaknya x = 0)"
    netmask = 0
    print(Fore.LIGHTGREEN_EX + "  IP Address" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, oktet_4_ipaddress, "/24")
    print(
        Fore.LIGHTGREEN_EX + "  Binary" + Fore.LIGHTBLUE_EX + "                    >>>" + Fore.WHITE +
        "   11111111.11111111.11111111.00000000")
    print(
        Fore.LIGHTGREEN_EX + "  Netmask" + Fore.LIGHTBLUE_EX + "                   >>>" + Fore.WHITE +
        "   255 255 255",
        netmask)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Subnet" + Fore.LIGHTBLUE_EX + "             >>>"+Fore.WHITE+"  ", jumlah_subnet, "[0]")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Total Host" + Fore.LIGHTBLUE_EX + "         >>>"+Fore.WHITE+"  ", total_host)
    print(Fore.LIGHTGREEN_EX + "  Jumlah Host Per Subnet" + Fore.LIGHTBLUE_EX + "    >>>"+Fore.WHITE+"  ", host_per_subnet)
    print(Fore.LIGHTGREEN_EX + "  Blok Subnet" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast)
    print("\n")
elif cari_netmask == 25:
    x = 1
    y = 7
    jumlah_subnet = 2 ** x
    total_host = 2 ** y
    host_per_subnet = 2 ** y - 2
    blok_subnet = 256 - angka_x_pertama_oktet_terakhir
    ip_network = oktet_4_ipaddress - oktet_4_ipaddress
    ip_broadcast = 255 - angka_x_pertama_oktet_terakhir
    rumus = "Banyaknya x = 1"
    netmask = angka_x_pertama_oktet_terakhir
    print(Fore.LIGHTGREEN_EX + "  IP Address" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, oktet_4_ipaddress, "/25")
    print(
        Fore.LIGHTGREEN_EX + "  Binary" + Fore.LIGHTBLUE_EX + "                    >>>" + Fore.WHITE +
        "   11111111.11111111.11111111.10000000")
    print(
        Fore.LIGHTGREEN_EX + "  Netmask" + Fore.LIGHTBLUE_EX + "                   >>>" + Fore.WHITE +
        "   255 255 255",
        netmask)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Subnet" + Fore.LIGHTBLUE_EX + "             >>>"+Fore.WHITE+"  ", jumlah_subnet, "[0,128]")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Total Host" + Fore.LIGHTBLUE_EX + "         >>>"+Fore.WHITE+"  ", total_host)
    print(Fore.LIGHTGREEN_EX + "  Jumlah Host Per Subnet" + Fore.LIGHTBLUE_EX + "    >>>"+Fore.WHITE+"  ", host_per_subnet)
    print(Fore.LIGHTGREEN_EX + "  Blok Subnet" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet)
    print("\n" * 1)
elif cari_netmask == 26:
    x = 2
    y = 6
    jumlah_subnet = 2 ** x
    total_host = 2 ** y
    host_per_subnet = 2 ** y - 2
    blok_subnet = 256 - angka_x_pertama_oktet_terakhir - angka_x_kedua_oktet_terakhir
    ip_network = oktet_4_ipaddress - oktet_4_ipaddress
    ip_broadcast = 255 - angka_x_pertama_oktet_terakhir - angka_x_kedua_oktet_terakhir
    rumus = "Banyaknya x = 2"
    netmask = angka_x_pertama_oktet_terakhir + angka_x_kedua_oktet_terakhir
    print(Fore.LIGHTGREEN_EX + "  IP Address" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, oktet_4_ipaddress, "/26")
    print(
        Fore.LIGHTGREEN_EX + "  Binary" + Fore.LIGHTBLUE_EX + "                    >>>" + Fore.WHITE +
        "   11111111.11111111.11111111.11000000")
    print(
        Fore.LIGHTGREEN_EX + "  Netmask" + Fore.LIGHTBLUE_EX + "                   >>>" + Fore.WHITE +
        "   255 255 255",
        netmask)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Subnet" + Fore.LIGHTBLUE_EX + "             >>>"+Fore.WHITE+"  ", jumlah_subnet,
          "[0,64,128,192]")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Total Host" + Fore.LIGHTBLUE_EX + "         >>>"+Fore.WHITE+"  ", total_host)
    print(Fore.LIGHTGREEN_EX + "  Jumlah Host Per Subnet" + Fore.LIGHTBLUE_EX + "    >>>"+Fore.WHITE+"  ", host_per_subnet)
    print(Fore.LIGHTGREEN_EX + "  Blok Subnet" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet)
    print("\n" * 1)
elif cari_netmask == 27:
    x = 3
    y = 5
    jumlah_subnet = 2 ** x
    total_host = 2 ** y
    host_per_subnet = 2 ** y - 2
    blok_subnet = 256 - angka_x_pertama_oktet_terakhir - angka_x_kedua_oktet_terakhir - angka_x_ketiga_oktet_terakhir
    ip_network = oktet_4_ipaddress - oktet_4_ipaddress
    ip_broadcast = 255 - angka_x_pertama_oktet_terakhir - angka_x_kedua_oktet_terakhir - angka_x_ketiga_oktet_terakhir
    rumus = "Banyaknya x = 2"
    netmask = angka_x_pertama_oktet_terakhir + angka_x_kedua_oktet_terakhir + angka_x_ketiga_oktet_terakhir
    print(Fore.LIGHTGREEN_EX + "  IP Address" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, oktet_4_ipaddress, "/27")
    print(
        Fore.LIGHTGREEN_EX + "  Binary" + Fore.LIGHTBLUE_EX + "                    >>>" + Fore.WHITE +
        "   11111111.11111111.11111111.11100000")
    print(
        Fore.LIGHTGREEN_EX + "  Netmask" + Fore.LIGHTBLUE_EX + "                   >>>" + Fore.WHITE +
        "   255 255 255",
        netmask)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Subnet" + Fore.LIGHTBLUE_EX + "             >>>"+Fore.WHITE+"  ", jumlah_subnet,
          "[0,32,64,96,128,160,192,224]")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Total Host" + Fore.LIGHTBLUE_EX + "         >>>"+Fore.WHITE+"  ", total_host)
    print(Fore.LIGHTGREEN_EX + "  Jumlah Host Per Subnet" + Fore.LIGHTBLUE_EX + "    >>>"+Fore.WHITE+"  ", host_per_subnet)
    print(Fore.LIGHTGREEN_EX + "  Blok Subnet" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet)
    print("\n" * 1)
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet+ 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n" * 1)
elif cari_netmask == 28:
    x = 4
    y = 4
    jumlah_subnet = 2 ** x
    total_host = 2 ** y
    host_per_subnet = 2 ** y - 2
    blok_subnet = 256 - angka_x_pertama_oktet_terakhir - angka_x_kedua_oktet_terakhir - angka_x_ketiga_oktet_terakhir - angka_x_keempat_oktet_terakhir
    ip_network = oktet_4_ipaddress - oktet_4_ipaddress
    ip_broadcast = 255 - angka_x_pertama_oktet_terakhir - angka_x_kedua_oktet_terakhir - angka_x_ketiga_oktet_terakhir - angka_x_keempat_oktet_terakhir
    rumus = "Banyaknya x = 2"
    netmask = angka_x_pertama_oktet_terakhir + angka_x_kedua_oktet_terakhir + angka_x_ketiga_oktet_terakhir + angka_x_keempat_oktet_terakhir
    print(Fore.LIGHTGREEN_EX + "  IP Address" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, oktet_4_ipaddress, "/28")
    print(
        Fore.LIGHTGREEN_EX + "  Binary" + Fore.LIGHTBLUE_EX + "                    >>>" + Fore.WHITE +
        "   11111111.11111111.11111111.11110000")
    print(
        Fore.LIGHTGREEN_EX + "  Netmask" + Fore.LIGHTBLUE_EX + "                   >>>" + Fore.WHITE +
        "   255 255 255",
        netmask)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Subnet" + Fore.LIGHTBLUE_EX + "             >>>"+Fore.WHITE+"  ", jumlah_subnet,
          "[0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240]")
    print(Fore.LIGHTGREEN_EX + "  Jumlah Total Host" + Fore.LIGHTBLUE_EX + "         >>>"+Fore.WHITE+"  ", total_host)
    print(Fore.LIGHTGREEN_EX + "  Jumlah Host Per Subnet" + Fore.LIGHTBLUE_EX + "    >>>"+Fore.WHITE+"  ", host_per_subnet)
    print(Fore.LIGHTGREEN_EX + "  Blok Subnet" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>"+Fore.WHITE+"  ", oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet)
    print("\n" * 1)
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet+ 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n" * 1)
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    # 99999999999999999999999999999
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet+ 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    #11 11 11 11
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet  + blok_subnet)
    print("\n" * 1)
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress, ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")#13 13 13
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")#14
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n")
    print(Fore.LIGHTGREEN_EX + "  IP Network" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet )
    print(Fore.LIGHTGREEN_EX + "  IP Pertama" + Fore.LIGHTBLUE_EX + "                >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_network + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + 1)
    print(Fore.LIGHTGREEN_EX + "  IP Terakhir" + Fore.LIGHTBLUE_EX + "               >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet - 1)
    print(Fore.LIGHTGREEN_EX + "  IP Broadcast" + Fore.LIGHTBLUE_EX + "              >>>" + Fore.WHITE + "  ",
          oktet_1_ipaddress,
          oktet_2_ipaddress, oktet_3_ipaddress,
          ip_broadcast + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet + blok_subnet)
    print("\n" * 1)
else:
    print("error")
