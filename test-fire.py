import fire
from dicto import fire_options

@fire_options("params-fire.yml")
def main(hola, chao, p1, p_2):
    # params = Dicto(params)

    print(p1, p_2)

    print(hola, chao)
    print(type(hola), type(chao))

if __name__ == '__main__':
    fire.Fire(main)

