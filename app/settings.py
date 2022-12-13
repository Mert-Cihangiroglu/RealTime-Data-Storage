# app/settings.py
#Before we jump into the implementation, we must configure Celery. 
# To create a configuration used by both the workers and the dashboard, create a settings.py file in the app package. 
# We will use pydantic's BaseSettings to define the configuration. This helps us to read the settings from a .env file, environment variable, and prefix them if needed.
# Ensuring that we do not overwrite any other environment variables, we will set the prefix to SMD which stands for "stock market dashboard". 
# Below you can see the settings file:
# In the settings, you can notice we already defined the celery_broker and database_url settings with unusual default values.
# Some bits are missing at the moment. We still have to define the correct settings and run the worker in a Docker container. Get started with the settings!
# To keep our environment separated, we will use a .env file. One of pydantic based settings' most significant advantage is that it can read environment variables from .env files.

from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings of the application, used by workers and dashboard.
    """

    # Celery settings
    celery_broker: str = "redis://127.0.0.1:6379/0"

    # Database settings
    database_url: str = "postgresql://admin:quest@127.0.0.1:8812/qdb"
    database_pool_size: int = 3

    # Finnhub settings
    api_key: str = ""
    frequency: int = 5  # default stock data fetch frequency in seconds
    symbols: List[str] = list()

    # Dash/Plotly
    debug: bool = True
    graph_interval: int = 10

    class Config:
        """
        Meta configuration of the settings parser.
        """

        env_file = ".env"
        # Prefix the environment variable not to mix up with other variables
        # used by the OS or other software.
        env_prefix = "SMD_"  # SMD stands for Stock Market Dashboard


settings = Settings()