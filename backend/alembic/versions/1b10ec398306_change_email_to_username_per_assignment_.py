"""Change email to username per Assignment 2 docs

Revision ID: 1b10ec398306
Revises: bb410d54c96a
Create Date: 2023-06-28 21:10:23.343035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b10ec398306'
down_revision = 'bb410d54c96a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'email', nullable=False,
                    new_column_name='username')

    pass


def downgrade() -> None:
    # We don't really need these tbh
    op.drop_table('users')
    pass
