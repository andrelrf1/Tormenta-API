from sql_alchemy import banco


class ModelHistorico(banco.Model):
    __tablename__ = 'historico'

    historico_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    mesa_id = banco.Column(banco.Integer, banco.ForeignKey('mesa.mesa_id'), nullable=False)
    usuario_id = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario_id'), nullable=False)
    data = banco.Column(banco.DateTime, nullable=False)
    acao = banco.Column(banco.Text)
    notas = banco.Column(banco.Text)

    def __init__(self, mesa_id, usuario_id, data, acao, notas):
        self.mesa_id = mesa_id
        self.usuario_id = usuario_id
        self.data = data
        self.acao = acao
        self.notas = notas

    def json(self):
        return {
            'historico_id': self.historico_id,
            'mesa_id': self.mesa_id,
            'usuario_id': self.usuario_id,
            'data': self.data,
            'acao': self.acao,
            'notas': self.notas
        }

    @classmethod
    def find_historico(cls, historico_id):
        historico = cls.query.filter_by(historico_id=historico_id).first()
        if historico:
            return historico

        return None

    @classmethod
    def find_historico_by_mesa_id(cls, mesa_id: int):
        historico = cls.query.filter_by(mesa_id=mesa_id).all()
        if historico:
            return historico

        return None

    def salvar_historico(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_historico(self):
        banco.session.delete(self)
        banco.session.commit()
