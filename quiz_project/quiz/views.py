from django.shortcuts import render

QUESTIONS = [
    {'question': 'What is the capital of France?', 'options': ['Berlin', 'Madrid', 'Paris', 'Rome'], 'answer': 'Paris'},
    {'question': 'Which planet is known as the Red Planet?', 'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'], 'answer': 'Mars'},
    {'question': 'What is the largest ocean on Earth?', 'options': ['Atlantic', 'Indian', 'Arctic', 'Pacific'], 'answer': 'Pacific'},
    {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Pb', 'Fe'], 'answer': 'Au'},
    {'question': 'Which element has the atomic number 1?', 'options': ['Oxygen', 'Hydrogen', 'Helium', 'Carbon'], 'answer': 'Hydrogen'},
    {'question': 'Who wrote "To Kill a Mockingbird"?', 'options': ['Harper Lee', 'Mark Twain', 'Ernest Hemingway', 'J.K. Rowling'], 'answer': 'Harper Lee'},
    {'question': 'What is the capital city of Australia?', 'options': ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'], 'answer': 'Canberra'},
    {'question': 'Which planet is closest to the sun?', 'options': ['Venus', 'Mars', 'Mercury', 'Earth'], 'answer': 'Mercury'},
    {'question': 'What year did the Titanic sink?', 'options': ['1905', '1912', '1918', '1923'], 'answer': '1912'},
    {'question': 'What is the hardest natural substance on Earth?', 'options': ['Gold', 'Iron', 'Diamond', 'Platinum'], 'answer': 'Diamond'},
    {'question': 'Who painted the Mona Lisa?', 'options': ['Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet'], 'answer': 'Leonardo da Vinci'},
    {'question': 'What is the capital of Japan?', 'options': ['Seoul', 'Beijing', 'Tokyo', 'Shanghai'], 'answer': 'Tokyo'},
    {'question': 'What is the longest river in the world?', 'options': ['Amazon', 'Nile', 'Yangtze', 'Mississippi'], 'answer': 'Nile'},
]


def index(request):
    return render(request, 'index.html')


def quiz(request):
    if request.method == 'POST':
        selected_answers = [request.POST.get(f'question_{i + 1}') for i in range(len(QUESTIONS))]
        correct_answers = [q['answer'] for q in QUESTIONS]
        score = sum(1 for i in range(len(selected_answers)) if selected_answers[i] == correct_answers[i])
        return render(request, 'result.html', {'score': score, 'total': len(QUESTIONS)})

    return render(request, 'quiz.html', {'questions': QUESTIONS})
