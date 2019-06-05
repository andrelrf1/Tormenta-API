from flask_restful import Resource, reqparse
from model.mesapart import ModelMesaPart
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_refresh_token_required
import time

atributos = reqparse.RequestParser()
atributos.add_argument('mesa_id', type=int, required=True, help='')
# atributos.add_argument('usuario_id', type=int, required=True, help='')
atributos.add_argument('personagem_id', type=int, required=True, help='')
atributos.add_argument('tip_usuario')
atributos.add_argument('sts_part')
atributos.add_argument('sts_pers')


class MesaPart(Resource):

    @jwt_refresh_token_required
    def get(self, mesa_id):  # Mostrar partidas relacionadas a mesa em questão
        try:
            return {'mesapart': [mesapart.json() for mesapart in ModelMesaPart.find_by_mesa_id(mesa_id)]}

        except TypeError:
            return {'message': 'Sem partidas recentes'}

    @jwt_refresh_token_required
    def delete(self, mesa_id):  # apagar a relação partida
        for mesapart in ModelMesaPart.find_by_mesa_id(mesa_id=mesa_id):
            mesapart.delete()

        return {'message': 'MesaPart deletada'}


class CreateMesaPart(Resource):
    @jwt_refresh_token_required
    def post(self):
        dados = atributos.parse_args()
        dados['ent_part'], dados['ini_mesa'] = time.strftime('%d/%m/%y %H:%M:%S'), time.strftime('%d/%m/%y %H:%M:%S')
        dados['usuario_id'] = get_jwt_identity()
        mesapart = ModelMesaPart(**dados)
        mesapart.salvar_mesapart()
