#!/usr/bin/python3
"""Creates a FileStorage instance."""
from models.engine.file_storage import FileStorage
from models import User

storage = FileStorage()
storage.reload()
