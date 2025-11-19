#for https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    #need abv bc scores within loop?
    avg = (sum(scores) )/ (len(scores))
    #print(float(sum(scores) / (len(scores))))
    print(f"{(avg):.2f}")
   
    
#scores = student_marks[query_name] avg = sum(scores) / len(scores) print(f"{avg:.2f}")
 #above doesn't pass with .5
