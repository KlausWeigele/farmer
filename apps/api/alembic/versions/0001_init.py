"""init schema v1

Revision ID: 0001_init
Revises: 
Create Date: 2025-09-14

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision = '0001_init'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    op.create_table(
        'farm',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    )

    op.create_table(
        'app_user',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('email', sa.Text(), nullable=False, unique=True),
        sa.Column('name', sa.Text()),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    )

    op.create_table(
        'membership',
        sa.Column('user_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('app_user.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('farm_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('farm.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('role', sa.Text(), nullable=False),
    )

    op.create_table(
        'field',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('farm_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('farm.id', ondelete='CASCADE')),
        sa.Column('name', sa.Text()),
        sa.Column('geom', Geometry(geometry_type='MULTIPOLYGON', srid=25832), nullable=False),
        sa.Column('area_ha', sa.Numeric()),
        sa.Column('crs', sa.Text(), server_default=sa.text("'EPSG:25832'")),
        sa.Column('soil_type', sa.Text()),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    )
    op.create_index('idx_field_geom', 'field', ['geom'], postgresql_using='gist')

    op.create_table(
        'task',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('field_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('field.id', ondelete='CASCADE')),
        sa.Column('type', sa.Text(), nullable=False),
        sa.Column('status', sa.Text(), nullable=False, server_default=sa.text("'planned'")),
        sa.Column('due_at', sa.TIMESTAMP(timezone=True)),
        sa.Column('window_score', sa.Numeric()),
        sa.Column('assigned_to', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('app_user.id', ondelete='SET NULL'), nullable=True),
        sa.Column('notes', sa.Text()),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    )

    op.create_table(
        'operation',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('field_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('field.id', ondelete='CASCADE')),
        sa.Column('kind', sa.Text()),
        sa.Column('product', sa.Text()),
        sa.Column('rate_per_ha', sa.Numeric()),
        sa.Column('total_qty', sa.Numeric()),
        sa.Column('weather_json', sa.JSON()),
        sa.Column('performed_at', sa.TIMESTAMP(timezone=True)),
        sa.Column('photos_json', sa.JSON()),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    )

    op.create_table(
        'weather_observation',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('field_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('field.id', ondelete='CASCADE')),
        sa.Column('ts', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('precip_mm', sa.Numeric()),
        sa.Column('wind_gust', sa.Numeric()),
        sa.Column('temp_c', sa.Numeric()),
        sa.Column('rh', sa.Numeric()),
        sa.Column('leaf_wetness_proxy', sa.Numeric()),
    )

    op.create_table(
        'document',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('field_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('field.id', ondelete='SET NULL'), nullable=True),
        sa.Column('task_id', sa.dialects.postgresql.UUID(as_uuid=True), sa.ForeignKey('task.id', ondelete='SET NULL'), nullable=True),
        sa.Column('type', sa.Text()),
        sa.Column('s3_key', sa.Text(), nullable=False),
        sa.Column('ocr_json', sa.JSON()),
        sa.Column('uploaded_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    )

    # RLS placeholders (disabled in dev)
    # op.execute("ALTER TABLE field ENABLE ROW LEVEL SECURITY")
    # Policies would be added here and toggled per environment


def downgrade() -> None:
    op.drop_table('document')
    op.drop_table('weather_observation')
    op.drop_table('operation')
    op.drop_table('task')
    op.drop_index('idx_field_geom', table_name='field')
    op.drop_table('field')
    op.drop_table('membership')
    op.drop_table('app_user')
    op.drop_table('farm')
