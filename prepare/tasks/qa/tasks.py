from unitxt.blocks import FormTask
from unitxt.catalog import add_to_catalog

add_to_catalog(
    FormTask(
        inputs={"context": "str", "context_type": "str", "question": "str"},
        outputs={"answers": "List[str]"},
        prediction_type="str",
        metrics=["metrics.squad"],
    ),
    "tasks.qa.with_context.extractive",
    overwrite=True,
)

add_to_catalog(
    FormTask(
        inputs={"context": "str", "context_type": "str", "question": "str"},
        outputs={"answers": "List[str]"},
        prediction_type="str",
        metrics=["metrics.rouge"],
        augmentable_inputs=["context", "question"],
    ),
    "tasks.qa.with_context.abstractive",
    overwrite=True,
)

add_to_catalog(
    FormTask(
        inputs={"question": "str"},
        outputs={"answers": "List[str]"},
        prediction_type="str",
        metrics=["metrics.rouge"],
    ),
    "tasks.qa.open",
    overwrite=True,
)
