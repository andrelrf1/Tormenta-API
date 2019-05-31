from flask_restful import Resource, reqparse
from model.usuario import UsuarioModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True, help="O campo não pode ser deixado em branco")
atributos.add_argument('senha', type=str, required=True, help="O campo não pode ser deixado em branco")


class Usuarios(Resource):

    def get(self):
        return {'usuarios': [usuario.json() for usuario in UsuarioModel.query.all()]}


class Usuario(Resource):

    def get(self, usuario_id):
        usuario = UsuarioModel.find_user(usuario_id)
        if usuario:
            return usuario.json()

        return {'message': 'Usuario not found'}

    @jwt_required
    def delete(self, usuario_id):
        usuario = UsuarioModel.find_user(usuario_id)
        if usuario:
            usuario.delete_user()
            return {'message': 'Usuario deleted'}

        return {'message': 'Usuario not found'}, 404


class RegistroUsuario(Resource):

    def post(self):
        dados = atributos.parse_args()

        if UsuarioModel.find_by_login(dados['nome']):
            return {"message": "O login '{}' já existe".format(dados['nome'])}

        user = UsuarioModel(**dados)
        user.salvar_user()
        return {"message": "Usuário criado"}, 201  # criado


class UsuarioLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        usuario = UsuarioModel.find_by_login(dados['nome'])
        if usuario and safe_str_cmp(usuario.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=usuario.usuario_id)
            return {'access_token': token_de_acesso}, 200

        return {'message': 'Usuario e senha incorretos'}, 401  # Unauthorize


class UsuarioLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']  # j de JWT, t de token e i de identifier
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully'}, 200
