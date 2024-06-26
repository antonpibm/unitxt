from unitxt.catalog import add_to_catalog
from unitxt.templates import InputOutputTemplate

add_to_catalog(
    InputOutputTemplate(
        instruction="Please act as an impartial judge and evaluate the quality of the response"
        " provided by an AI assistant to the user question displayed below. Your evaluation should"
        " consider factors such as the helpfulness, relevance, accuracy, depth, creativity, "
        " and level of detail of the response. Begin your evaluation by providing a short"
        " explanation. Be as objective as possible. After providing your explanation, you must rate"
        ' the response on a scale of 1 to 10 by strictly following this format: "[[rating]]",'
        ' for example: "[[5]]".\n\n',
        input_format="[Question]\n{question}\n\n[The Start of Assistant's Answer]"
        "\n{model_output}\n[The End of Assistant's Answer]",
        output_format="{rating_label}",
        postprocessors=[
            r"processors.extract_mt_bench_judgment",
        ],
    ),
    "templates.rag.model_response_assessment.llm_as_judge_using_mt_bench_template",
    overwrite=True,
)
