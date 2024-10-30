from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django_ratelimit.decorators import ratelimit
from django.contrib.auth import login , logout
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .models import GeneratedContent, UserApiUsage, Feedback
from .forms import SignUpForm
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

# Index view
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            name=request.POST.get('name')
            feedback=request.POST.get('suggestion')
            rating=request.POST.get('rating')
            Feedback.objects.create(name=name,feedback=feedback,rating=rating)
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('index')

    return render(request, 'paragraph_generator/index.html')

# Signup view
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


# Check and reset daily limit
def check_reset_daily_limit(user):
    """Reset daily usage if it's a new day"""
    usage, created = UserApiUsage.objects.get_or_create(user=user)
    today = timezone.now().date()
    
    # Check if it's a new day and reset usage if so
    if usage.last_reset != today:
        usage.daily_usage = 0
        usage.last_reset = today
        usage.save()
    
    return usage


# Generate paragraph view
@login_required
@ratelimit(key='user_or_ip', rate='50/d', method='POST', block=True)
def generate_paragraph(request):
    if request.method == 'GET':
        # Render the generate.html page with initial context
        return render(request, 'paragraph_generator/generate.html', {'remaining_requests': 50})

    try:
        # Check daily limit
        usage = check_reset_daily_limit(request.user)
        if usage.daily_usage >= 50:  # 50 requests per day limit
            return JsonResponse({
                'status': 'error',
                'message': 'Daily limit exceeded. Please try again tomorrow.'
            }, status=429)

        # Set the OpenAI API key
        openai.api_key = os.environ.get("OPENAI_API_KEY")

        # Get and validate parameters from request
        topic = request.POST.get('topic', '').strip()
        grade_level = request.POST.get('grade_level', 'high school').strip()
        tone = request.POST.get('tone', 'neutral').strip()
        style = request.POST.get('style', 'informative').strip()
        
        try:
            word_limit = int(request.POST.get('word_limit', 200))+30
            if word_limit <= 0 or word_limit > 500:
                raise ValueError("Word limit must be a positive integer and not exceed 500.")
        except (TypeError, ValueError) as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Invalid word limit: {str(e)}'
            }, status=400)

        # Construct the prompt
        prompt = f"""Generate an educational paragraph about {topic}.
        Requirements:
        - Appropriate for {grade_level} level students
        - Use a {tone} tone
        - Write in a {style} style
        - Keep it approximately {word_limit} words
        - Make it engaging and informative"""
        
        # Make the API call
        client = openai.OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"),
  base_url="https://api.together.xyz/v1",
)
        # response = client.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "user", "content": prompt}
        #     ]
        # )

        response = client.chat.completions.create(
  model="meta-llama/Llama-Vision-Free",
  messages=[
    # {"role": "system", "content": "You are a Teacher."},
    {"role": "user", "content": prompt},
    # {"role": "user", "content": "Generate a paragraph on the topic of 'The importance of education in life'"},
  ]
)

        # Parse API response
        content = response.choices[0].message.content
        if not content:
            return JsonResponse({
                'status': 'error',
                'message': 'No content generated by the API.'
            }, status=500)
        
        word_count = len(content.split())

        # Save to database (assuming you have a model to store this data)
        GeneratedContent.objects.create(
            user=request.user,
            prompt=prompt,
            content=content,
            word_count=word_count,
            topic=topic,
            grade_level=grade_level,
            tone=tone,
            style=style
        )
        
        # Update usage
        usage.daily_usage += 1
        usage.save()
        
        return JsonResponse({
            'status': 'success',
            'content': content,
            'word_count': word_count,
            'remaining_requests': 50 - usage.daily_usage
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Unexpected error: {str(e)}'
        }, status=500)


# Dashboard view
@login_required
def dashboard(request):
    user_content = GeneratedContent.objects.filter(user=request.user)
    usage = UserApiUsage.objects.get_or_create(user=request.user)[0]
    
    context = {
        'user_content': user_content,
        'remaining_requests': 50 - usage.daily_usage,
        'total_generations': user_content.count()
    }
    return render(request, 'paragraph_generator/dashboard.html', context)


# Logout view
@login_required
def user_logout(request):
    # Logging out the user
    logout(request)
    return redirect('index')