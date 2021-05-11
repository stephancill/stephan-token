"""Add accounts

Revision ID: 9589abd6b259
Revises: 
Create Date: 2021-05-11 16:58:57.588850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9589abd6b259'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('twitter_id', sa.String(), nullable=True),
    sa.Column('eth_address', sa.String(), nullable=True),
    sa.Column('balance', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###
