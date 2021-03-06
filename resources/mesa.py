from flask_restful import Resource, reqparse
from model.mesa import MesaModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_refresh_token
from werkzeug.security import safe_str_cmp

atributos = reqparse.RequestParser()
# atributos.add_argument('usuario_id', type=int, help='O campo usuario_id não pode ficar vazio')
atributos.add_argument('nome', type=str, help='O campo nome não pode ficar vazio')
atributos.add_argument('senha', type=str, help='O campo senha não pode estar vazio')
atributos.add_argument('tp_part', type=str, help='')
atributos.add_argument('sts_part', type=str, help='')
atributos.add_argument('sts_pers', type=str, help='')


class MesasPersonagens(Resource):
    @jwt_required
    def get(self):
        usuario_id = get_jwt_identity()
        try:
            return {'mesas': [mesa.json() for mesa in MesaModel.query.filter_by(usuario_id=usuario_id)]}

        except TypeError:
            return {'message': 'Não há mesas criadas'}


class Mesas(Resource):
    def get(self):
        return {'mesas': [mesa.json() for mesa in MesaModel.query.all()]}


class Mesa(Resource):
    @jwt_required
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
        dados['usuario_id'] = get_jwt_identity()
        mesa = MesaModel(**dados)
        mesa.salvar_mesa()

        return {'message': 'Mesa criada'}


class MesaLogin(Resource):
    @jwt_required
    def post(self, mesa_id, senha):
        mesa = Mesa().get(mesa_id)

        if mesa and safe_str_cmp(mesa['senha'], senha):
            usuario_id = get_jwt_identity()
            refresh_token = create_refresh_token(identity=usuario_id)
            return {'refresh_token': refresh_token}, 200

        return {'message': 'Senha incorreta'}
