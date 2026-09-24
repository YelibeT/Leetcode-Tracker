
from bot.services.roadmap import get_next_problem


problem = get_next_problem("neetcode75", 1)

if problem:
    print(problem.title)
    print(problem.difficulty)
    print(problem.category)
    print(problem.position)
else:
    print("No problem found")
