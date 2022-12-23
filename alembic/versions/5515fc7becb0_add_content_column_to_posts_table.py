"""add content column to posts table

Revision ID: 5515fc7becb0
Revises: 6af00fccd14e
Create Date: 2022-12-23 02:41:21.879824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5515fc7becb0'
down_revision = '6af00fccd14e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
