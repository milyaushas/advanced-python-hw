from itertools import zip_longest


def table_begin():
    return "\\begin{tabular}{ |c|c| }\n \\hline\n"


def table_end():
    return "\end{tabular}"


def table_body(l):
    return ''.join([f" {a} & {b} \\\\ \\hline\n" for (a, b) in zip_longest(l[0], l[1], fillvalue="")])


def generate_table(l):
    return table_begin() + table_body(l) + table_end()


def main():
    l = [[1, 2, 3, 4], ['a', 'b', 'c']]
    tex = generate_table(l)

    with open("advanced-python-hw/hw_2/artifacts/easy.tex", "w") as file:
        file.write(tex)


if __name__ == "__main__":
    main()
