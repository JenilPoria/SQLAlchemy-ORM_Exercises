"""sql_94th_question

Revision ID: 3f175e3d8695
Revises: 48672eba12de
Create Date: 2025-12-03 12:17:50.185802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f175e3d8695'
down_revision: Union[str, None] = '48672eba12de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Sjpeople",
                    sa.Column("snum", sa.INTEGER(), nullable=True),
                    sa.Column("sname", sa.TEXT(), nullable=True),
                    sa.Column("city", sa.TEXT(), nullable=True),
                    sa.Column("comm", sa.REAL(), nullable=True)
                    )


def downgrade() -> None:
    op.drop_table("Sjpeople")
