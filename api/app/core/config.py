import os


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


API_V1_STR = "/v1"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
BACKEND_CORS_ORIGINS = "http://localhost:3000,https://atme.solufit.net, {}".format(os.getenv(
    "BACKEND_CORS_ORIGINS")
)  # a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000, http://localhost:8080, http://dev.couchbase-project.com, https://stag.couchbase-project.com, https://couchbase-project.com, http://local.dockertoolbox.tiangolo.com"
PROJECT_NAME = "at-me Backend API"
DESCRIPTION = """@Me backend API 

create by sasanqua-create & Walkmana-25

Repo URL: https://github.com/solufit/at-me/

Copyright (c) 2024 Solufit
This software is released under MIT License
https://github.com/solufit/at-me/raw/main/LICENSE
"""
VERSION = "0.0.1"