import sys
sys.path.append(r"C:\Users\John\Personal Files\Entrepreneurship\News Cruncher\03 NLP")
from django.shortcuts import render
from .forms import BlogModelForm
from .models import BlogModel
from django.http import JsonResponse
# Create your views here.

grabber = {}

def homepage(request):
	if request.POST:
		form = BlogModelForm(request.POST)
		form.save()
		context = {'msg':"succesfully Submitted",'form.as_p':form}
		return render(request,'junk.html',context)
	else:
		form = BlogModelForm()
		context = {'form':form}
		return render(request,'homepage.html',context)

def ajaxsave(request):
	BlogModel.objects.create(title=request.POST['title'],content = request.POST['textareacontent'],method = request.POST['method'])
	grabber['content'] = str(request.POST['textareacontent'])
	return JsonResponse({'foop':'foopy'})

import Capitalize
def quantumize(request):
	result = Capitalize.correlate(Capitalize.model_loader(), Capitalize.corpus_loader(), grabber['content'])
	context = {
	'url_one':result['1']['url'], 
	'headline_one': result['1']['headline'],
	'news_source_one': result['1']['news_source'],
	'pub_time_one': result['1']['url_scrape_time'][:len(result['1']['url_scrape_time'])-10],
	'url_two':result['2']['url'], 
	'headline_two': result['2']['headline'],
	'news_source_two': result['2']['news_source'],
	'pub_time_two': result['2']['url_scrape_time'][:len(result['2']['url_scrape_time'])-10],
	'url_three':result['3']['url'], 
	'headline_three': result['3']['headline'],
	'news_source_three': result['3']['news_source'],
	'pub_time_three': result['3']['url_scrape_time'][:len(result['3']['url_scrape_time'])-10],
	'url_four':result['4']['url'], 
	'headline_four': result['4']['headline'],
	'news_source_four': result['4']['news_source'],
	'pub_time_four': result['4']['url_scrape_time'][:len(result['4']['url_scrape_time'])-10],
	'url_five':result['5']['url'], 
	'headline_five': result['5']['headline'],
	'news_source_five': result['5']['news_source'],
	'pub_time_five': result['5']['url_scrape_time'][:len(result['5']['url_scrape_time'])-10],
	'url_six':result['6']['url'], 
	'headline_six': result['6']['headline'],
	'news_source_six': result['6']['news_source'],
	'pub_time_six': result['6']['url_scrape_time'][:len(result['6']['url_scrape_time'])-10],
	'url_seven':result['7']['url'], 
	'headline_seven': result['7']['headline'],
	'news_source_seven': result['7']['news_source'],
	'pub_time_seven': result['7']['url_scrape_time'][:len(result['7']['url_scrape_time'])-10],
	'url_eight':result['8']['url'], 
	'headline_eight': result['8']['headline'],
	'news_source_eight': result['8']['news_source'],
	'pub_time_eight': result['8']['url_scrape_time'][:len(result['8']['url_scrape_time'])-10],
	'url_nine':result['9']['url'], 
	'headline_nine': result['9']['headline'],
	'news_source_nine': result['9']['news_source'],
	'pub_time_nine': result['9']['url_scrape_time'][:len(result['9']['url_scrape_time'])-10],
	'url_ten':result['10']['url'], 
	'headline_ten': result['10']['headline'],
	'news_source_ten': result['10']['news_source'],
	'pub_time_ten': result['10']['url_scrape_time'][:len(result['10']['url_scrape_time'])-10],
}
	return render(request,'meal.html',context)