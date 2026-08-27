from alembic import op
import sqlalchemy as sa

revision = "004_general_channel"
down_revision = "003_project_read_states"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "projects",
        sa.Column("is_general", sa.Boolean(), nullable=False, server_default=sa.false()),
    )
    op.create_index(
        "uq_projects_one_general_per_org",
        "projects",
        ["organization_id"],
        unique=True,
        postgresql_where=sa.text("is_general IS TRUE"),
    )


def downgrade() -> None:
    op.drop_index("uq_projects_one_general_per_org", table_name="projects")
    op.drop_column("projects", "is_general")
