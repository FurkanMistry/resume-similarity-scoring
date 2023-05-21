# resume-similarity-scoring
Resume Similarity Scoring API  
The Resume Similarity Scoring API is a Flask-based web service that enables users to compare a job description with an uploaded resume file and obtain a similarity score. It utilizes natural language processing techniques, such as text cleaning, tokenization, and cosine similarity, to determine the similarity between the job requirements and the candidate's resume.

Key Features:

User-friendly Interface: The API provides a straightforward interface for users to submit a job description, job experience, job skills, and a resume file for comparison.

Supports Multiple File Formats: It supports both Word document (docx) and PDF file formats, allowing users to upload resumes in the most common formats.

Text Preprocessing: The API applies various text preprocessing techniques, such as removing URLs, mentions, punctuations, and non-ASCII characters, as well as converting text to lowercase and removing stopwords, to ensure accurate comparison results.

Cosine Similarity Scoring: By utilizing the CountVectorizer and cosine_similarity functions from scikit-learn, the API calculates the similarity score between the job description and the resume, providing a quantitative measure of how well the candidate's skills align with the job requirements.

CORS Headers Implementation: To enable cross-origin resource sharing, the API incorporates CORS headers, allowing requests from different domains.

Live Deployment on PythonAnywhere: The API is currently deployed on PythonAnywhere, providing a live environment accessible to users for seamless integration and utilization.

Usage:

Submit a POST request to the /upload_file endpoint, including the job description, job experience, job skills, and a resume file as parameters.

The API processes the resume file, performs text cleaning and preprocessing, and calculates the similarity score using cosine similarity.

The similarity score is returned as a JSON response, indicating the percentage of similarity between the job description and the candidate's resume.

Deployment:

The Resume Similarity Scoring API is live and can be accessed at https://your-username.pythonanywhere.com/. Users can leverage the API to evaluate the suitability of resumes for specific job descriptions quickly and accurately.

For detailed instructions on how to use the API, refer to the documentation provided in the repository.

Contributing:

Contributions to the Resume Similarity Scoring API are welcome. Whether it's bug fixes, feature enhancements, or other improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

License:

This project is licensed under the MIT License. Please refer to the LICENSE file for more information.

Enjoy using the Resume Similarity Scoring API to streamline and optimize your resume evaluation process!
