import pytest
import logging
import psycopg2
import os
from datetime import datetime

from sqlalchemy import and_
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

# from onesixpiece import PGAdaptor

logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s- %(message)s"
)


given = pytest.mark.parametrize
skipif = pytest.mark.skipif
skip = pytest.mark.skip
xfail = pytest.mark.xfail

postgres_host = "192.168.2.13"               # 数据库地址
postgres_port = "5432"       # 数据库端口
postgres_user = "postgres"              # 数据库用户名
postgres_password = "password"      # 数据库密码
postgres_database = "sandbox"      # 数据库名字
db_string = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"

Base = declarative_base()

class Order(Base):
    __tablename__ = '_order'

    order_id = Column(Integer, primary_key=True)
    customer_name = Column(String(30), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.now())
    # order_items = relationship(
    #     "OrderItem", cascade="all, delete-orphan", backref="order"
    # )

    def __init__(self, customer_name):
        self.customer_name = customer_name


class Item(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True)
    description = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, description, price):
        self.description = description
        self.price = price
    
    def setID(self, id):
        self.item_id = id

    def __repr__(self):
        return "Item(%r, %r)" % (self.description, self.price)

# @pytest.mark.usefixtures("connect_pg")
class TestSQLAlchemyClass:
    @pytest.fixture(scope="module")
    def session(self):
        engine = create_engine(db_string)
        Base.metadata.create_all(engine)
        session = Session(engine)
        yield session
        # session.delete()
        logging.info("Team down")


    def test_connect(self, session):
        logging.info("start to run test_connect")
        assert session is not None

    def test_insertdata(self, session):
        tshirt, mug, hat, crowbar = (
            Item("SA T-Shirt", 10.99),
            Item("SA Mug", 6.50),
            Item("SA Hat", 8.99),
            Item("MySQL Crowbar", 16.99),
        )
        session.add_all([tshirt, mug, hat, crowbar]) 
        session.commit()

        order = Order("john smith")
        session.add(order)
        session.commit()

    def test_updatedata(self,session):
        first_item = session.query(Item).filter(Item.item_id == 1).update({"description": "Galaxy T Shirt!"})
        logging.info(first_item)
        session.commit()
    # def test_delete(self):
    #     assert True


    def test_deletedata(self, session):
        todelete_item = session.query(Item).filter(Item.description == 'SA T-Shirt').delete()
        logging.info(todelete_item)
        session.commit()
# if __name__ == '__main__':
#     pytest.main(args=['-s', os.path.abspath(__file__)])
