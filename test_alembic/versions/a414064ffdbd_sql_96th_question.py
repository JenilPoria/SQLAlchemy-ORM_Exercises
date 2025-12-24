"""sql_96th_question

Revision ID: a414064ffdbd
Revises: 278ea1889eb1
Create Date: 2025-12-03 19:50:18.707861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a414064ffdbd'
down_revision: Union[str, None] = '278ea1889eb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("bonus",
                    sa.Column("snum", sa.INTEGER(), nullable=True),
                    sa.Column("odate", sa.Date(), nullable=True),
                    sa.Column("amount", sa.Integer(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table("bonus")
