class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost/usuarios'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave_secreta'