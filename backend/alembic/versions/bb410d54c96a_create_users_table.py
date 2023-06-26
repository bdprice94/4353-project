"""Create users table

Revision ID: bb410d54c96a
Revises: 
Create Date: 2023-06-26 08:23:05.059314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb410d54c96a'
down_revision = None # This HAS to point to a previous migration. We do not have any right now.
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        # Autoincrement is here by default, primary_key is what gives it, i've added it to be explicit
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False)
    )


def downgrade() -> None:
    # We don't really need these tbh
    op.drop_table('users')
