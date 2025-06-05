"""Create Poost Table

Revision ID: 117c1cfc1bce
Revises: 
Create Date: 2025-06-02 16:16:13.538924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '117c1cfc1bce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(),nullable = False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )
    pass

def downgrade() -> None:
    op.drop_table('posts')
    """Downgrade schema."""
    pass
