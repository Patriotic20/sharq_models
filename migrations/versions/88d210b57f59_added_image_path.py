"""added image path

Revision ID: 88d210b57f59
Revises: 4a904572b579
Create Date: 2025-07-12 18:21:25.503386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88d210b57f59'
down_revision: Union[str, None] = '4a904572b579'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('passport_data', sa.Column('image_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('passport_data', 'image_path')
    # ### end Alembic commands ###
