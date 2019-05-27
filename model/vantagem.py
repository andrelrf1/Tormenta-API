from sql_alchemy import banco


class Vantagem(banco.Model):
    __tablename__ = "vantagem"

    vantagem_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    nome = banco.Column(banco.String(15), nullable=True)
    descricao = banco.Column(banco.String, nullable=True)
    custo = banco.Column(banco.Integer, nullable=True)
    # personagens = banco.relationship("Personagem", backref="vantagem", lazy=True)

    def __init__(self, nome, descricao, custo):
        self.nome = nome
        self.descricao = descricao
        self.custo = custo

    @classmethod
    def find_vantagem(cls, vantagem_id):
        vantagem = cls.query.filter_by(vantagem_id=vantagem_id).first()
        if vantagem:
            return vantagem

        return None

    @classmethod
    def find_by_nome(cls, nome):
        vantagem = cls.query.filter_by(nome=nome).first()
        if vantagem:
            return vantagem

        return None

    def salve_vantagem(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_vantagem(self):
        banco.session.delete(self)
        banco.session.commit()