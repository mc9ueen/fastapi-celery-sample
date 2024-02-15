"""empty message

Revision ID: 97b6372b117a
Revises: 05fd4c5b313d
Create Date: 2024-02-15 09:50:14.474545

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "97b6372b117a"
down_revision = "05fd4c5b313d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=128), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###