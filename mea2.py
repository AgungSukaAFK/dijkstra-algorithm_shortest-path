def means_ends_analysis(start, goal, graph):
    """
    Simulasi Means-Ends Analysis untuk memindahkan barang ke tujuan akhir.

    Parameters:
    start (str): Titik awal barang.
    goal (str): Titik tujuan barang.
    graph (dict): Representasi graf, di mana key adalah node, dan value adalah node yang terhubung.

    Returns:
    list: Jalur dari start ke goal, atau None jika tidak ada jalur.
    """
    current_state = start  # Kondisi awal
    path = [current_state]  # Menyimpan jalur yang dilalui
    
    while current_state != goal:
        # Cari perbedaan (tetangga dari state saat ini)
        neighbors = graph.get(current_state, [])
        if not neighbors:
            print(f"Tidak ada jalur dari {current_state} ke {goal}")
            return None
        
        # Pilih langkah pertama yang mengurangi perbedaan
        next_step = None
        for neighbor in neighbors:
            if neighbor not in path:  # Hindari lingkaran
                next_step = neighbor
                break

        if next_step is None:
            print(f"Tidak ada langkah valid untuk mengurangi perbedaan dari {current_state}")
            return None

        # Perbarui state dan tambahkan ke path
        current_state = next_step
        path.append(current_state)

    return path


# Representasi graf
graph = {
    "Start": ["A"],
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["Gudang"],
    "E": [],
    "F": ["Gudang"],
    "G": [],
    "Gudang": []
}

# Jalankan MEA
start = "Start"
goal = "Gudang"
result = means_ends_analysis(start, goal, graph)

# Hasil
if result:
    print("Jalur ditemukan:", " → ".join(result))
else:
    print("Tidak ada jalur yang ditemukan.")
