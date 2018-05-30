"""Added pubs, authors and many-to-many association tables

Revision ID: f2db02c6ea1f
Revises: 
Create Date: 2018-05-30 14:38:51.545570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2db02c6ea1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname_en', sa.String(), nullable=True),
    sa.Column('lastname_en', sa.String(), nullable=True),
    sa.Column('firstname_th', sa.String(), nullable=True),
    sa.Column('lastname_th', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pubs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doi', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('abstract', sa.String(), nullable=True),
    sa.Column('pub_date', sa.Date(), nullable=True),
    sa.Column('citation_count', sa.Integer(), nullable=True),
    sa.Column('detail', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('doi')
    )
    op.create_index(op.f('ix_pubs_title'), 'pubs', ['title'], unique=False)
    op.create_table('pub_author_table',
    sa.Column('pub_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['pub_id'], ['pubs.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pub_author_table')
    op.drop_index(op.f('ix_pubs_title'), table_name='pubs')
    op.drop_table('pubs')
    op.drop_table('authors')
    # ### end Alembic commands ###
