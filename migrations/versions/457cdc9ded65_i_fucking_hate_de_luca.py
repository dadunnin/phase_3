"""I fucking hate De Luca

Revision ID: 457cdc9ded65
Revises: 0dc0074d4a7d
Create Date: 2023-04-10 16:55:02.447248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '457cdc9ded65'
down_revision = '0dc0074d4a7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo',
    sa.Column('photo_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('caption', sa.Text(), nullable=True),
    sa.Column('img', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('photo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('photo')
    # ### end Alembic commands ###
