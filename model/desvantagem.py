from sql_alchemy import banco


class Desvantagem(banco.Model):
    __tablename__ = "desvantagem"

    desvantagem_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    nome = banco.Column(banco.String(15), nullable=True)
    descricao = banco.Column(banco.String, nullable=True)
    custo = banco.Column(banco.Integer, nullable=True)
    # personagens = banco.relationship("Personagem", backref='desvantagem', lazy=True)

    def __init__(self, nome, descricao, custo):
        self.nome = nome
        self.descricao = descricao
        self.custo = custo

    def json(self):
        return {
            "desvantagem_id": self.desvantagem_id,
            "nome": self.nome,
            "descricao": self.descricao,
            "custo": self.custo
        }

    @classmethod
    def find_desvantagem(cls, desvantagem_id):
        desvantagem = cls.query.filter_by(desvantagem_id=desvantagem_id).first()
        if desvantagem:
            return desvantagem

        return None

    @classmethod
    def find_by_nome(cls, nome):
        desvantagem = cls.query.filter_by(nome=nome).first()
        if desvantagem:
            return desvantagem

        return None

    def salve_desvantagem(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_desvantagem(self):
        banco.session.delete(self)
        banco.session.commit()
