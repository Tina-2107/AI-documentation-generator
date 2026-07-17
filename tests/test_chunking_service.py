from pathlib import Path

from app.services.chunking_service import chunk_python_file,create_chunk_id

#This tests whether your chunking logic works correctly.
def test_chunk_python_file(tmp_path):
    project_root = tmp_path

    python_file = project_root / "sample.py"

    python_file.write_text(
        """
def add(a,b):
    return a+b

class User:
    pass
"""
    )

    chunks = chunk_python_file(
        python_file,
        project_root,
        "sample_project"
    )

    assert len(chunks) == 2

    names = {
        chunk.metadata["symbol_name"]
        for chunk in chunks
    }

    assert "add" in names
    assert "User" in names
    
# Deterministic IDs
def test_chunk_id_is_deterministic():

    id1 = create_chunk_id(
        "project",
        "main.py",
        "function",
        "add",
        "def add(): pass"
    )

    id2 = create_chunk_id(
        "project",
        "main.py",
        "function",
        "add",
        "def add(): pass"
    )

    assert id1 == id2
    #Changing content changes ID
def test_chunk_id_changes_when_content_changes():

    id1 = create_chunk_id(
        "project",
        "main.py",
        "function",
        "add",
        "def add(): pass"
    )

    id2 = create_chunk_id(
        "project",
        "main.py",
        "function",
        "add",
        "def add(): return 5"
    )

    assert id1 != id2