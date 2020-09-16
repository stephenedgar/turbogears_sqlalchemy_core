from tg import expose, request, flash

from xispike.lib.base import BaseController
from xispike import model

import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

__all__ = ['XiDataController']

class XiDataController(BaseController):

  def setup_db(self):
    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata = MetaData()
    users = Table('users', metadata,
      Column('id', Integer, primary_key=True),
      Column('name', String),
      Column('fullname', String),
    )

    addresses = Table('addresses', metadata,
      Column('id', Integer, primary_key=True),
      Column('user_id', None, ForeignKey('users.id')),
      Column('email_address', String, nullable=False)
    )

    metadata.create_all(engine)

  @expose()
  def index(self):
    print(sqlalchemy.__version__)
    self.setup_db()
    """Handle the index page"""




