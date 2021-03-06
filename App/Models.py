from App.main.Extensions import db;

class User(db.Model):
    __tablename__ = 'user';
    id = db.Column(db.Integer, primary_key=True, autoincrement=True);
    username = db.Column(db.String(100),nullable = False);
    age = db.Column(db.Integer, autoincrement=True);

class Article(db.Model):
    __tablename__ = 'article';
    id = db.Column(db.Integer,primary_key = True,autoincrement = True);
    title = db.Column(db.String(100),nullable = False );
    content = db.Column(db.Text, nullable = False );
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'));
    author = db.relationship('User', backref=db.backref('articles'))

