from django.shortcuts import render
from polls.models import Question
import base64


# Create your views here.

def index(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        user_image = request.FILES['user_image']

        # Read the file content
        file_content = user_image.read()

        # Determine the image format
        image_format = user_image.content_type.split('/')[1]

        # Convert to base64
        base64_encoded_image = base64.b64encode(file_content).decode('utf-8')

        # Prepend the data URI prefix
        data_uri = f'data:image/{image_format};base64,{base64_encoded_image}'

        q = Question(question_text=question_text, user_image=data_uri)
        q.save()

    return render(request, 'polls/index.html')
