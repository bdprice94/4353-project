"""changing delivery date type

Revision ID: beb572ba8aa3
Revises: 10179377ee2a
Create Date: 2023-07-14 15:59:49.329711

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import VARCHAR

# revision identifiers, used by Alembic.
revision = 'beb572ba8aa3'
down_revision = '10179377ee2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name="fuelquote",
        column_name="delivery_date",
        type_=postgresql.VARCHAR,
        postgresql_using="delivery_date::varchar"
    )
    pass


def downgrade() -> None:
    pass
