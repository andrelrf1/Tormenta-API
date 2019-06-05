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
    experiencia = banco.Column(banco.Integer, nullable=True)
    dinheiro = banco.Column(banco.Integer, nullable=True)
    pvs = banco.Column(banco.Integer, nullable=True)
    pms = banco.Column(banco.Integer, nullable=True)
    dano = banco.Column(banco.Integer, nullable=True)
    pms_gasto = banco.Column(banco.Integer, nullable=True)

    def __init__(self, nome, usuario_id, nivel, forca, habilidade, resistencia, armadura, pdf, expereienia, dinheiro,
                 pvs, pms, dano, pms_gato):
        self.nome = nome
        self.usuario_id = usuario_id
        self.nivel = nivel
        self.forca = forca
        self.habilidade = habilidade
        self.resistencia = resistencia
        self.armadura = armadura
        self.pdf = pdf
        self.experiencia = expereienia
        self.dinheiro = dinheiro
        self.pvs = pvs
        self.pms = pms
        self.dano = dano
        self.pms_gasto = pms_gato

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
            "experiencia": self.experiencia,
            "dinheiro": self.dinheiro,
            "pvs": self.pvs,
            "pms": self.pms,
            "dano": self.dano,
            "pms_gasto": self.pms_gasto
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

    @classmethod
    def find_by_user_id(cls, usuario_id):
        personagens = cls.query.filter_by(usuario_id=usuario_id).all()
        if personagens:
            return personagens

        return None

    def salvar_personagem(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_personagem(self):
        banco.session.delete(self)
        banco.session.commit()
