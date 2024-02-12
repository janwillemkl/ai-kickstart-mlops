"""Ames Housing price prediction model."""

from dagster import Definitions
from src.ames_housing.constants import (
    AMES_HOUSING_DATA_SET_SEPARATOR,
    AMES_HOUSING_DATA_SET_URL,
    DATA_BASE_DIR,
    MODEL_BASE_DIR,
)

from ames_housing.assets.ames_housing_data import ames_housing_data
from ames_housing.assets.ames_housing_features import ames_housing_features
from ames_housing.assets.price_prediction_model import price_prediction_model
from ames_housing.assets.train_test import train_test_data
from ames_housing.io_managers.csv_fs_io_manager import CSVFileSystemIOManager
from ames_housing.io_managers.pickle_fs_io_manager import PickleFileSystemIOManager
from ames_housing.resources.csv_data_set_loader import CSVDataSetLoader

definitions = Definitions(
    assets=[
        ames_housing_data,
        ames_housing_features,
        train_test_data,
        price_prediction_model,
    ],
    resources={
        "ames_housing_data_set_downloader": CSVDataSetLoader(
            path_or_url=AMES_HOUSING_DATA_SET_URL,
            separator=AMES_HOUSING_DATA_SET_SEPARATOR,
        ),
        "csv_fs_io_manager": CSVFileSystemIOManager(base_dir=DATA_BASE_DIR),
        "picke_fs_io_manager": PickleFileSystemIOManager(base_dir=MODEL_BASE_DIR)
    },
)
