"""add_foreign_key_to_queries_table

Revision ID: 21f62e4d8cd5
Revises: e85ade217d63
Create Date: 2022-09-15 22:48:49.768803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21f62e4d8cd5'
down_revision = 'e85ade217d63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('queries', sa.Column('intent', sa.String(255), nullable=False))
    op.create_foreign_key('query_intents_fk', source_table="queries", referent_table="intents", local_cols=[
                          'intent'], remote_cols=['title'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('query_intents_fk', table_name="queries")
    op.drop_column('queries', 'intent')
