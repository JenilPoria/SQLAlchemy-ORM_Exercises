"""sql_110th_question

Revision ID: 789264abf5de
Revises: 5e98a3453a29
Create Date: 2025-12-04 17:38:29.359321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '789264abf5de'
down_revision: Union[str, None] = '5e98a3453a29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""create view if not exists ratingcounts as 
                  select rating, count(*) as countcol from customer group by rating;""")


def downgrade() -> None:
    op.execute("drop view ratingcounts")
