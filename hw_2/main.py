from itertools import zip_longest


def generate_table(l):
    begin = "\\begin{tabular}{ |c|c| }\n \\hline\n"
    end = "\end{tabular}"
    body = ''.join([f" {a} & {b} \\\\ \\hline\n" for (a, b) in zip_longest(l[0], l[1], fillvalue="")])
    return begin + body + end


def main():
    l = [[1, 2, 3, 4], ['a', 'b', 'c']]
    tex = generate_table(l)

    with open("advanced-python-hw/hw_2/artifacts/easy.tex", "w") as file:
        file.write(tex)


if __name__ == "__main__":
    main()
