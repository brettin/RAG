import os
import sys
from txtai import Embeddings
from txtai.pipeline import Textractor
from txtai.pipeline import Segmentation

path = sys.argv[1]
textractor = Textractor(sections=True) #paragraphs=True)
def stream(path):
    for f in sorted(os.listdir(path)):
        fpath = os.path.join(path, f)

        # Only accept documents
        if f.endswith(("docx", "xlsx", "pdf", "md")):
            print(f"Indexing {fpath}")
            for paragraph in textractor(fpath):
                yield paragraph

# Create Embedding model from folder of pdfs/mds
# embeddings = Embeddings(content=True)
# embeddings.index(stream("/lambda_stor/data/ngetty/LUCID/md/"))

for f in sorted(os.listdir(path)):
    fpath = os.path.join(path, f)
    if f.endswith(("docx", "xlsx", "pdf", "md")):
        print(textractor(fpath))
