import os
import json
import openai
from langchain import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI  # , ChatOpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from services.constants import Constants
from services.replace_language_in_prompt import replace_language_in_prompt


def text_to_meeting_report(transcript: str, language: str) -> dict:
    openai.api_key = str(os.getenv("GPT_TURBO_API_KEY"))
    openai.api_base = "https://labopenaiapi.openai.azure.com/"
    openai.api_type = "azure"
    openai.api_version = "2023-03-15-preview"

    # Split text in chunks
    text_splitter = CharacterTextSplitter(separator=".", chunk_size=2900)
    texts = text_splitter.split_text(transcript)
    docs = [Document(page_content=t) for t in texts[:30]]

    # Prepare prompt for Meeting report generation
    prompt_template = replace_language_in_prompt(
        Constants.MEETING_REPORT_PROMPT, language
    )
    question_prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    print("question_prompt  : ", question_prompt)

    # Prepare refine prompt to handle large transcript
    refine_template = Constants.MEETING_REPORT_REFINE_PROMPT
    refine_prompt = PromptTemplate(
        input_variables=["existing_answer", "text"],
        template=refine_template,
    )

    # Define model and refine chain type methods
    chain = load_summarize_chain(
        AzureChatOpenAI(
            deployment_name="gpt_3_5_turbo_api",
            max_tokens=1000,
            temperature=0,
            openai_api_version=openai.api_version,
            openai_api_type=openai.api_type,
            openai_api_base=openai.api_base,
            openai_api_key=openai.api_key,
        ),  # type:ignore
        chain_type="refine",
        return_intermediate_steps=True,
        question_prompt=question_prompt,
        refine_prompt=refine_prompt,
        verbose=True,
    )

    steps = chain({"input_documents": docs}, return_only_outputs=True)
    meeting_report = steps["output_text"]

    meeting_report_json = json.loads(meeting_report)
    return meeting_report_json
