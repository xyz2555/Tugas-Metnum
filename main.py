import sympy as sym
import numpy as np

x = sym.Symbol('x')

def Newton_Raphson(f, a, i, e):
    x0 = a
    f = sym.simplify(f)
    df = sym.diff(f, x)
    
    for z in range(i):
        try:
            f1 = float(f.subs(x, x0))
            f2 = float(df.subs(x, x0))

            if f2 == 0:
                print("Turunan bernilai nol, iterasi tidak dapat dilanjutkan")
                Main()

            hasil = x0 - (f1/f2)

            gap = abs(hasil-x0)

            if gap <= e:
                print(f"Akar ditemukan dengan nilai {hasil} pada iterasi {z+1}")
                Main()

            x0 = hasil

        except (ZeroDivisionError, ValueError):
            print("Terjadi kesalahan dalam perhitungan. Pastikan fungsi dan nilai awal valid.")
            Main()

    print("Maksimal iterasi tercapai, solusi tidak ditemukan")
    Main()

def Secant(f, x0, x1, i, e):
    fx = sym.simplify(f)

    for z in range(i):
        try:
            f0 = float(fx.subs(x, x0))
            f1 = float(fx.subs(x, x1))

            x2 = x1 - (f1*((x1 - x0)/(f1 - f0)))

            gap = abs(x2 - x1)

            if gap <= e:
                print(f"Akar ditemukan dengan nilai {x2} pada iterasi ke {z+1}")
                Main()

            f2 = float(fx.subs(x,x2))

            x3 = x2 - (f2*((x2 - x1)/(f2 - f1)))

            gap = abs(x3 - x2)

            if gap <= e:
                print(f"Akar ditemukan dengan nilai {x3} pada iterasi ke {z+2}")
                Main()

            x0 = x2
            x1 = x3

        except(ZeroDivisionError, ValueError):
            print("Terjadi kesalahan dalam perhitungan. Pastikan fungsi dan nilai awal valid.")
            Main()

    print("Maksimal iterasi tercapai, solusi tidak ditemukan")
    Main()

def Main():
    print("Metode yang tersedia: ")
    print("1. Newton Raphson")
    print("2. Secant")
    print("3. Exit")

    user = input("Metode apa yang ingin digunakan: ")
    if user == "1":
        fungsi = input(f"Masukkan fungsi: ")
        tebakan = float(input(f"Masukkan nilai tebakan awal: "))
        iterasi = int(input(f"Masukkan batas iterasi: "))
        batas = float(input(f"Masukkan nilai batas toleransi: "))

        Newton_Raphson(fungsi, tebakan, iterasi, batas)

    elif user == "2":
        fungsi = input(f"Masukkan fungsi: ")
        tebakan = float(input(f"Masukkan nilai tebakan awal: "))
        tebakan2 = float(input(f"Masukkan nilai tebakan dua: "))
        iterasi = int(input(f"Masukkan batas iterasi: "))
        batas = float(input(f"Masukkan nilai batas toleransi: "))

        Secant(fungsi, tebakan, tebakan2, iterasi, batas)

    elif user == "3":
        exit()
        return None

    else:
        print("Input Error")
        Main()

Main()
