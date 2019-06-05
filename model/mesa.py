from sql_alchemy import banco


class MesaModel(banco.Model):
    __tablename__ = "mesa"

    mesa_id = banco.Column(banco.Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario_id = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario_id'))
    nome = banco.Column(banco.Text, nullable=False)
    senha = banco.Column(banco.Text, nullable=False)
    tp_part = banco.Column(banco.VARCHAR(10), nullable=False)
    sts_part = banco.Column(banco.VARCHAR(10))
    sts_pers = banco.Column(banco.VARCHAR(5))

    def __init__(self, usuario_id, nome, senha, tp_part, sts_part, sts_pers):
        self.usuario_id = usuario_id
        self.nome = nome
        self.senha = senha
        self.tp_part = tp_part
        self.sts_part = sts_part
        self.sts_pers = sts_pers

    def json(self):
        return {
            'usuario_id': self.usuario_id,
            'mesa_id': self.mesa_id,
            'nome': self.nome,
            'tp_part': self.tp_part,
            'sts_part': self.sts_part,
            'sts_pers': self.sts_pers
        }

    @classmethod
    def find_mesa(cls, mesa_id):
        mesa = cls.query.filter_by(mesa_id=mesa_id).first()
        if mesa:
            return mesa

        return None

    @classmethod
    def find_by_user_id(cls, usuario_id):
        mesas = cls.query.filter_by(usuario_id=usuario_id).all()
        if mesas:
            return mesas

        return None

    def salvar_mesa(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_mesa(self):
        banco.session.delete(self)
        banco.session.commit()
