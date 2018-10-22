import click
from dicto import click_options_config, Dicto

@click.command()
@click.argument("chao")
@click.argument("hola")
@click_options_config("params.yml", underscore_to_dash = True)
def main(hola, chao, p1, p_2):
    # params = Dicto(params)

    print(p1, p_2)

    print(hola, chao)

if __name__ == '__main__':
    main()