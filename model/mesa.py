from sql_alchemy import banco


class MesaModel(banco.Model):
    __tablename__ = "mesas"

    mesa_id = banco.Column(banco.Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = banco.Column(banco.Text, nullable=False)
    senha = banco.Column(banco.Text, nullable=False)
    mundo = banco.Column(banco.Text, nullable=False)

    def __init__(self, mesa_id, nome, senha, mundo):
        self.mesa_id = mesa_id
        self.nome = nome
        self.senha = senha
        self.mundo = mundo

    def json(self):
        return {'mesa_id': self.mesa_id, 'nome': self.nome, 'senha': self.senha, 'mundo': self.mundo}

    @classmethod
    def procurar_mesa(cls, mesa_id):
        mesa = cls.query.filter_by(mesa_id=mesa_id).first()
        if mesa:
            return mesa_id

        return None

    def salvar_mesa(self):
        banco.session.add(self)
        banco.session.commit()

    def update_mesa(self, nome, senha, mundo):
        self.nome = nome
        self.senha = senha
        self.mundo = mundo
