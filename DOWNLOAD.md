Dataset **PolypGen** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMjE0NV9Qb2x5cEdlbi9wb2x5cGdlbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJSWG5ocGtQVFk3dnlzM0lFSDF0c1ZKSGo4TVoxVlpycXo0dGY5RWRLTG53PSJ9?response-content-disposition=attachment%3B%20filename%3D%22polypgen-DatasetNinja.tar%22)

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

