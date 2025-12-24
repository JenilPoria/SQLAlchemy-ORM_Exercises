"""sql_103th_question

Revision ID: 03a14ff296f0
Revises: a414064ffdbd
Create Date: 2025-12-04 12:45:11.329380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03a14ff296f0'
down_revision: Union[str, None] = 'a414064ffdbd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("multicast",
                    sa.Column("snum", sa.INTEGER(), nullable=True),
                    sa.Column("sname", sa.TEXT(), nullable=True),
                    sa.Column("city", sa.TEXT(), nullable=True),
                    sa.Column("comm", sa.REAL(), nullable=True)
                    )


def downgrade() -> None:
    op.drop_table("multicast")
