from fastapi import FastAPI, Form, UploadFile, File
import extract
import uuid
import os

app = FastAPI ()

@app.post("/get_pdf_file")
def get_pdf_file(
      file_format : str = Form(...),
      file : UploadFile = File(...),
):
    content = file.file.read()
    file_path = '../uploads/' + str(uuid.uuid4()) + '.pdf'

    with open(file_path, 'wb') as f:
        f.write(content)

    try:
        data = extract.extractor(file_path, file_format)
    except Exception as e:
         data = {
             'error' : str(e)
         }

    if os.path.exists(file_path):
        os.remove(file_path)

    return data
