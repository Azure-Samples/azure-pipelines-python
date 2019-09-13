---
page_type: sample
languages:
- python
products:
- azure
description: "This repo contains tested reference examples of using Python with Azure Pipelines."
urlFragment: azure-pipelines-python
---

# azure-pipelines-python

This repo contains tested reference examples of using Python with Azure Pipelines.

## Pipelines

This sample contains several Azure Pipelines for Python developers that showcase useful end-to-end patterns of varying complexity. All pipelines are in the [`.azure-pipelines`](.azure-pipelines) folder and have been fully annotated and validated.

Pipeline results and sample Artifacts for the definitions contained in this repo can be viewed at the following Azure DevOps organization: [az-samples](https://dev.azure.com/az-samples/azure-pipelines-python/_build)

### simple_package

`simple_package` is a pure Python package with no external dependencies. It exists to give just-enough structure to show how to use Azure Pipelines with Python.

#### [0-basic-build](.azure-pipelines/simple_package.0-basic-build.yml)

[![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_package.0-basic-build?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=1&branchName=master)

Build a simple package against a single Python version

Concepts:

- Building for a project contained in a repo subfolder (separate src/tests folders)
- Choosing a Python version
- Installing build dependencies
- Linting ([pylint](https://www.pylint.org/) and [flake8](http://flake8.pycqa.org/en/latest/))
- Running tests ([pytest](https://docs.pytest.org/en/latest/))
- Building a source archive and built distribution
- Capturing build artifacts

#### [1-multi-target](.azure-pipelines/simple_package.1-multi-target.yml)

[![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_package.1-multi-target?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=2&branchName=master)

Build a simple package against multiple Python versions

Concepts:

- Building for multiple Python versions
- Capturing multiple artifacts per build

#### [2-artifacts](.azure-pipelines/simple_package.2-artifacts.yml)

[![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_package.2-artifacts?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=3&branchName=master)

Build a simple package against multiple Python versions, then upload it to Azure Artifacts (private PyPI)

Concepts:

- Setting job dependency order
- Conditionally running pipeline jobs
- Disabling code checkout to control the pipeline environment
- Downloading previously uploaded build artifacts
- Authenticating to Azure Artifacts
- Publishing to a private Artifacts feed

### simple_server

`simple_server` is a minimal Flask application that takes a dependency on `simple_package` from the Azure Artifacts feed. It can be run as a standalone Python application, or can be built as a Docker container image.

#### [0-consume-artifacts](.azure-pipelines/simple_server.0-consume-artifacts.yml)

[![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_server.0-consume-artifacts?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=4&branchName=master)

Build a Python application that has a dependency on a package sourced from Azure Artifacts

Concepts:

- Authenticating to Azure Artifacts for pip
- Installing private dependencies
- Distinguish between Python versions in pytest output

#### [1-docker](.azure-pipelines/simple_server.1-docker.yml)

[![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_server.1-docker?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=5&branchName=master)

Build a Docker image using an application that pulls dependencies from Azure Artifacts

Concepts:

- Customizing the build artifact download path
- Building a containerized Python app with Azure Artifacts
- Using multi-stage builds with pip

## Development

This project has been configured for Python development with [VS Code](https://code.visualstudio.com/) using the following extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Azure Pipelines](https://marketplace.visualstudio.com/items?itemName=ms-azure-devops.azure-pipelines)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

To get started, clone the repo, and run the following commands to get started with a new environment

```sh
# Clone the repo
git clone https://github.com/Azure-Samples/azure-pipelines-python.git
cd azure-pipelines-python

# Create a virtual environment at .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.dev.txt -U --upgrade-strategy eager

# Install packages in editable mode
python -m pip install -e src/simple_package
python -m pip install -e src/simple_server

# Start coding! :)
code .
```

## Resources

- [Build Python apps](https://docs.microsoft.com/en-us/azure/devops/pipelines/languages/python?view=azure-devops)
- [Publish Python packages in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/artifacts/pypi?view=azure-devops&tabs=yaml)
- [Azure Pipelines YAML schema](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema)
