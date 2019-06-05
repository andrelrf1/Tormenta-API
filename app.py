import os
from flask import Flask, jsonify
from flask_restful import Api
from resources.usuario import Usuario, Usuarios, RegistroUsuario, UsuarioLogin, UsuarioLogout
from resources.personagem import Personagem, Personagens, CreatePersonagem, PersonagensUsuario
from resources.mesa import Mesa, Mesas, CreateMesa, MesasPersonagens
from resources.mesapart import MesaPart, CreateMesaPart
from resources.sessao import Sessao, CreateSessao
from resources.mesa_sess import MesaSess
from resources.mesa_login import MesaLogin
from flask_jwt_extended import JWTManager  # gerencia a autenticação
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  # configuração para criação e conexão do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'  # chave
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_deacesso_invalidado():
    return jsonify({'messade': 'you have been logged out'}), 401


@app.before_first_request
def criar_banco():
    banco.create_all()


api.add_resource(Usuarios, '/usuario/all')
api.add_resource(Usuario, '/usuario/<int:usuario_id>')
api.add_resource(UsuarioLogin, '/usuario/login')
api.add_resource(UsuarioLogout, '/usuario/logout')

api.add_resource(Personagem, '/personagem/<int:personagem_id>')
api.add_resource(Personagens, '/personagem/all')
api.add_resource(CreatePersonagem, '/personagem/criar')
api.add_resource(RegistroUsuario, '/cadastro')
api.add_resource(PersonagensUsuario, '/personagem/get')

api.add_resource(Mesas, '/mesa')
api.add_resource(Mesa, '/mesa/<int:mesa_id>')
api.add_resource(CreateMesa, '/mesa/criar')
api.add_resource(MesasPersonagens, '/mesa/get/<int:usuario_id>')
api.add_resource(MesaLogin, '/mesa/login')

api.add_resource(MesaPart, '/mesapart/<int:mesa_id>')
api.add_resource(CreateMesaPart, '/mesapart/create')

api.add_resource(Sessao, '/sessao/<int:mesa_id>')
api.add_resource(CreateSessao, '/sessao/create')

api.add_resource(MesaSess, '/mesaSessao')

if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
