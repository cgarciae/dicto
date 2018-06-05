import click
from dicto import click_options_config, Dicto

@click.command()
@click.argument("hola")
@click_options_config("params.yml")
def main(hola, **params):
    params = Dicto(params)

    print(params)

if __name__ == '__main__':
    main()