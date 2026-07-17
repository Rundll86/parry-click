from pydantic import BaseModel
import os

FILE_NAME = "parry-click.json"


class ConfigModel(BaseModel):
    port: int
    hwnd_max_retry: int
    allow_stdout: bool


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf8") as f:
        f.write(
            ConfigModel(
                port=25565,
                hwnd_max_retry=30,
                allow_stdout=False,
            ).model_dump_json(indent=4)
        )
with open(FILE_NAME, encoding="utf8") as f:
    config = ConfigModel.model_validate_json(f.read())
