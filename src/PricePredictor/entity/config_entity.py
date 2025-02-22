from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class MissingValueHandlingConfig:
    root_dir: Path
    input_data_dir: Path
    processed_data_dir: Path
    categorical_imputation: dict
    numerical_imputation: dict



@dataclass(frozen=True)
class OutlierHandlingConfig:
    root_dir: Path
    input_data_dir: Path
    processed_data_dir: Path
    outlier_id_list: list