def yerleriTapma(xallar):
    siralananXallar = sorted(enumerate(xallar), key=lambda x: x[1], reverse=True)
    yerlər = [0] * len(xallar)
    for sıra, (index, xal) in enumerate(siralananXallar):
        yerlər[index] = f"{sıra + 1}-ci"
    return yerlər
xallar = [5, 3, 4, 2, 1]
print(yerleriTapma(xallar))
