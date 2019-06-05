from sql_alchemy import banco


class ModelMesaSessao(banco.Model):
    __tablename__ = 'mesasessao'

    mesa_sess_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    data_sess = banco.Column(banco.DateTime, nullable=False)
    sessao_id = banco.Column(banco.Integer, banco.ForeignKey('sessao.sessao_id'))
    mesa_id = banco.Column(banco.Integer, banco.ForeignKey('mesa.mesa_id'))

    def __init__(self, sessao_id, mesa_id):
        self.sessao_id = sessao_id
        self.mesa_id = mesa_id

    def json(self):
        return {
            'data_sess': self.data_sess,
            'sessao_id': self.sessao_id,
            'mesapart_id': self.mesa_id
        }

    @classmethod
    def find_by_mesa_id(cls, mesa_id):
        mesa_sessao = cls.query.filter_by(mesa_id=mesa_id)
        if mesa_sessao:
            return mesa_sessao

        return None

    def salvar(self):
        banco.session.add(self)
        banco.session.commit()

    def delete(self):
        banco.session.delete(self)
        banco.session.commit()
