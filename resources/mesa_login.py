from resources.mesa import MesaLogin
from flask_restful import reqparse

atributos = reqparse.RequestParser()
atributos.add_argument('mesa_id', type=int, required=True, help='O campo mesa_id é necessário')
atributos.add_argument('senha', type=str, required=True, help='O campo senha não pode estar vazio')


class Login(MesaLogin):
    def __init__(self):
        super().__init__()
        self.dados = atributos.parse_args()
        self.post(**self.dados)
