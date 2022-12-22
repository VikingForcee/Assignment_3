print("Q4")
print()

grade_point=int(input("Enter grade points:"))
dic = {10 : "Your grade is 'A+' and Outstanding performance.",
     9: "Your grade is 'A' and Excellent performance.",
     8: "Your grade is 'B+' and Very Good performance.",
     7: "Your grade is 'B' and Good performance.",
     6: "Your grade is 'C+' and Average performance.",
     5: "Your grade is 'C' and Below Average performance.",
     4: "Your grade is 'D' and Poor performance."}

if 4 <= grade_point <= 10:
        string = dic.get(grade_point)
        print(string)
else:
    print("\nError\nPlease enter grade in range [4,10]")