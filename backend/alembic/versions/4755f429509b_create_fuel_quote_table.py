"""create fuel quote table

Revision ID: 4755f429509b
Revises: 5e472be92e79
Create Date: 2023-07-13 19:53:36.623966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4755f429509b'
down_revision = '5e472be92e79'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "fuelquote",
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column("gallons_requested", sa.Numeric, nullable=False),
        sa.Column("delivery_address", sa.String, nullable=False),
        sa.Column("delivery_date", sa.Date, nullable=False),
        sa.Column("suggested_price", sa.Numeric, nullable=False),
        sa.Column("total_amount_due", sa.Numeric, nullable=False),
    )
    pass


def downgrade() -> None:
    pass
