"""Add last few columns to posts table

Revision ID: b29e4c779b53
Revises: 0412c24d0ef3
Create Date: 2025-06-02 17:57:05.948516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b29e4c779b53'
down_revision: Union[str, None] = '0412c24d0ef3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.add_column('posts', 
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                nullable=False, server_default=sa.text('NOW()')))
    
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'content')
    pass
