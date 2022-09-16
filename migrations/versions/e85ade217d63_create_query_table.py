"""create Query table

Revision ID: e85ade217d63
Revises: 1b158b8428fa
Create Date: 2022-09-15 22:35:19.291155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e85ade217d63'
down_revision = '1b158b8428fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('queries',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.String(500), unique=True, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False), 
                    sa.PrimaryKeyConstraint('id'),
                    )


def downgrade() -> None:
    op.drop_table('queries')
