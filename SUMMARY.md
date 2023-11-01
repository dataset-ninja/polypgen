**PolypGen: A Polyp Segmentation and Detection Generalisation Dataset from EndoCV2021 Challenge** is a dataset for instance segmentation, semantic segmentation, object detection, and classification tasks. It is used in the medical industry. 

The dataset consists of 8037 images with 3734 labeled objects belonging to 1 single class (*polyp*).

Images in the PolypGen dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 4916 (61% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Alternatively, the dataset could be split into 2 cases: ***negative*** (4275 images) and ***positive*** (3762 images). Also ***institute*** and ***sequence*** tags are included. The dataset was released in 2022 by the UK-NOR-EGY-IT-SWE-FR-US joint research group.

<img src="https://github.com/dataset-ninja/polypgen/raw/main/visualizations/poster.png">
