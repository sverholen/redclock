from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.sql.schema import (
    Column as dbColumn
)
from sqlalchemy.sql.sqltypes import (
    Integer as dbInteger
)

from sqlalchemy_utils import UUIDType as dbUUID

Base = declarative_base()

class BaseModel(AbstractConcreteBase, Base):

    id = dbColumn(dbInteger, primary_key=True)
    uuid = dbColumn(dbUUID())