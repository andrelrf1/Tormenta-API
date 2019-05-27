from flask import Flask
from flask_restful import Api
from resources.usuario import Usuario, Usuarios, RegistroUsuario, UsuarioLogin
from flask_jwt_extended import JWTManager  # gerencia a autenticação

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  # configuração para criação e conexão do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'  # chave
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def criar_banco():
    banco.create_all()


api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<int:usuario_id>')
api.add_resource(RegistroUsuario, '/cadastro')
api.add_resource(UsuarioLogin, '/login')

if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
