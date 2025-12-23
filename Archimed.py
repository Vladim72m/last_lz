def main():
    M = float(input("Введите массу объекта (кг): "))
    V = float(input("Введите объем погруженной части (м^3): "))
    P = float(input("Введите плотность объекта (кг/м^3): "))
    water = 1000  
    plavuchest = lambda M, V, water: (water * V) >= M
    if plavuchest(M, V, water):
        print("Объект плавает")
    else:
        print("Объект тонет")

if __name__ == "__main__":  
    main()
