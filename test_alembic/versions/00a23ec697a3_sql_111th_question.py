"""sql_111th_question

Revision ID: 00a23ec697a3
Revises: 789264abf5de
Create Date: 2025-12-04 18:24:58.445946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00a23ec697a3'
down_revision: Union[str, None] = '789264abf5de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        create view if not exists dailyordersummary as 
                  select odate, count(distinct snum) as num_salespeople, count(*) as num_orders,
                  avg(amount) as avg_amount, sum(amount) as total_amount from "order" group by odate;
    """)


def downgrade() -> None:
    op.execute("drop view dailyordersummary")
