"""First revision p2

Revision ID: 4adae57f9667
Revises: fcb1587cb336
Create Date: 2025-12-02 22:56:47.434194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4adae57f9667'
down_revision: Union[str, None] = 'fcb1587cb336'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Londonstaff',
    sa.Column('snum', sa.INTEGER(), nullable=True),
    sa.Column('sname', sa.TEXT(), nullable=True),
    sa.Column('city', sa.TEXT(), nullable=True),
    sa.Column('comm', sa.REAL(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('Londonstaff')
