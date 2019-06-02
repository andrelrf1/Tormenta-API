from sql_alchemy import banco


class ModelMesaPart(banco.Model):
    __tablename__ = 'mesapart'

    mesapart_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True, unique=True)
    usuario_id = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario_id'), nullable=False)
    personagem_id = banco.Column(banco.Integer, banco.ForeignKey('personagem.personagem_id'), nullable=False)
    mesa_id = banco.Column(banco.Integer, banco.ForeignKey('mesa.mesa_id'), nullable=False)

    def __init__(self, usuario_id, personagem_id, mesa_id):
        self.usuario_id = usuario_id
        self.personagem_id = personagem_id
        self.mesa_id = mesa_id

    def json(self):
        return {
            'mesapart_id': self.mesapart_id,
            'usuario_id': self.usuario_id,
            'personagem_id': self.personagem_id,
            'mesa_id': self.mesa_id
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
