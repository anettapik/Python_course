import math
import sys
import click


def wc(file):
    newline = 0
    word = 0
    count = 0
    while True:
        stroka = file.readline()
        if not stroka:
            break
        # считаем количество байт
        count += len(stroka)
        # считаем количество слов
        word += len(list(filter(lambda s: len(s) > 0, stroka.split())))
        # количество строк
        newline += 1
    return count, word, newline

@click.command()
@click.argument('file', type=click.File('rb'), nargs=-1)
def main(file):
    count, word, newline = (0, 0, 0)
    results = []
    length = 0
    # если нет файлов
    if len(file) == 0:
        length = 7
        res = wc(sys.stdin)
        results.append(res)
        word += res[1]
        count += res[0]
        newline += res[2]
    for cur_file in file:
        res = wc(cur_file)
        results.append(res)
        newline += res[2]
        word += res[0]
        count += res[1]
        if cur_file.name == "-":
            length = 17
    mx = max(newline, word, count)
    length = max(1 if (mx == 0) else math.floor(math.log10(mx)) + 2, length)
    for result, cur_file in zip(results, file):
        click.echo(f"{result[0]:{length}d}{result[1]:{length}d}{result[2]:{length}d} {cur_file.name}")
    if len(file) > 1:
        click.echo(f"{newline:{length}d}{word:{length}d}{count:{length}d} total")


if __name__ == '__main__':
    main()