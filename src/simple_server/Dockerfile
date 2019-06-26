# ##########
#
# Build a container image based on a prepackaged application pulled from an Azure Artifacts feed (private PyPI)
#
# We use a multi-stage build to keep artifact feed secrets out of the final image
# If we did not, we would be able to retrieve the secret in plain text by running `docker history`
#
# ##########

# We don't have any glibc dependencies, so we'll use a minimal Alpine image to build
FROM python:3.7-alpine AS builder

# We'll pass in the credentials for pip as a Docker --build-arg
ARG PIP_EXTRA_INDEX_URL

# Copy our application wheel(s) from dist
COPY dist /dist

# Set the PIP_EXTRA_INDEX_URL environment variable for this command, which is used by pip to search for packages
# We want to update pip itself, as to not accidentally log the password during build (requires pip 19.0+)
# We also choose gunicorn as our wsgi host - it's not explicitly defined as a dependency in setup.py
# We install everything with the --user flag, which places packages into ~/.local
# References:
#   * pip environment variable configuration: https://pip.pypa.io/en/stable/user_guide/#environment-variables
#   * pip 19.0 release notes: https://pip.pypa.io/en/stable/news/#id61
RUN PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL \
    pip install -U pip \
    && pip install --user gunicorn \
    && pip install --user dist/*.whl

# For our runtime stage, we want our final image to be small, so we'll use Alpine again
FROM python:3.7-alpine AS app

# We'll copy the packages from ~/.local into our final runtime image
COPY --from=builder /root/.local /root/.local

# We also need to set the PATH so that package commands (gunicorn, flask, etc) will resolve
ENV PATH=/root/.local/bin:$PATH

# We'll expose the port we want to use
EXPOSE 5000

# Use gunicorn to launch our app
CMD ["gunicorn", "-b=:5000", "simple_server:app"]
