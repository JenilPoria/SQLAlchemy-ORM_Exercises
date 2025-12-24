"""sql_115th_question

Revision ID: dbde17009102
Revises: 36ef96d90dcd
Create Date: 2025-12-04 23:06:05.300332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbde17009102'
down_revision: Union[str, None] = '36ef96d90dcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    CREATE VIEW IF NOT EXISTS bonus_after_10_times AS
    WITH highest_each_day AS (
        SELECT o.odate, o.snum, o.cnum, o.amount
        FROM "order" o
        WHERE o.amount = (
            SELECT MAX(o2.amount)
            FROM "order" o2
            WHERE o2.odate = o.odate
        )
    ),
    counts AS (
        SELECT snum, COUNT(*) AS times_highest
        FROM highest_each_day
        GROUP BY snum
        HAVING COUNT(*) >= 10
    )
    SELECT s.snum, s.sname, c.times_highest
    FROM counts c
    JOIN salespeople s ON s.snum = c.snum;
    """)


def downgrade() -> None:
    op.execute("DROP VIEW IF EXISTS bonus_after_10_times;")
