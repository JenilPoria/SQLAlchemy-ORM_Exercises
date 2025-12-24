"""sql_108th_question

Revision ID: a1cf23baa8f0
Revises: 4b57f2636a9e
Create Date: 2025-12-04 16:05:34.044785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1cf23baa8f0'
down_revision: Union[str, None] = '4b57f2636a9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_snum_rating', ['snum', 'rating'])

def downgrade() -> None:
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_constraint('uq_snum_rating', type_='unique')