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
                return None

            hasil = x0 - (f1/f2)

            gap = abs(hasil-x0)

            if gap <= e:
                print(f"Akar ditemukan dengan nilai {hasil} pada iterasi {z+1}")
                return hasil

            x0 = hasil

        except (ZeroDivisionError, ValueError):
            print("Terjadi kesalahan dalam perhitungan. Pastikan fungsi dan nilai awal valid.")
            return None
    print("Maksimal iterasi tercapai, solusi tidak ditemukan")
    return None

fungsi = input(f"Masukkan fungsi: ")
tebakan = float(input(f"Masukkan nilai tebakan awal: "))
iterasi = int(input(f"Masukkan batas iterasi: "))
batas = float(input(f"Masukkan nilai batas toleransi: "))

Newton_Raphson(fungsi, tebakan, iterasi, batas)