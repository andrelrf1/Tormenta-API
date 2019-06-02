from flask_restful import Resource, reqparse
from model.mesapart import ModelMesaPart
from flask_jwt_extended import jwt_required, get_jwt_identity

atributos = reqparse.RequestParser()
atributos.add_argument('usuario_id', type=int, required=True, help='')
atributos.add_argument('personagem_id', type=int, required=True, help='')
atributos.add_argument('mesa_id', type=int, required=True, help='')


class MesaPart(Resource):

    @jwt_required
    def get(self, mesa_id):  # Mostrar partidas relacionadas a mesa em questão
        try:
            return {'mesapart': [mesapart.json() for mesapart in ModelMesaPart.find_by_mesa_id(mesa_id)]}

        except TypeError:
            return {'message': 'Sem partidas recentes'}

    @jwt_required
    def delete(self, mesa_id):  # apagar a relação partida
        for mesapart in ModelMesaPart.find_by_mesa_id(mesa_id=mesa_id):
            mesapart.delete()

        return {'message': 'MesaPart deletada'}
