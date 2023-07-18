"""Rename DB tables for requirements

Revision ID: 9aaf36f14d47
Revises: beb572ba8aa3
Create Date: 2023-07-18 00:30:22.674377

"""
from alembic import op
import sqlalchemy as sa
from app.database import Base


# revision identifiers, used by Alembic.
revision = '9aaf36f14d47'
down_revision = 'beb572ba8aa3'
branch_labels = None
depends_on = None


class OldUser(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer)
    username = sa.Column(sa.String)
    password = sa.Column(sa.String)
    full_name = sa.Column(sa.String)
    address_1 = sa.Column(sa.String)
    address_2 = sa.Column(sa.String)
    city = sa.Column(sa.String)
    state = sa.Column(sa.String)
    zipcode = sa.Column(sa.Integer)


def upgrade() -> None:
    op.create_table("usercredentials",
                    sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
                    sa.Column("username", sa.String, unique=True, index=True),
                    sa.Column("password", sa.String),
                    )

    op.create_table("clientinformation",
                    sa.Column("full_name", sa.String(50)),
                    sa.Column("address_1", sa.String(100)),
                    sa.Column("address_2", sa.String(100)),
                    sa.Column("city", sa.String(100)),
                    sa.Column("state", sa.String(2)),
                    sa.Column("zipcode", sa.Integer),
                    sa.Column("userid", sa.ForeignKey("usercredentials.id"),
                              primary_key=True)
                    )
    conn = op.get_bind()
    res = conn.execute(
        sa.select(OldUser)
    ).fetchall()
    for id, username, password, full_name, address_1, address_2, city, state, zipcode in res:
        op.execute(f"INSERT INTO usercredentials (id, username, password) VALUES ({id}, {username}, {password})")
        op.execute("INSERT INTO clientinformation (full_name, address_1, address_2, city, state, zipcode, userid) "
                   f"VALUES ({full_name}, {address_1}, {address_2}, {city}, {state}, {zipcode}, {id})")

    op.drop_table("users")


def downgrade() -> None:
    pass
