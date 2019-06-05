from sql_alchemy import banco


class ModelSessao(banco.Model):
    __tablename__ = 'sessao'

    sessao_id = banco.Column(banco.Integer, primary_key=True, nullable=False, autoincrement=True)
    ultm_acao = banco.Column(banco.Text)
    nts_narr = banco.Column(banco.Text)

    def __init__(self, ultm_acao, nts_narr):
        self.ultm_acao = ultm_acao
        self.nts_narr = nts_narr

    def json(self):
        return {
            'sessao_id': self.sessao_id,
            'ultm_acao': self.ultm_acao,
            'nts_narr': self.nts_narr
        }

    @classmethod
    def find_sessao(cls, sessao_id):
        sessao = cls.query.filter_by(sessao_id=sessao_id)
        if sessao:
            return sessao

        return None

    def salvar(self):
        banco.session.add(self)
        banco.session.commit()

    def delete(self):
        banco.session.delete(self)
        banco.session.commit()
