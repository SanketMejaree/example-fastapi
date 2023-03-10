"""add user table

Revision ID: 8bf931b3b40a
Revises: 690700d9734c
Create Date: 2022-12-23 03:16:26.151067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bf931b3b40a'
down_revision = '690700d9734c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String, nullable=False), sa.Column('password', sa.String, nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
