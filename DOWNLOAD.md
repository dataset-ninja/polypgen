Dataset **PolypGen** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/7/K/rT/GluU1xZ1LreIYYOfm2FFIBKha4tml7RCNoF4tMYzJdmrQ0ATPzPWYqe7PoJq0PxE5F41dd6SLtZZLz3k0dSzLlyYu7aAQeZfD44AA6BZlaxXbF3d0C4NJomZQ2Zs.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PolypGen', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

