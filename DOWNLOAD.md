Dataset **PolypGen** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/X/jI/ZcjATJzh4l65FhHoM1SjbqQVPGRvLRLwaI36ECcWXrQDb0vxs25NbpPcG7ivNC0MGKj3z3eEFYdQlfOCc1eVqXYmsydrdGVETLguvzh6C7FbqySovHuPLa5zFo4T.tar)

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

