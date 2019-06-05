from flask_restful import Resource, reqparse
from model.mesa_sess import ModelMesaSessao
from flask_jwt_extended import jwt_required
import time

atributos = reqparse.RequestParser()
atributos.add_argument('sessãp id', type=int, required=True)
atributos.add_argument('mesa_id', type=int, required=True)

class MesaSess(Resource):
    @jwt_required
    def get(self, mesa_id):
        return {'MesaSess': [mesa_sess for mesa_sess in ModelMesaSessao.find_by_mesa_id(mesa_id)]}

    def delete(self, mesa_id):

        deletado = False
        for mesa_sess in ModelMesaSessao.find_by_mesa_id(mesa_id):
            if mesa_sess:
                mesa_sess.delete()
                deletado = True

            if deletado:
                return {'message': 'Sessão apagas'}

            return {'message': 'Sem sessão encontrada'}


    class CreateMesaSess(Resource):
        @jwt_required
        def post(self):
            dados = atributos.parse_args()
            dados['data_sess'] = time.strftime('%D/%M/%Y %H:%M:%S')
            mesa_sess = ModelMesaSessao(**dados)
            mesa_sess.salvar()

            return {'message': 'MesaSess criada'}

