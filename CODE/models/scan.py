from app import DB

class Scan(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True)

    filename = DB.Column(DB.String(200))

    vulnerability = DB.Column(DB.String(300))

    severity = DB.Column(DB.String(50))

    recommendation = DB.Column(DB.Text)