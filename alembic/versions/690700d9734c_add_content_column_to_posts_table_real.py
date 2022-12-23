"""add content column to posts table real

Revision ID: 690700d9734c
Revises: 5515fc7becb0
Create Date: 2022-12-23 02:57:31.147475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690700d9734c'
down_revision = '5515fc7becb0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
