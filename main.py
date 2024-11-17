import os
import sys
import platform
from dijkstra import dijkstra

def visualize_graph(graph_data):
    # START tampilin graf
    print("\nPenjabaran Graf (contoh kasus):")
    for node, neighbors in graph_data.items():
        print(f"{node}: {', '.join([f'{neighbor} (bobot: {weight})' for neighbor, weight in neighbors.items()])}")
    print("\n")
    # END tampilin graf

def main():
    # CLSCR
    if sys.platform == 'win32':
        os.system('cls')    

    # START Salam pembuka
    print("\n=======================================")
    print("Selamat datang di Program Algoritma Dijkstra")
    print()
    developer = ["M. Agung Maulana - 1101221114", "Devitasari Dewi- 1101221114", "Yulianingsih - 1101221114"]
    print("Dibuat oleh:")
    for d in developer:
        print(f"  {developer.index(d) + 1}. {d}")
    print()
    print(f"Versi Python: {platform.python_version()}")
    print()
    print("Deskripsi: Program ini menggunakan Algoritma Dijkstra untuk menemukan jalur terpendek antara dua node.")
    print("=======================================\n\n")
    # END Salam pembuka

    
    graph_data = {
        # Lantai 2
        'P13': {'P7': 3, 'P12': 4},
        'P7': {'P13': 3, 'P9': 2},
        'P12': {'P13': 4, 'P9': 4, 'T12': 5},
        'P9': {'P7': 2, 'P8': 3, 'P12': 4, 'P10': 8},
        'P8': {'P9': 3},
        'T12': {'P12': 5, 'P11': 3, "P4": 3, "P5": 4},
        'P11': {'T12': 3, 'P10': 5},
        'P10': {'P9': 8, 'P11': 5},
        # Lantai 1
        'P1': {'P2': 3, 'PK': 4},
        'P2': {'P1': 3, 'P3': 7, 'P5': 4, 'PK': 5},
        'P3': {'P2': 7, 'P4': 4, 'PK': 4},
        'P4': {'P3': 4, 'T12': 3},
        'P5': {'P2': 4, 'P6': 4, 'T12': 4},
        'P6': {'P5': 4, 'PK': 1},
        'PK': {'P1': 4, 'P2': 5, 'P3': 4, 'P6': 1}
    }

    visualize_graph(graph_data)

    # START Loop program
    while True:
        # Input node awal dan tujuan
        start = input("Masukkan node awal (Initial): ").strip()
        end = input("Masukkan node tujuan (Final): ").strip()
        print()
        # Validasi input node
        if start not in graph_data or end not in graph_data:
            print("Node yang dimasukkan tidak valid. Pastikan node ada di dalam graf.")
            continue

        # Panggil fungsi dijkstra dan tampilkan hasil
        hasil = dijkstra(graph_data, start, end)
        print(hasil)
        print()

        # Tanya apakah ingin mengulangi atau keluar
        ulang = input("Apakah Anda ingin mengulangi? (y/n): ").strip().lower()
        if ulang != 'y':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
    # END Loop program

main()