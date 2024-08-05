from django.shortcuts import render
import random

# List of jokes
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? It had too many problems.",
    "Why don't programmers like nature? It has too many bugs.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "A Pen is worth a thousand docs.",
    "Be the developer your linter thinks you are.",
    "How do you comfort a JavaScript bug? You console it.",
    "How would you React if I said I love Vue.",
    "If a groundhog inspects their Web Component, do they see their Shadow DOM.",
    "If you get tired, be like an AJAX request and REST.",
    "If you want to flex your skills and go off the grid, try coding a layout with float.",
    "Keep friends close and formatters closer.",
    "Keep the <main> thing the <main> thing.",
    "Knock knock! Race condition. Who's there.",
    "Learning 3D transforms in CSS requires a little perspective.",
    "Old programmers never die; they just lose some of their functions.",
    "Promise you'll await for me.",
    "Save your sass for CSS. Everywhere else, be kind.",
    "The best caches are like the best hugs. Warm.",
    "The Pen is mightier than the sword.",
    "There are 10 kinds of people, those who understand binary and those who don't.",
    "There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.",
    "Two CSS properties walk into a bar. A barstool in a completely different bar falls over.",
    "We would have called your functions earlier, but we were in a bind.",
    "We'd ask you for an infinite loop joke, but we'd never hear the end of it.",
    "We're stronger <u>nited than <div>ided.",
    "What did the colon say to the semicolon? Stop winking at me.",
    "What did the HTML say to the CSS? I like your style.",
    "What do you call a two-legged ghost cow? Boolean Beef.",
    "What's a functional programmer's favorite animal? A lamb, duh.",
    "Who's loopier? A fruit loop or a for loop.",
    "Why did the programmer quit her job? She didn't get arrays.",
    "💕 I'm the CSS to your HTML."
]

def joke_generator(request):
    joke = random.choice(JOKES)
    return render(request, 'joke.html', {'joke': joke})
