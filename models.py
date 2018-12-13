from sqlalchemy import (
    Sequence,
    Column,
    BigInteger,
    String,
    Boolean,
    Text,
    ForeignKey,
    orm
)

from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    admin = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

    bets = orm.relationship('bets', secondary='bet_to_user', back_populates='users')


class Bet(Base):
    __tablename__ = 'bets'
    id = Column(BigInteger, Sequence('bet_id_seq'), primary_key=True)
    content = Column(Text, nullable=False)

    users = orm.relationship(User, secondary='bet_to_user', back_populates='bets')


class BetToUser(Base):
    __tablename__ = 'bet_to_user'
    user_id = Column(BigInteger, ForeignKey(User.id, onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    bet_id = Column(BigInteger, ForeignKey(Bet.id, onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)

    user = orm.relationship('users')
    bet = orm.relationship('bets')


Base.metadata.create_all(engine)
