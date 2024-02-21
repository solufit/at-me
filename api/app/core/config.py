import os


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


API_V1_STR = "/v1"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
BACKEND_CORS_ORIGINS = "http://localhost:8080, {}".format(os.getenv(
    "BACKEND_CORS_ORIGINS")
)  # a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000, http://localhost:8080, http://dev.couchbase-project.com, https://stag.couchbase-project.com, https://couchbase-project.com, http://local.dockertoolbox.tiangolo.com"
PROJECT_NAME = "at-me Internal API"
DESCRIPTION = "at-me Internal API"
VERSION = "0.0.1"