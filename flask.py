import os
from flask import Flask, jsonify, render_template, request, after_this_request
import docx2txt
#from docx2txt import process
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import json
import PyPDF2
#from flask_cors import CORS
#import opencv as cv2
import re
from nltk.tokenize import word_tokenize
import nltk


app = Flask(__name__)
#CORS(app)
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return "hello"


@app.route('/upload_file', methods=['POST'])
def upload_file():
    def __clean_text(resume_text):
        resume_text = re.sub('http\S+\s*', ' ', resume_text)  # remove URLs
        resume_text = re.sub('RT|cc', ' ', resume_text)  # remove RT and cc
        resume_text = re.sub('#\S+', '', resume_text)  # remove hashtags
        resume_text = re.sub('@\S+', '  ', resume_text)  # remove mentions
        resume_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resume_text)  # remove punctuations
        resume_text = re.sub(r'[^\x00-\x7f]',r' ', resume_text)
        resume_text = re.sub('\s+', ' ', resume_text)  # remove extra whitespace
        resume_text = resume_text.lower()  # convert to lowercase
        resume_text_tokens = word_tokenize(resume_text)  # tokenize
        filtered_text = [w for w in resume_text_tokens]  # remove stopwords
        return ' '.join(filtered_text)

    a = request.form.get('jobdesc')
    b = request.form.get('jobexp')
    c = request.form.get('jobskills')
    #job_desc = "NLP machine learning with experience, python programming, mysql, sql, database, artificial intelligence"
    job_desc = a + " " + b + " " + c
    file = request.files['file']

    if file.content_type in ['application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        #For docx format
        resume1 = docx2txt.process(file)

    elif file.content_type == 'application/pdf':
        #For PDF format
        pdf = PyPDF2.PdfFileReader(file)
        resume1 = ""
        for page in range(pdf.getNumPages()):
            resume1 += pdf.getPage(page).extractText()

    resume = __clean_text(resume1)

    content = [job_desc, resume]
    cv = CountVectorizer()
    max = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(max)
    Accuracy = str(similarity_matrix[0][1]*100)
    return jsonify({"Score": Accuracy})

if __name__ == '__main__':
    app.run() 