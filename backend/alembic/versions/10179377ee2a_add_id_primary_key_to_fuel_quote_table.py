"""add id primary key to fuel quote table

Revision ID: 10179377ee2a
Revises: 4755f429509b
Create Date: 2023-07-14 08:52:16.390772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10179377ee2a'
down_revision = '4755f429509b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "fuelquote",
        sa.Column("id", sa.Integer, nullable=False)
    )
    op.execute("CREATE SEQUENCE fuelquote_id_seq START WITH 1")
    op.execute("ALTER TABLE fuelquote ALTER COLUMN id SET DEFAULT nextval('fuelquote_id_seq')")
    op.create_primary_key("pk_fuelquote", "fuelquote", ["id"])


def downgrade() -> None:
    pass
