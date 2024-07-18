from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()

BaseORM = declarative_base(metadata=metadata)
