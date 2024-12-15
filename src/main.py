from unittest.mock import patch


def get_mames(txt):
    with open(txt, 'r',encoding="utf-8") as fail:
        for lains in fail:
            print(lains)


#path = '../'
get_mames('data/names.txt')