def formatInput(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ["y", "n"]:
            return user_input

if __name__ == "__main__":
    try:
        from os import system

        system("cls||clear")

        text_berbahaya = "******"    # vag***
        text_berbahaya2 = "******"   # pan***
        text_berbahaya3 = "*****"    # rah*****
        text_berbahaya4 = "*****"    # san**
        text_berbahaya5 = "*******"  # se*****

        ciri_ciri = {
            "mulut": ["lebar", "sempit"],
            "bibirAtas": ["tebal", "tipis"],
            "bibirBawah": ["kecil", "besar"],
            "warnaBibir": ["kering", "tidak kering"],
            "hidungMancung": [f"tidak begitu {text_berbahaya4} untuk melakukan {text_berbahaya5}", f"begitu {text_berbahaya4} untuk melakukan {text_berbahaya5}"],
            "dagu": ["menganga sedikit bulu", "tidak mengaga banyak bulu"],
            "alis": ["posisi agak kedalam", "posisi agak keluar"],
            "mataBercelakLebar": [f"sempit {text_berbahaya3}", f"lebar {text_berbahaya3}"]
        }

        print("\n # YTTA\n")

        mulut = formatInput(" - Apakah mulut lebar? (y/n) ")
        bibirAtas = formatInput(" - Apakah bibir atas tebal? (y/n) ")
        bibirBawah = formatInput(" - Apakah bibir bawah tebal? (y/n) ")
        warnaBibir = formatInput(" - Apakah warna bibir merah? (y/n) ")
        hidungMancung = formatInput(" - Apakah hidung mancung? (y/n) ")
        dagu = formatInput(" - Apakah dagu panjang? (y/n) ")
        alis = formatInput(" - Apakah alis tebal? (y/n) ")
        mataBercelakLebar = formatInput(" - Apakah mata bercelak & lebar? (y/n) ")

        ciri1 = ciri_ciri["mulut"][0] if mulut == "y" else ciri_ciri["mulut"][1]
        ciri2 = ciri_ciri["bibirAtas"][0] if bibirAtas == "y" else ciri_ciri["bibirAtas"][1]
        ciri3 = ciri_ciri["bibirBawah"][0] if bibirBawah == "y" else ciri_ciri["bibirBawah"][1]
        ciri4 = ciri_ciri["warnaBibir"][0] if warnaBibir == "y" else ciri_ciri["warnaBibir"][1]
        ciri5 = ciri_ciri["hidungMancung"][0] if hidungMancung == "y" else ciri_ciri["hidungMancung"][1]
        ciri6 = ciri_ciri["dagu"][0] if dagu == "y" else ciri_ciri["dagu"][1]
        ciri7 = ciri_ciri["alis"][0] if alis == "y" else ciri_ciri["alis"][1]
        ciri9 = ciri_ciri["mataBercelakLebar"][0] if mataBercelakLebar == "y" else ciri_ciri["mataBercelakLebar"][1]

        ciri8 = f"{text_berbahaya2} besar dan {text_berbahaya} kecil serta lebar" if mulut == "y" else f"{text_berbahaya2} kecil dan {text_berbahaya} besar serta sempit"

        print("\n # Hasil:")
        print(f" > {text_berbahaya} {ciri1}, {ciri2}, {ciri3}, dan {ciri4}\n   beliau {ciri5}\n   {text_berbahaya} {ciri6}, {ciri7}\n   {ciri8}\n   serta beliau {ciri9}")
    except KeyboardInterrupt:
        exit(0)
