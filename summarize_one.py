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

