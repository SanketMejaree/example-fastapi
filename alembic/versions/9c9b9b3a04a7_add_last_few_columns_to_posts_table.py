"""add last few columns to posts table

Revision ID: 9c9b9b3a04a7
Revises: 9005c12167e1
Create Date: 2022-12-23 04:01:18.678692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c9b9b3a04a7'
down_revision = '9005c12167e1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default='True'))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts", "created_at")
    pass
