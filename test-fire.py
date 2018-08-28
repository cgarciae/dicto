import fire
from dicto import fire_options

@fire_options("params-fire.yml", 'params')
def main(hola, chao, params):
    # params = Dicto(params)

    print(params)

    print(hola, chao)

if __name__ == '__main__':
    fire.Fire(main)

