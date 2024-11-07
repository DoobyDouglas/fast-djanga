from settings.nosqldb.mongodb import MongoDBSettings
from settings.sqldb.postgres import PostgresSettings
from settings.sqldb.mysql import MySQLSettings
from settings.cache.redis import RedisSettings

# Настройки баз данных
postgres_ = PostgresSettings()
mysql_ = MySQLSettings()
mongodb_ = MongoDBSettings()
# Настройки кэша
redis_ = RedisSettings()
