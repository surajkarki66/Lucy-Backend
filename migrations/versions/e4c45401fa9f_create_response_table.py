"""Create response table

Revision ID: e4c45401fa9f
Revises: 21f62e4d8cd5
Create Date: 2022-09-16 09:44:22.742979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c45401fa9f'
down_revision = '21f62e4d8cd5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('responses',
                    sa.Column('id', sa.String(), nullable=False),
                    sa.Column('text', sa.String(1000), unique=True, nullable=False),
                    sa.Column('link', sa.String(255), nullable=True),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False), 
                    sa.PrimaryKeyConstraint('id'),
                    )


def downgrade() -> None:
    op.drop_table('responses')