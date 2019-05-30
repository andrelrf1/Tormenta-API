from sql_alchemy import banco


class Personagem(banco.Model):
    __tablename__ = "personagem"

    personagem_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    usuario_id = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario_id'))
    nome = banco.Column(banco.String(15), nullable=True)
    nivel = banco.Column(banco.Integer, nullable=True)
    forca = banco.Column(banco.Integer, nullable=True)
    habilidade = banco.Column(banco.Integer, nullable=True)
    resistencia = banco.Column(banco.Integer, nullable=True)
    armadura = banco.Column(banco.Integer, nullable=True)
    pdf = banco.Column(banco.Integer, nullable=True)
    pv = banco.Column(banco.Integer, nullable=True)
    pms = banco.Column(banco.Integer, nullable=True)
    experiencia = banco.Column(banco.Integer, nullable=True)
    dinheiro = banco.Column(banco.Float(8.2), nullable=True)

    def __init__(self, nome, usuario_id, nivel, forca, habilidade, resistencia, armadura, pdf, pv, pms, experiencia, dinheiro):
        self.nome = nome
        self.usuario_id = usuario_id
        self.nivel = nivel
        self.forca = forca
        self.habilidade = habilidade
        self.resistencia = resistencia
        self.armadura = armadura
        self.pdf = pdf
        self.pv = pv
        self.pms = pms
        self.experiencia = experiencia
        self.dinheiro = dinheiro

    def json(self):
        return {
            "personagem_id": self.personagem_id,
            "usuario_id": self.usuario_id,
            "nome": self.nome,
            "nivel": self.nivel,
            "forca": self.forca,
            "habilidade": self.habilidade,
            "resistencia": self.resistencia,
            "armadura": self.armadura,
            "pdf": self.pdf,
            "pv": self.pv,
            "pms": self.pms,
            "experiencia": self.experiencia,
            "dinheiro": self.dinheiro
        }

    @classmethod
    def find_personagem(cls, personagem_id):
        personagem = cls.query.filter_by(personagem_id=personagem_id).first()
        if personagem:
            return personagem

        return None

    @classmethod
    def find_by_nome(cls, nome):
        personagem = cls.query.filter_by(nome=nome).first()
        if personagem:
            return personagem

        return None

    def salvar_personagem(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_personagem(self):
        banco.session.delete(self)
        banco.session.commit()
