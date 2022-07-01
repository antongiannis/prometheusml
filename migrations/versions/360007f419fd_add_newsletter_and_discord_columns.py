"""Add newsletter and discord columns

Revision ID: 360007f419fd
Revises: 877e02254954
Create Date: 2022-04-29 13:55:42.313547

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "360007f419fd"
down_revision = "877e02254954"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column(
            "register_timestamp",
            sa.DateTime(),
            nullable=True,
            server_default=sa.func.now(),
        ),
    )
    op.add_column(
        "user",
        sa.Column(
            "register_newsletter", sa.Boolean(), nullable=False, server_default="true"
        ),
    )
    op.add_column(
        "user",
        sa.Column(
            "register_discord", sa.Boolean(), nullable=False, server_default="true"
        ),
    )
    op.alter_column(
        "user", "password_hash", existing_type=sa.VARCHAR(length=128), nullable=False
    )
    op.create_index(
        op.f("ix_user_register_timestamp"), "user", ["register_timestamp"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_register_timestamp"), table_name="user")
    op.alter_column(
        "user", "password_hash", existing_type=sa.VARCHAR(length=128), nullable=True
    )
    op.drop_column("user", "register_discord")
    op.drop_column("user", "register_newsletter")
    op.drop_column("user", "register_timestamp")
    # ### end Alembic commands ###
