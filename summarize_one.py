import sys
fpath = sys.argv[1]

# Extract document
from txtai.pipeline import Textractor
txt = Textractor(fpath)

# Summarize document
from CustomLLM import ARGO_LLM
from ARGO import ArgoWrapper

llm = ARGO_LLM(argo=ArgoWrapper())


print(llm("hello world"))

prompt="""You are an advanced AGI for science. Please read the following
paper and answer the following questions.

1. What is the paper about?
2. What is the central question or questions that the paper aims to answer?
3. What are the key findings that relate to the central question or questions?
4. If there are unanswered questions in the paper, what are those?

Please provide the output with the following headings:

SUMMARY
CENTRAL QUESTION(S)
FINDINGS
OPEN QUESTIONSi

If you are unsure of the answer to any of the questions, please say you are unsure.

Here is the paper """ + paper


