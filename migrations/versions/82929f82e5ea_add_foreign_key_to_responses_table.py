"""add_foreign_key_to_responses_table

Revision ID: 82929f82e5ea
Revises: e4c45401fa9f
Create Date: 2022-09-16 10:11:15.782521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82929f82e5ea'
down_revision = 'e4c45401fa9f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('responses', sa.Column('tag', sa.String(255), nullable=False))
    op.create_foreign_key('response_intents_fk', source_table="responses", referent_table="intents", local_cols=[
                          'tag'], remote_cols=['title'], ondelete="CASCADE")



def downgrade() -> None:
    op.drop_constraint('response_intents_fk', table_name="responses")
    op.drop_column('responses', 'tag')
