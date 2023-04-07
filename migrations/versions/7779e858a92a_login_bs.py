"""login bs

Revision ID: 7779e858a92a
Revises: ac6bd1805836
Create Date: 2023-04-05 16:31:49.442264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7779e858a92a'
down_revision = 'ac6bd1805836'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
