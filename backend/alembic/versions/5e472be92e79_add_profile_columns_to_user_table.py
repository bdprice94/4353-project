"""add profile columns to user table

Revision ID: 5e472be92e79
Revises: 09b078c3fd3e
Create Date: 2023-07-09 18:03:19.553250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e472be92e79'
down_revision = '09b078c3fd3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
     
    op.add_column('users', sa.Column('full_name', sa.String(50) ))
    op.add_column('users', sa.Column('address_1', sa.String(100) ))
    op.add_column('users', sa.Column('address_2', sa.String(100)))
    op.add_column('users', sa.Column('city', sa.String(100)))
    op.add_column('users', sa.Column('state', sa.String(2)))
    op.add_column('users', sa.Column('zipcode', sa.Integer(9)))

    pass


def downgrade() -> None:
    pass
