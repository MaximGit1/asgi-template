from dataclasses import dataclass
from os import getenv
from typing import TypeVar


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    user: str
    password: str
    host: str
    port: int
    db_name: str
    debug: bool

    @property
    def uri(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


@dataclass(frozen=True, slots=True)
class APIConfig:
    host: str
    port: int


@dataclass(frozen=True, slots=True)
class Config:
    db: PostgresConfig
    app: APIConfig


def init_postgres_config() -> PostgresConfig:
    return PostgresConfig(
        user=get_arg("POSTGRES_USER", str),
        password=get_arg("POSTGRES_PASSWORD", str),
        host=get_arg("POSTGRES_HOST", str),
        port=get_arg("POSTGRES_PORT", int),
        db_name=get_arg("POSTGRES_DB", str),
        debug=get_arg("POSTGRES_DEBUG", bool),
    )


def init_api_config() -> APIConfig:
    return APIConfig(
        host=get_arg("UVICORN_HOST", str),
        port=get_arg("UVICORN_PORT", int),
    )


def init_config() -> Config:
    return Config(
        db=init_postgres_config(),
        app=init_api_config(),
    )


# Working with environment variables

T = TypeVar("T", str, int, float, bool)


def get_arg(arg_name: str, arg_type: type[T]) -> T:
    return _convert_arg(
        arg=_get_env_arg(arg_name),
        type_=arg_type,
    )


def _convert_arg(arg: str, type_: type[T]) -> T:
    error_msg = f"Unsupported argument type: {arg}"

    if type_ is str:
        return arg  # type: ignore
    if type_ is int:
        return int(arg)  # type: ignore
    if type_ is float:
        return float(arg)  # type: ignore
    if type_ is bool:
        lower_arg = arg.lower()
        if lower_arg in ("true", "1", "yes"):
            return True  # type: ignore
        if lower_arg in ("false", "0", "no"):
            return False  # type: ignore

    raise ValueError(error_msg)

def _get_env_arg(env_name: str) -> str:
    if not (env_value := getenv(env_name)):
        error_msg = f'Environment variables "{env_name}" - not loaded or missing.'
        raise KeyError(error_msg)
    return env_value
