"""sql_89th_question

Revision ID: 48672eba12de
Revises: 4adae57f9667
Create Date: 2025-12-02 23:27:00.572474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48672eba12de'
down_revision: Union[str, None] = '4adae57f9667'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("DayTotals",
                    sa.Column("data", sa.Date(), nullable=False),
                    sa.Column("total_sales", sa.Float(), nullable=True)
                    )


def downgrade() -> None:
    op.drop_table("DayTotals")
