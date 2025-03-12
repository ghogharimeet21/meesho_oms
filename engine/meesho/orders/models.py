from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    order_date = Column(Date, nullable=False)
    sub_order_no = Column(String, nullable=False)
    packet_id = Column(String, nullable=False)
    size = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    sku = Column(String, nullable=True)
    supplier_price = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Order(product_name={self.product_name}, order_date={self.order_date})>"
