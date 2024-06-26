from unitxt.blocks import LoadHF
from unitxt.card import TaskCard
from unitxt.catalog import add_to_catalog
from unitxt.operators import (
    AddFields,
    ListFieldValues,
    MapInstanceValues,
    RenameFields,
)
from unitxt.test_utils.card import test_card

card = TaskCard(
    loader=LoadHF(path="super_glue", name="copa"),
    preprocess_steps=[
        "splitters.small_no_test",
        ListFieldValues(fields=["choice1", "choice2"], to_field="choices"),
        RenameFields(field_to_field={"premise": "context", "label": "answer"}),
        MapInstanceValues(
            mappers={
                "question": {  # https://people.ict.usc.edu/~gordon/copa.html
                    "cause": "What was the cause of this?",
                    "effect": "What happened as a result?",
                }
            }
        ),
        AddFields({"context_type": "sentence"}),
    ],
    task="tasks.qa.multiple_choice.with_context",
    templates="templates.qa.multiple_choice.with_context.all",
)

test_card(card, strict=False)
add_to_catalog(card, "cards.copa", overwrite=True)
