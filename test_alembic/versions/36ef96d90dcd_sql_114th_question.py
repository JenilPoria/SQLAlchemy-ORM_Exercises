"""sql_114th_question

Revision ID: 36ef96d90dcd
Revises: f051c1835884
Create Date: 2025-12-04 20:09:12.043156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36ef96d90dcd'
down_revision: Union[str, None] = 'f051c1835884'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
            create view if not exists bonus_salespeople as
                  select o.onum, o.odate, o.amount, s.sname as salespeople_name, c.cname as customer_name
                  from "order" o join salespeople s on o.snum = s.snum join customer c on o.cnum = c.cnum 
                  where o.amount = (select max(o2.amount) from "order" o2 where o2.date = o.odate);
                  """)


def downgrade() -> None:
    op.execute("drop view bonus_salespeople;")
