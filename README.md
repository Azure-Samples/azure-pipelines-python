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