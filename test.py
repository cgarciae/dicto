import click
from dicto import click_options_config, Dicto

@click.command()
@click.argument("chao")
@click.argument("hola")
@click_options_config("params.yml")
def main(hola, chao, **prms):
    # params = Dicto(params)

    print(prms)

    print(hola, chao)

if __name__ == '__main__':
    main()