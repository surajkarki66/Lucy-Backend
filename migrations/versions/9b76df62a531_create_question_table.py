"""create question table

Revision ID: 9b76df62a531
Revises: 0dcb0e7fa7b6
Create Date: 2022-05-25 19:43:44.333497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b76df62a531'
down_revision = '0dcb0e7fa7b6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('questions',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('question', sa.String(255), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              nullable=False, server_default=sa.text('now()')),
                    sa.Column('updated_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('question')
                    )
                    

def downgrade():
    op.drop_table('questions')
