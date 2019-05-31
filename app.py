import os
from flask import Flask, jsonify
from flask_restful import Api
from resources.usuario import Usuario, Usuarios, RegistroUsuario, UsuarioLogin, UsuarioLogout
from resources.personagem import Personagem, Personagens, CreatePersonagem
from resources.mesa import Mesa, Mesas, CreateMesa
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
    return jsonify({'messade': 'you have been logged iut'}), 401


@app.before_first_request
def criar_banco():
    banco.create_all()


api.add_resource(Usuarios, '/usuarios')
api.add_resource(Personagens, '/personagens')
api.add_resource(Mesas, '/mesas')
api.add_resource(Mesa, '/mesa/<int:mesa_id>')
api.add_resource(Personagem, '/personagem/<int:personagem_id>')
api.add_resource(Usuario, '/usuario/<int:usuario_id>')
api.add_resource(CreateMesa, '/criarMesa')
api.add_resource(RegistroUsuario, '/cadastro')
api.add_resource(CreatePersonagem, '/criarPersonagem')
api.add_resource(UsuarioLogin, '/login')
api.add_resource(UsuarioLogout, '/logout')

if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
