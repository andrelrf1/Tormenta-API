from flask_restful import Resource, reqparse
from model.historico import ModelHistorico
from flask_jwt_extended import jwt_required
import time

atributos = reqparse.RequestParser()
atributos.add_argument('mesa_id', type=int, required=True, help='')
atributos.add_argument('usuario_id', type=int, required=True, help='')
atributos.add_argument('data', time.strftime('%d/%m/%y %H:%M:%S'))
atributos.add_argument('acao', type=str, required=True, help='')
atributos.add_argument('notas', type=str, required=True, help='')


class Historico(Resource):
    @jwt_required
    def get(self, mesa_id):
        try:
            return {'historico': [historico.json() for historico in ModelHistorico.find_historico_by_mesa_id(mesa_id)]}

        except TypeError:
            return {'message': 'Sem históricos'}

    @jwt_required
    def delete(self, mesa_id):
        for historico in ModelHistorico.find_historico_by_mesa_id(mesa_id):
            historico.delete()

            return {'message': 'Histórico Apagado'}


class CreateHistorico(Resource):
    @jwt_required
    def post(self):
        dados = atributos.parse_args()
        historico = ModelHistorico(**dados)
        historico.salvar_historico()

        return {'message': 'Histórico salvo'}

