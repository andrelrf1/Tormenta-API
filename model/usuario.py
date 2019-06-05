from sql_alchemy import banco


class UsuarioModel(banco.Model):
    __tablename__ = 'usuario'

    usuario_id = banco.Column(banco.Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = banco.Column(banco.Text, nullable=False)
    senha = banco.Column(banco.Text, nullable=False)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def json(self):
        return {
            "usuario_id": self.usuario_id,
            "nome": self.nome,
        }

    @classmethod
    def find_user(cls, usuario_id):
        usuario = cls.query.filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario

        return None

    @classmethod
    def find_by_login(cls, nome):
        usuario = cls.query.filter_by(nome=nome).first()
        if usuario:
            return usuario

        return None

    def salvar_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
