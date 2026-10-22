def fcfs(proses):

    waktu = 0

    hasil = []

    for nama, burst in proses:

        selesai = waktu + burst

        tat = selesai

        wt = tat - burst

        hasil.append((nama, burst, waktu, selesai, wt, tat))

        waktu = selesai

    return hasil

def sjf(proses):

    urut = sorted(proses, key=lambda p: p[1])

    return fcfs(urut)

if __name__ == "__main__":

    dataset = {

        "D1": [("A", 7), ("B", 4), ("C", 1), ("D", 4)],

        "D2": [("A", 10), ("B", 10), ("C", 10)],

        "D3": [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)],

    }

    for nama, proses in dataset.items():

        print(nama, "FCFS:", fcfs(proses))

        print(nama, "SJF:", sjf(proses))

from collections import deque

def round_robin(proses, quantum):

    sisa = {nama: burst for nama, burst in proses}

    antrean = deque(nama for nama, _ in proses)

    waktu = 0

    mulai_pertama = {}

    selesai = {}

    while antrean:

        nama = antrean.popleft()

        if nama not in mulai_pertama:

            mulai_pertama[nama] = waktu

        jalan = min(quantum, sisa[nama])

        waktu += jalan

        sisa[nama] -= jalan

        if sisa[nama] > 0:

            antrean.append(nama)

        else:

            selesai[nama] = waktu

    hasil = []

    for nama, burst in proses:

        tat = selesai[nama]

        wt = tat - burst

        rt = mulai_pertama[nama]

        hasil.append((nama, burst, tat, wt, rt))

    return hasil

def priority(proses):

    urut = sorted(proses, key=lambda p: p[2])

    waktu = 0

    hasil = []

    for nama, burst, prio in urut:

        selesai = waktu + burst

        tat = selesai

        wt = tat - burst

        hasil.append((nama, burst, prio, waktu, selesai, wt, tat))

        waktu = selesai

    return hasil

if __name__ == "__main__":

    dataset = [("A", 7), ("B", 4), ("C", 1), ("D", 4)]

    dataset_prio = [("A", 7, 2), ("B", 4, 1), ("C", 1, 4), ("D", 4, 3)]

    print("FCFS:", fcfs(dataset))

    print("SJF:", sjf(dataset))

    print("RR q=2:", round_robin(dataset, 2))

    print("RR q=4:", round_robin(dataset, 4))

    print("Priority:", priority(dataset_prio))