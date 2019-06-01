from flask_restful import Resource, reqparse
from model.mesa import MesaModel
from flask_jwt_extended import jwt_required

parametros = reqparse.RequestParser()
parametros.add_argument('usuario_id', type=int)

atributos = reqparse.RequestParser()
atributos.add_argument('usuario_id', type=int, help='O campo usuario_id não pode ficar vazio')
atributos.add_argument('nome', type=str, help='O campo nome não pode ficar vazio')
atributos.add_argument('senha', type=str, help='O campo senha não pode estar vazio')


class MesasPersonagens(Resource):
    @jwt_required
    def get(self, usuario_id):
        return {'mesas': [mesa.json() for mesa in MesaModel.query.filter_by(usuario_id=usuario_id)]}


class Mesas(Resource):
    def get(self):
        return {'mesas': [mesa.json() for mesa in MesaModel.query.all()]}


class Mesa(Resource):
    def get(self, mesa_id):
        mesa = MesaModel.find_mesa(mesa_id)
        if mesa:
            return mesa.json()

        return {'message': 'Mesa not found'}, 404

    @jwt_required
    def delete(self, mesa_id):
        mesa = MesaModel.find_mesa(mesa_id)
        if mesa:
            mesa.delete_mesa()
            return {'message': 'Mesa deleted'}

        return {'message': 'Mesa not found'}, 404


class CreateMesa(Resource):
    @jwt_required
    def post(self):
        dados = atributos.parse_args()
        mesa = MesaModel(**dados)
        mesa.salvar_mesa()

        return {'message': 'Mesa criada'}
