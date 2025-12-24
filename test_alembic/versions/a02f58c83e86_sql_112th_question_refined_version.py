"""sql_112th_question(refined_version)

Revision ID: a02f58c83e86
Revises: 86de4bd53ccf
Create Date: 2025-12-04 18:40:06.347271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a02f58c83e86'
down_revision: Union[str, None] = '86de4bd53ccf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
                create view if not exists orderswithnames as
                  select o.onum, s.sname as salesperson_name, c.cname as customer_name, o.odate, o.amount 
                  from "order" o join salespeople s on o.snum = s.snum
                  join customer c on o.cnum = c.cnum; 
""")


def downgrade() -> None:
    op.execute("drop view orderswithnames;")
