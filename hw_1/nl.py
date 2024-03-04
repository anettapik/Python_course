# Написать упрощенный вариант утилиты `nl` -- скрипт, который выдает в `stdout` пронумерованные строки из файла.
# Если файл не передан, то скрипт читает строки из `stdin`.

# Он должен работать так же, как `nl -b a`.

# sys.stdin - объект в программа, куда попадает весь введеныый ползователем ввод 
# Данные в нем хранятся до тех пока пока программа их не прочитала


import click

@click.command()
@click.argument('file', type=click.File('r'), default="-")
def main(file):
    index = 0
    while True:
        line = file.readline()
        if not line:
            break
        index += 1
        click.echo(f"{index:6d}\t{line}", nl=False)

if __name__ == '__main__':
    main()

