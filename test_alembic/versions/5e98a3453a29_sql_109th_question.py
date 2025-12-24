"""sql_109th_question

Revision ID: 5e98a3453a29
Revises: a1cf23baa8f0
Create Date: 2025-12-04 16:22:15.237139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e98a3453a29'
down_revision: Union[str, None] = 'a1cf23baa8f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE VIEW LondonStaffView AS
        SELECT *
        FROM salespeople
        WHERE city = 'London';
    """)

def downgrade() -> None:
    op.execute("DROP VIEW LondonStaffView;")
