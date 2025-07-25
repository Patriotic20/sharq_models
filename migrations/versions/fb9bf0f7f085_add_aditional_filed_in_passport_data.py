"""Add aditional filed in passport_data

Revision ID: fb9bf0f7f085
Revises: 05d27f5e2096
Create Date: 2025-07-12 12:26:47.375117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb9bf0f7f085'
down_revision: Union[str, None] = '05d27f5e2096'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('passport_data', sa.Column('citizenship', sa.String(), nullable=False))
    op.add_column('passport_data', sa.Column('nationality', sa.String(), nullable=False))
    op.add_column('passport_data', sa.Column('country', sa.String(), nullable=False))
    op.add_column('passport_data', sa.Column('region', sa.String(), nullable=False))
    op.add_column('passport_data', sa.Column('district', sa.String(), nullable=False))
    op.add_column('passport_data', sa.Column('address', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('passport_data', 'address')
    op.drop_column('passport_data', 'district')
    op.drop_column('passport_data', 'region')
    op.drop_column('passport_data', 'country')
    op.drop_column('passport_data', 'nationality')
    op.drop_column('passport_data', 'citizenship')
    # ### end Alembic commands ###
