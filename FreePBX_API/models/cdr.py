import connection.init as app

class Cdr(app.db.Model):
    __tablename__ = 'cdr'
    calldate = app.db.Column(app.db.DateTime, primary_key=True)
    src = app.db.Column(app.db.String(80))
    dst = app.db.Column(app.db.String(80), index=True)
    duration = app.db.Column(app.db.Integer)
    disposition = app.db.Column(app.db.String(45))

    def to_dict(self):
        return {
            'calldate': self.calldate.strftime('%Y-%m-%d %H:%M:%S'),
            'src': self.src,
            'dst': self.dst,
            'duration': self.duration,
            'disposition': self.disposition
        }
