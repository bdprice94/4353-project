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
    op.drop_table('users')  # This lets us upgrade without messing with the database directly or over API
    op.create_table(
        'users',
        # Autoincrement is here by default, primary_key is what gives it, i've added it to be explicit
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False)
    )
    pass


def downgrade() -> None:
    # We don't really need these tbh
    op.drop_table('users')
    pass
