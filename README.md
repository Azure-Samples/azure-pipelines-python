# azure-pipelines-python

This repo contains tested reference examples of using Python with Azure Pipelines.

## Pipelines

This sample contains several Azure Pipelines for Python developers that showcase useful end-to-end patterns of varying complexity. All pipelines are in the [`.azure-pipelines`](.azure-pipelines) folder and have been fully annotated and validated.

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

- Disabling code checkout to control the pipeline environment
- Downloading previously uploaded build artifacts
- Authenticating to Azure Artifacts
- Publishing to a private Artifacts feed


## Development

This project has been configured for Python development with [VS Code](https://code.visualstudio.com/) using the following extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Azure Pipelines](https://marketplace.visualstudio.com/items?itemName=ms-azure-devops.azure-pipelines)

To get started, clone the repo, and run the following commands to get started with a new environment

```sh
# Clone the repo
git clone https://github.com/Azure-Samples/azure-pipelines-python.git
cd azure-pipelines-python

# Create a virtual environment at .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.dev.txt -U --upgrade-strategy eager

# Start coding! :)
code .
```

## Resources

- [Build Python apps](https://docs.microsoft.com/en-us/azure/devops/pipelines/languages/python?view=azure-devops)
- [Publish Python packages in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/artifacts/pypi?view=azure-devops&tabs=yaml)
- [Azure Pipelines YAML schema](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema)