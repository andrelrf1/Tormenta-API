from sql_alchemy import banco


class ModelMesaPart(banco.Model):
    __tablename__ = 'mesapart'

    mesapart_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    mesa_id = banco.Column(banco.Integer, banco.ForeignKey('mesa.mesa_id'), nullable=False)
    usuario_id = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario_id'), nullable=False)
    personagem_id = banco.Column(banco.Integer, banco.ForeignKey('personagem.personagem_id'), nullable=False)
    tip_usuario = banco.Column(banco.Boolean, nullable=False)
    ent_part = banco.Column(banco.DateTime, nullable=False)
    sai_part = banco.Column(banco.DateTime)
    ini_mesa = banco.Column(banco.DateTime, nullable=False)
    fim_mesa = banco.Column(banco.DateTime)

    def __init__(self, mesa_id, usuario_id, personagem_id, tip_usuario, ent_part, sai_part, ini_mesa, fim_mesa):
        self.mesa_id = mesa_id
        self.usuario_id = usuario_id
        self.personagem_id = personagem_id
        self.tip_usuario = tip_usuario
        self.ent_part = ent_part
        self.sai_part = sai_part
        self.ini_mesa = ini_mesa
        self.fim_mesa = fim_mesa

    def json(self):
        return {
            'mesapart_id': self.mesapart_id,
            'mesa_id': self.mesa_id,
            'usuario_id': self.usuario_id,
            'personagem_id': self.personagem_id,
            'tip_usuario': self.tip_usuario,
            'ent_part': self.ent_part,
            'sai_part': self.sai_part,
            'ini_mesa': self.ini_mesa,
            'fim_mesa': self.fim_mesa
        }

    @classmethod
    def find_mesapart(cls, mesapart_id):
        mesapart = cls.query.filter_by(mesapart_id=mesapart_id).first()
        if mesapart:
            return mesapart

        return None

    @classmethod
    def find_by_mesa_id(cls, mesa_id):
        mesapart = cls.query.filter_by(mesa_id=mesa_id).all()
        if mesapart:
            return mesapart

        return None

    def salvar_mesapart(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_historico(self):
        banco.session.delete(self)
        banco.session.commit()
