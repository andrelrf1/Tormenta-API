from sql_alchemy import banco


class MesaModel(banco.Model):
    __tablename__ = "mesas"

    mesa_id = banco.Column(banco.Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario_id = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario_id'))
    nome = banco.Column(banco.Text, nullable=False)
    senha = banco.Column(banco.Text, nullable=False)

    def __init__(self, mesa_id, nome, senha):
        self.mesa_id = mesa_id
        self.nome = nome
        self.senha = senha

    def json(self):
        return {'mesa_id': self.mesa_id, 'usuario_id': self.usuario_id, 'nome': self.nome, 'senha': self.senha}

    @classmethod
    def procurar_mesa(cls, mesa_id):
        mesa = cls.query.filter_by(mesa_id=mesa_id).first()
        if mesa:
            return mesa_id

        return None

    def salvar_mesa(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_mesa(self):
        banco.session.delete(self)
        banco.session.commit()
