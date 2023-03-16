"""add_hire_statistics

Revision ID: c3c6f73e81b4
Revises: 991ecb2bf269
Create Date: 2023-03-16 01:33:48.129842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3c6f73e81b4'
down_revision = '991ecb2bf269'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hire_statistics',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('standard_job_id', sa.String(), nullable=True),
    sa.Column('country_code', sa.String(), nullable=True),
    sa.Column('min_days_to_hire', sa.Integer(), nullable=True),
    sa.Column('max_days_to_hire', sa.Integer(), nullable=True),
    sa.Column('avg_days_to_hire', sa.Integer(), nullable=True),
    sa.Column('num_postings', sa.Integer(), nullable=False),
    sa.Column('calculation_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hire_statistics', schema='public')
    # ### end Alembic commands ###