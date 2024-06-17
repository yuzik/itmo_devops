import os

c = get_config()  # noqa

c.JupyterHub.db_url = f"postgresql://postgres:abobus@database-service:5432/postgres"