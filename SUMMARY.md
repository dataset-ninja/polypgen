**PolypGen** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the medical industry. 

The dataset consists of 8037 images with 3734 labeled objects belonging to 1 single class different classes (*polyp*).

Images in the PolypGen dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 4916 (61% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Alternatively, the dataset could be split into 2 cases: ***negative*** (4275 images) and ***positive*** (3762 images). Also ***institute*** and ***sequence*** tags are included. The dataset was released in 2022 by the United Kingdom, Norway, Italy, Sweden, France, Egypt joint research team.

<img src="https://github.com/dataset-ninja/polypgen/raw/main/visualizations/poster.png">
