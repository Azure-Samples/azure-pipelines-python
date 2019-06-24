# azure-pipelines-python

This repo contains tested reference examples of using Python with Azure Pipelines.

## Scenarios

- Building a package
    - linting
    - running tests
    - building a distribution package
    - uploading to a private Artifacts feed

- Building an application
    - reference package from private Artifacts feed
    - linting
    - running tests
    - build a Docker image

- Python development with VS Code
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Azure Pipelines](https://marketplace.visualstudio.com/items?itemName=ms-azure-devops.azure-pipelines)

## Pipelines

This sample contains several Azure Pipelines for Python developers that showcase useful end-to-end patterns of varying complexity. All pipelines are in the [`.azure-pipelines`](.azure-pipelines) folder and have been fully annotated and validated.

| Status | Name | Description |
| --- | --- | --- |
| [![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_package.0-basic-build?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=1&branchName=master) | [simple_package.0-basic-build](.azure-pipelines/simple_package.0-basic-build.yml) | Build a simple package against a single Python target version |
| [![Build Status](https://dev.azure.com/az-samples/azure-pipelines-python/_apis/build/status/simple_package.1-multi-target?branchName=master)](https://dev.azure.com/az-samples/azure-pipelines-python/_build/latest?definitionId=2&branchName=master) | [simple_package.1-multi-target](.azure-pipelines/simple_package.1-multi-target) | Build a simple package against a multiple Python target versions |

## Development

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.dev.txt -U --upgrade-strategy eager
```

## Resources

- [Build Python apps](https://docs.microsoft.com/en-us/azure/devops/pipelines/languages/python?view=azure-devops)
- [Publish Python packages in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/artifacts/pypi?view=azure-devops&tabs=yaml)
- [Azure Pipelines YAML schema](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema)