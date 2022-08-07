from .database import Base
import sqlalchemy as table


class User(Base):
    __tablename__ = 'users'

    id = table.Column(table.Integer, primary_key=True)
    email = table.Column(table.Text, unique=True)
    username = table.Column(table.Text, unique=True)
    password_hash = table.Column(table.Text)


class Operation(Base):
    __tablename__ = 'operations'

    id = table.Column(table.Integer, primary_key=True)
    user_id = table.Column(table.Integer, table.ForeignKey('users.id'))
    date = table.Column(table.Date)
    kind = table.Column(table.String)
    amount = table.Column(table.Numeric(10, 2))
    description = table.Column(table.String, nullable=True)
