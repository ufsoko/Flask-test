
def init_db_conf(envinfo):
    dialect = envinfo.get("DIALECT") or "sqlite"
    driver = envinfo.get("DRIVER") or "sqlite"
    user = envinfo.get("USER") or ""
    password = envinfo.get("PASSWORD") or ""
    host = envinfo.get("HOST") or ""
    port = envinfo.get("PORT") or ""
    name = envinfo.get("NAME") or "sqlite.db"
    return "{}+{}://{}:{}@{}/{}".format(dialect,driver,user,password,host,name)

class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(Config):
    DEBUG = True
    envinfo = {}
    SQLALCHEMY_DATABASE_URI = init_db_conf(envinfo)


class TestingConfig(Config):
    TESTING = True
    envinfo = {
        "DIALECT":"mysql",
        "DRIVER":"mysqldb",
        "USER":"root",
        "PASSWORD":"123456",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"flask_test"
    }
    SQLALCHEMY_DATABASE_URI = init_db_conf(envinfo)

envs = {
    "develop":DevelopConfig,
    "testing":TestingConfig,
    "default":DevelopConfig
}