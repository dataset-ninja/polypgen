from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "PolypGen2021"
PROJECT_NAME_FULL: str = (
    "PolypGen: A Polyp Segmentation and Detection Generalisation Dataset from EndoCV2021 Challenge"
)
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical(sensitive_content=True)

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [CVTask.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2022-11-16"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://www.synapse.org/#!Synapse:syn26376615/wiki/613312"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 4317957
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/polypgen"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = [
    "https://www.synapse.org/#!Synapse:syn26376615/files/"
]
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/abs/2106.04463"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "Alternative Kaggle Source": "https://www.kaggle.com/datasets/kokoroou/polypgen2021"
}

CITATION_URL: Optional[str] = "https://arxiv.org/abs/2106.04463"
AUTHORS: Optional[List[str]] = [
    "Sharib Ali",
    "Debesh Jha",
    "Noha Ghatwary",
    "Stefano Realdon",
    "Renato Cannizzaro",
    "Osama E. Salem",
    "Dominique Lamarque",
    "Christian Daul",
    "Michael A. Riegler",
    " Kim V. Anonsen",
    "Andreas Petlund",
    "Pål Halvorsen",
    "Jens Rittscher",
    "Thomas de Lange",
    "James E. East",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "University of Leeds",
    " University of Oxford",
    "Oxford National Institute for Health Research Biomedical Research centre",
    "SimulaMet",
    " UiT The Arctic University of Norway",
    "Arab Academy for Science and Technology",
    "Veneto Institute of Oncology IOV-IRCCS",
    ", Sahlgrenska University Hospital-Molnda",
    "CRO Centro Riferimento Oncologico IRCCS Aviano Italy",
    "1Universite de Versailles St-Quentin en Yvelines",
    "University of Alexandria",
    "Universite de Lorraine and CNRS",
    "University of Gothenburg",
    "Augere Medical",
    "Oslo Metropolitan University",
    "Oslo University Hospital Ulleval",
    "Northwestern University",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.leeds.ac.uk/",
    "https://www.ox.ac.uk/",
    "https://oxfordbrc.nihr.ac.uk/",
    "https://www.simulamet.no/",
    "https://en.uit.no/startsida",
    "https://aast.edu/en/",
    "https://www.ioveneto.it/en/about-the-iov/",
    "https://www.sahlgrenska.se/en/",
    "https://www.cro.sanita.fvg.it/it/",
    "https://www.uvsq.fr/",
    "https://alexu.edu.eg/index.php/en/",
    "https://www.univ-lorraine.fr/en/univ-lorraine/",
    "https://www.gu.se/en",
    "https://augere.md/",
    "https://www.oslomet.no/en/",
    "https://oslo-universitetssykehus.no/oslo-university-hospital",
    "https://www.northwestern.edu/",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "cases": ["positive", "negative"],
    "__POSTTEXT__": "Also ***institute*** and ***sequence*** tags are included.",
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
