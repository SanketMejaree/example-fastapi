"""create posts table

Revision ID: 6af00fccd14e
Revises: 
Create Date: 2022-12-23 02:05:03.399229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6af00fccd14e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
