from pathlib import Path

from logic.libs.sqliteAlchemy.sqliteAlchemy import Config, setup

from .variables import Vars


def setup_sqlite():

    setup(
        Config(
            url=f'{Path.home()}/.base/db/sqlite.db',
            echo=False,
            path='logic/apps/*/repositories/entities'
        )
    )
