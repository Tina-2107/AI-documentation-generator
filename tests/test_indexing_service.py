from pathlib import Path

from app.services.indexing_service import index_repository


def test_index_repository(tmp_path):

    project = tmp_path / "project"

    project.mkdir()

    (project / "main.py").write_text(
        """
def hello():
    pass
"""
    )

    result = index_repository(
        project_path=project,
        project_id="demo"
    )

    assert result["files_indexed"] == 1

    assert result["chunks_created"] == 1