"""sql_112th_question

Revision ID: 86de4bd53ccf
Revises: 00a23ec697a3
Create Date: 2025-12-04 18:31:48.722356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86de4bd53ccf'
down_revision: Union[str, None] = '00a23ec697a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
                create view if not exists orderswithnames as
                  select o.onum, s.sname as salesperson_name, c.cname as customer_name, o.odate, o.amount 
                  from "order" o join salesperson s on o.snum = s.snum
                  join customer c on o.cnum = c.cnum; 
""")


def downgrade() -> None:
    op.execute("drop view orderswithnames;")
