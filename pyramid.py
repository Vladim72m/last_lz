import math
def sss(h, v_1, v_2):
    V_V = (1 / 3) * h * (v_1 + v_2 + math.sqrt(v_1 * v_2))
    return V_V 
def main():
    h = float(input("Высота: "))
    v_1 = float(input("Площадь нижнего основания: "))
    v_2 = float(input("Площадь верхнего основания: "))
    res = sss(h, v_1, v_2)
    print("Объём усечённой пирамиды:", res)

if __name__ == "__main__":
    main()
