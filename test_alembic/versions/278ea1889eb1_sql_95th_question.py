"""sql_95th_question

Revision ID: 278ea1889eb1
Revises: 3f175e3d8695
Create Date: 2025-12-03 12:46:18.896671

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '278ea1889eb1'
down_revision: Union[str, None] = '3f175e3d8695'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("samecity",
                    sa.Column("snum", sa.INTEGER(), nullable=True),
                    sa.Column("sname", sa.TEXT(), nullable=True),
                    sa.Column("city", sa.TEXT(), nullable=True),
                    sa.Column("comm", sa.REAL(), nullable=True)
                    )


def downgrade() -> None:
    op.drop_table("samecity")
