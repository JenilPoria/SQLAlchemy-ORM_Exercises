"""sql_113th_question

Revision ID: f051c1835884
Revises: a02f58c83e86
Create Date: 2025-12-04 18:55:12.885910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f051c1835884'
down_revision: Union[str, None] = 'a02f58c83e86'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
            create view if not exists axelrods_data as
                  select o.*, s.comm from "order" o join salespeople s on o.snum = s.snum where s.sname = "Axelrod"; 

""")


def downgrade() -> None:
    op.execute("drop view axelrods_data;")
