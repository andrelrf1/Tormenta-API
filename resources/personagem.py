from flask_restful import Resource, reqparse
from model.personagem import Personagem as ModelPersonagem

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('nivel', type=int, required=True, help='O campo nível não pode estar vasio')
atributos.add_argument('forca', type=int, required=True, help='O campo forca não pode estar vasio')
atributos.add_argument('habilidade', type=int, required=True, help='O campo habilidade não pode estar vasio')
atributos.add_argument('resistencia', type=int, required=True, help='O campo resistencia não pode estar vasio')
atributos.add_argument('armadura', type=int, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('pdf', type=int, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('pv', type=int, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('pms', type=int, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('experiencia', type=int, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('dinheiro', type=float, required=True, help='O campo nome não pode estar vasio')
# atributos.add_argument('vantagem_id', type=int, required=True, help='O campo nome não pode estar vasio')
# atributos.add_argument('desvantagem_id', type=int, required=True, help='O campo nome não pode estar vasio')
# atributos.add_argument('usuario_id', type=int, required=True, help='O campo nome não pode estar vasio')


class Personagem(Resource):
    def get(self, personagem_id):
        personagem = ModelPersonagem.find_personagem(personagem_id)
        if personagem:
            return personagem.json()

        return {}
