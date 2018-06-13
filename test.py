import click
from dicto import click_options_config, Dicto

@click.command()
@click.argument("chao")
@click.argument("hola")
@click_options_config("params.yml")
def main(hola, chao, **params):
    params = Dicto(params)
    print(params)

    print(hola, chao)

if __name__ == '__main__':
    main()