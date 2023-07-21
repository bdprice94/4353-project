"""Encrypt passwords

Revision ID: 6fb64fbdd269
Revises: 3801acca22d7
Create Date: 2023-07-21 13:29:03.677706

"""
from alembic import op
import sqlalchemy as sa
from app.models import UserCredentials
import bcrypt


# revision identifiers, used by Alembic.
revision = '6fb64fbdd269'
down_revision = '3801acca22d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    usercredentals = conn.execute(sa.select(UserCredentials)).all()
    conn.commit()
    op.drop_column("usercredentials", "password")
    op.add_column("usercredentials", sa.Column("password", sa.LargeBinary))
    for uc in usercredentals:
        conn.execute(
            sa.update(UserCredentials)
            .values(password=bcrypt.hashpw(uc.password.encode('utf-8'), bcrypt.gensalt()))
            .where(UserCredentials.id == uc.id)
        )
        conn.commit()

def downgrade() -> None:
    pass
