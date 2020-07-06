from django.http import HttpResponse
from django.shortcuts import render
import operator 

def home (request): 
    return render(request, 'home.html', {'HiThere':'This is writing in Python'});

def eggs(request):
    return HttpResponse('<h1>Liam loves eggs<h1>');

def count(request):
    fullText = request.GET['fulltext']
    print(fullText);
    
    wordList = fullText.split();
    
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            # increase
            wordDict[word] += 1;
        else:
            # Add to dict
            wordDict[word] = 1;
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fullText, 'totalCount':len(wordList), 'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html', {'AboutPage':'About Page'});



