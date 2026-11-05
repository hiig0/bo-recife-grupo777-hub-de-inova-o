"""add descricao to projetos

Revision ID: 3eda222e4e8f
Revises: fc4d5b8ee310
Create Date: 2026-11-04 22:48:00.928907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3eda222e4e8f'
down_revision: Union[str, Sequence[str], None] = 'fc4d5b8ee310'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("projetos", sa.Column("descricao", sa.String(), nullable=True))


def downgrade():
    op.drop_column("projetos", "descricao")