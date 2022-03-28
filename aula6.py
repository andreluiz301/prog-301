"""
class Casa(db.Model):

    id = db.Column(db.Integer, primary-key=True)
    formato = db.Column(db.String(254))


class Quarto(db.Model):

    id = db.Column(db.Integer, primary-key=True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column( " )

    casa_id = db.Column(db.Integer, ForeignKey(Casa.id), nullable=False)
"""