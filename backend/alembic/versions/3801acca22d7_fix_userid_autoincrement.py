"""Fix userid autoincrement

Revision ID: 3801acca22d7
Revises: 9aaf36f14d47
Create Date: 2023-07-18 03:03:35.485388

"""
from alembic import op
import sqlalchemy as sa
from app.models import UserCredentials


# revision identifiers, used by Alembic.
revision = '3801acca22d7'
down_revision = '9aaf36f14d47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    session = sa.orm.session.Session(bind=conn)
    max_id = session.query(sa.func.max(UserCredentials.id)).scalar()
    op.execute(f"CREATE SEQUENCE user_id_seq START WITH {max_id + 1}")
    op.execute("ALTER TABLE usercredentials ALTER COLUMN id SET DEFAULT nextval('user_id_seq')")


def downgrade() -> None:
    pass
