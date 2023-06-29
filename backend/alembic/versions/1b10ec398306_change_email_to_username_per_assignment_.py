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
    op.create_table(
        'users',
        # Autoincrement is here by default, primary_key is what gives it, i've added it to be explicit
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False)
    )
    pass


def downgrade() -> None:
    # We don't really need these tbh
    op.drop_table('users')
    pass
