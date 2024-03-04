import click

tail_size = 10


def tail(file):
    buffer = []
    while True:
        line = file.readline()
        if not line:
            break
        buffer.append(line)
        if len(buffer) > tail_size:
            buffer.pop(-1)
    for line in buffer:
        click.echo(line, nl=False)


@click.command()
@click.argument('file', type=click.File('r'), nargs=-1)
def main(file):
    if len(file) == 1:
        tail(file[0])
    else:
        for index, cur_file in enumerate(file):
            click.echo(f"==> {cur_file.name} <==")
            tail(cur_file)
            if index + 1 != len(file):
                click.echo()


if __name__ == '__main__':
    main()