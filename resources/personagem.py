from flask_restful import Resource, reqparse
from model.personagem import Personagem as ModelPersonagem
from flask_jwt_extended import jwt_required, get_jwt_identity

path_params = reqparse.RequestParser()
path_params.add_argument('usuario_id', type=int)

atributos = reqparse.RequestParser()
# atributos.add_argument('usuario_id', type=int, required=True, help='O campo usuario_id não pode estar vazio')
atributos.add_argument('nome', type=str, required=True, help='O campo nome não pode estar vasio')
atributos.add_argument('nivel', type=int, required=True, help='O campo nível não pode estar vasio')
atributos.add_argument('forca', type=int, required=True, help='O campo forca não pode estar vasio')
atributos.add_argument('habilidade', type=int, required=True, help='O campo habilidade não pode estar vasio')
atributos.add_argument('resistencia', type=int, required=True, help='O campo resistencia não pode estar vasio')
atributos.add_argument('armadura', type=int, required=True, help='O campo armadura não pode estar vasio')
atributos.add_argument('pdf', type=int, required=True, help='O campo pdf não pode estar vasio')
atributos.add_argument('experiencia', type=int, required=True, help='O campo experiencia não pode estar vasio')
atributos.add_argument('dinheiro', type=float, required=True, help='O campo dinheiro não pode estar vasio')
atributos.add_argument('pvs', type=int, required=True, help='O campo pvs não pode estar vasio')
atributos.add_argument('pms', type=int, required=True, help='O campo pms não pode estar vasio')
atributos.add_argument('dano', type=int, required=True, help='O campo dano não pode estar vasio')
atributos.add_argument('pms_gasto', type=int, required=True, help='O campo pms_gastp não pode estar vasio')


class PersonagensUsuario(Resource):
    @jwt_required
    def get(self):
        usuario_id = get_jwt_identity()
        try:
            return {'personagens': [personagem.json() for personagem in
                                    ModelPersonagem.find_by_user_id(usuario_id=usuario_id)]}

        except TypeError:
            return {'message': 'Sem personagens criados.'}, 404


class Personagens(Resource):
    def get(self):
        return {'personagens': [personagem.json() for personagem in ModelPersonagem.query.all()]}


class Personagem(Resource):
    @jwt_required
    def get(self, personagem_id):
        personagem = ModelPersonagem.find_personagem(personagem_id)
        if personagem:
            return personagem.json()

        return {'message': 'Personagem not found'}, 404

    @jwt_required
    def delete(self, personagem_id):
        personagem = ModelPersonagem.find_personagem(personagem_id)
        if personagem:
            personagem.delete_personagem()
            return {'message': 'Personagem deleted'}

        return {'message': 'Personagem not found'}, 404


class CreatePersonagem(Resource):
    @jwt_required
    def post(self):
        dados = atributos.parse_args()
        dados['usuario_id'] = get_jwt_identity()
        personagem = ModelPersonagem(**dados)
        personagem.salvar_personagem()

        return {'message': 'Personagem criado'}
