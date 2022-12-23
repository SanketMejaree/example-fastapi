"""add foreign key to posts table

Revision ID: 9005c12167e1
Revises: 8bf931b3b40a
Create Date: 2022-12-23 03:49:40.515228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9005c12167e1'
down_revision = '8bf931b3b40a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.add_column("posts", "owner_id")
    pass
