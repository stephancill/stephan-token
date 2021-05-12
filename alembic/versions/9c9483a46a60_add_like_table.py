"""Add Like table

Revision ID: 9c9483a46a60
Revises: 3dd83c7048b9
Create Date: 2021-05-12 17:22:26.848309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c9483a46a60'
down_revision = '3dd83c7048b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('like',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('account_id', sa.INTEGER(), nullable=False),
    sa.Column('tweet_id', sa.String(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    # ### end Alembic commands ###
