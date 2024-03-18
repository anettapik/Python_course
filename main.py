from hw21 import generate_table

if __name__ == '__main__':
    table = [["one", 2, 3, [1, 2]],
             [11, 5, 15, 8],
             [21, 22, 23, 24],
             ["aha", 2, 3, 4]]

    tex = generate_table(table)

    f = open("artifacts/2-1.tex", "w")
    f.write(tex)
    f.close()