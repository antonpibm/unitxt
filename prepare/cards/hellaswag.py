from unitxt.blocks import LoadHF, TaskCard
from unitxt.catalog import add_to_catalog
from unitxt.operators import AddFields, CastFields, RenameFields
from unitxt.test_utils.card import test_card

card = TaskCard(
    loader=LoadHF(path="hellaswag"),
    preprocess_steps=[
        "splitters.large_no_test",
        RenameFields(
            field_to_field={
                "ctx": "context",
                "activity_label": "topic",
                "endings": "choices",
            }
        ),
        RenameFields(field_to_field={"label": "answer"}),
        CastFields(fields={"answer": "int"}),
        AddFields(fields={"context_type": "sentence"}),
    ],
    task="tasks.completion.multiple_choice",
    templates="templates.completion.multiple_choice.all",
)
# We disable strict checking because garbage predictions (when using the post processor
# that takes the first letter) is sometimes right and yields a non zero score.
test_card(card, debug=False, strict=False)
add_to_catalog(card, "cards.hellaswag", overwrite=True)
