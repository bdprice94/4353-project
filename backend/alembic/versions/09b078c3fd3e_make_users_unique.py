"""Make Users unique

Revision ID: 09b078c3fd3e
Revises: 1b10ec398306
Create Date: 2023-07-04 12:09:24.328947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09b078c3fd3e'
down_revision = '1b10ec398306'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint('unique_username', 'users', ['username'])

    pass


def downgrade() -> None:
    # We don't really need these tbh
    op.drop_table('users')
    pass
