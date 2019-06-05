from flask_restful import Resource, reqparse
from model.sessao import ModelSessao
from model.mesa_sess import ModelMesaSessao
from flask_jwt_extended import jwt_required

atributos = reqparse.RequestParser()
atributos.add_argument('ultm_acao', type=str)
atributos.add_argument('nts_narr', type=str)


class Sessao(Resource):
    @jwt_required
    def get(self, mesa_id):
        sessao_ids = [i for i in ModelMesaSessao.find_by_mesa_id(mesa_id)]

        try:
            sessao = []
            for sessao_id in sessao_ids:
                sessao.append(ModelSessao.find_sessao(sessao_id))

            return {
                'sessoes': sessao
            }

        except TypeError:
            return {'message': 'Sem sessões encontradas'}, 404

    @jwt_required
    def delete(self, sessao_id):

        deletado = False
        for sessao in ModelSessao.find_sessao(sessao_id):
            if sessao:
                sessao.delete()
                deletado = True

        if deletado:
            return {'message': 'Sessão apagada'}

        return {'message': 'Sessão não encontrada'}


class CreateSessao(Resource):
    @jwt_required
    def post(self):
        dados = atributos.parse_args()
        sessao = ModelSessao(**dados)
        sessao.salvar()

        return {'message': 'Sessão apagada'}
