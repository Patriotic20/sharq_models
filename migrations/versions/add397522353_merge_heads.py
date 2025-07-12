"""Merge heads

Revision ID: add397522353
Revises: 88d210b57f59, c80adb995e16
Create Date: 2025-07-12 21:08:24.633852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add397522353'
down_revision: Union[str, None] = ('88d210b57f59', 'c80adb995e16')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
