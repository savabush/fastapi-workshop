from .database import Base
import sqlalchemy as table


class Operation(Base):
    __tablename__ = 'operations'

    id = table.Column(table.Integer, primary_key=True)
    date = table.Column(table.Date)
    kind = table.Column(table.String)
    amount = table.Column(table.Numeric(10, 2))
    description = table.Column(table.String, nullable=True)


