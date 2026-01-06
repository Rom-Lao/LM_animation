from manim import *

class Logic(Scene):
    def construct(self):
        self.counter = 0
        PATTERN_CLR = KEYWORD_CLR = YELLOW_D
        SOLUTION_CLR = TEAL_D  
        BG_CLR = WHITE
        TXT_CLR = BLACK
        
        """to create a group (keyword, pattern, example, solution)
        arrange them DOWN, color for keyword nd pattern are global, change 
        it in global variable
        """
        def create_group(k, p, e, s, solution_size = 36, vline_space=0.2):
            keyword = MarkupText(f'<u><span fgcolor="{WHITE}">Keyword:</span></u> {k}', color=KEYWORD_CLR)
            
            text_p = MarkupText(f'<u><span fgcolor="{WHITE}">Pattern:</span></u>')
            pattern = VGroup(text_p, MathTex(p, color=PATTERN_CLR)).arrange(RIGHT, buff=0.2)

            example = MarkupText(f'<u><span fgcolor="{WHITE}">Example:</span></u> {e}', font_size=36)
            
            text_s = MarkupText(f'<u><span fgcolor="{WHITE}">Solution:</span></u>')
            solution = VGroup(text_s, MathTex(s, color=SOLUTION_CLR, font_size=solution_size)).arrange(RIGHT, buff=0.2)
            
            group = VGroup(keyword, pattern, example, solution).arrange(DOWN, buff=vline_space)
            
            return group.shift(DOWN)
        
        # create rectangle box, to explain
        def add_rectangle(text, bg_clr=BG_CLR, text_clr=TXT_CLR, opacity=1, rectangle_radius=0.15, padding=0.4):
            self.counter = self.counter + 1
            t = MarkupText(text, color=text_clr)
            t.set_width(12)
            bgRectangle = BackgroundRectangle(
                t,
                fill_color=bg_clr,
                fill_opacity=opacity,
                corner_radius = rectangle_radius,
                buff = padding
            )
            
            bgCircle = Circle(
                radius=0.2,
                color=DARK_BLUE,
                fill_opacity=1
            )
            t_number = Text(str(self.counter), font_size=32).move_to(bgCircle.get_center())

            circle = VGroup(bgCircle, t_number)
            box = VGroup(bgRectangle, t).to_edge(UP)
            circle.next_to(box, LEFT)
            pair = VGroup(circle, box)
            return pair
        
        # add example 1 and its animation
        group_1 = create_group(
            "Every / all / each",
            r"\forall ... \to ",
            "Every student passed",
            r"\forall x (Student(x) \to Passed(x))",
        )
        group_1_box = add_rectangle("Many of you, will be tempted to use the connector 'and' instead of the 'implication', if you use 'and'; you are saying: everyone is a student and everyone passed the exam! but there is a condition here; you need to be a student first, that's why we use implication (it's just the students who passed, first you need to be a student, then it implies you passed the exam)")
        self.play(
            FadeIn(group_1_box),
            FadeIn(group_1)
        )
        self.wait(60)
        self.play(
            FadeOut(group_1_box), 
            FadeOut(group_1)  
        )
        # end of example 1
        
        # example 2
        group_2 = create_group(
            "Some / there exist / at least one",
            r"\exists ... \land ",
            "Some student passed",
            r"\exists x (Student(x) \land Passed(x))",
        )
        group_2_box = add_rectangle("there is at least one student who passed")
        self.play(
            FadeIn(group_2_box),
            FadeIn(group_2)
        )
        self.wait(60)
        self.play(
            FadeOut(group_2_box), 
            FadeOut(group_2)  
        )
        #end of example 2
        
        #example 3
        group_3 = create_group(
            "No, nobody, none",
            r"\forall ... \to...\lnot ",
            "No student cheated",
            r"\forall x (Student(x) \to \lnot Cheated(x))",
        )
        group_3_box = add_rectangle("for every student x, x did not cheat")
        self.play(
            FadeIn(group_3_box),
            FadeIn(group_3)  

        )
        self.wait(60)
        self.play(
            FadeOut(group_3_box), 
            FadeOut(group_3)  
        )
        #end of example 3
        
        # example 4 \: for space
        group_4 = create_group(
            "Nobody...everything",
            r"\forall, \exists , \lnot",
            "Nobody likes everything",
            r"\forall x\: \exists y\: \lnot Likes(x, y) ",
        )
        group_4_box = add_rectangle("Solution 1: for every person, there is at least one thing they don't like; Solution 2: negation(Solution 1)(inverse quantifiers)")
        self.play(
            FadeIn(group_4_box),
            FadeIn(group_4)
        )
        self.wait(60)
        self.play(
            FadeOut(group_4_box), 
            FadeOut(group_4)  
        )
        # end of example 4
        
        # example 5
        group_5 = create_group(
            "Not all",
            r"\exists...\lnot ",
            "Not all student passed",
            r"\exists x (Student(x) \land \lnot Passed(x))",
        )
        group_5_box = add_rectangle("we know that not everyone succeeded, so at least one student did not pass")
        self.play(
            FadeIn(group_5_box),
            FadeIn(group_5)
        )
        self.wait(60)
        self.play(
            FadeOut(group_5_box), 
            FadeOut(group_5)  
        )
        # end of example 5
        
        #example 6
        group_6 = create_group(
            "A only if B",
            r"\to",
            "You pass the exam only if you study",
            r"\forall x (Passed(x) \to Studied(x))",
        )
        group_6_box = add_rectangle("for every person x, if x passes the exam, then x must have studied")
        self.play(
            FadeIn(group_6_box),
            FadeIn(group_6)
        )
        self.wait(60)
        self.play(
            FadeOut(group_6_box), 
            FadeOut(group_6)  
        )
        #end of example 6
        
        #example of 7
        group_7 = create_group(
            "If A then B",
            r"\to ",
            "If you study, you pass",
            r"\forall x (Studied(x) \to Passed(x))",
        )
        group_7_box = add_rectangle("for every person, if this person studies, they passs; since it didn't mention a specific person, it is considered as a general rule (anyone who studied) so you should use universal quantifier")
        self.play(
            FadeIn(group_7_box),
            FadeIn(group_7)
        )
        self.wait(60)
        self.play(
            FadeOut(group_7_box), 
            FadeOut(group_7)  
        )
        #end of example 7
        
        #example 8 
        group_8 = create_group(
            "Every...some",
            r"\forall ... \to, \exists ",
            "Every student loves some food",
            r"\forall x (Student(x) \to \exists y (Food(y) \land Loves(x, y)) )",
        )
        group_8_box = add_rectangle("each student has at least one food they love. It doesn't have to be the same food for everyone")
        self.play(
            FadeIn(group_8_box),
            FadeIn(group_8)
        )
        self.wait(60)
        self.play(
            FadeOut(group_8_box), 
            FadeOut(group_8)  
        )
        #end of example 8
        
        # example of 9
        group_9 = create_group(
            "There is...every",
            r"\exists ... \land, \forall ... \to ",
            "There is an anime loved by every student",
            r"\exists y (Anime(y) \land \forall x\: Student(x) \to Loves(x, y))",
        )
        group_9_box = add_rectangle("there is one thing, everyone love it")
        self.play(
            FadeIn(group_9_box),
            FadeIn(group_9)
        )
        self.wait(60)
        self.play(
            FadeOut(group_9_box), 
            FadeOut(group_9)  
        )
        #end of example 9
        
        #example 10
        group_10 = create_group(
            "Everybody...something",
            r"\forall, \exists ",
            "Everybody knows something",
            r"\forall x\: \exists y\: Knows(x, y)",
        )
        group_10_box = add_rectangle("everyone knows at least one thing")
        self.play(
            FadeIn(group_10_box),
            FadeIn(group_10)
        )
        self.wait(60)
        self.play(
            FadeOut(group_10_box), 
            FadeOut(group_10)  
        )
        #end of example 10
        
        #example 11
        group_11 = create_group(
            "Without, does not, never",
            r"\lnot ",
            "Students without ID cannot enter",
            r"Students(x) \land \lnot hasID(x) \to \lnot Enter(x)",
        )
        group_11_box = add_rectangle("if there is a negation word next to your function, add it")
        self.play(
            FadeIn(group_11_box),
            FadeIn(group_11)
        )
        self.wait(60)
        self.play(
            FadeOut(group_11_box), 
            FadeOut(group_11)  
        )
        #end of example 11
        
        #example 12
        group_12 = create_group(
            "Exactly one",
            r"\exists x (P(x) \land \forall y(P(y) \to y= x))",
            "Exactly one student passed",
            r"\exists x (Passed(x) \land \forall y (Passed(y) \to y = x)",
        )
        group_12_box = add_rectangle("there is only one student who passed, y = x ensure that no other student passed")
        self.play(
            FadeIn(group_12_box),
            FadeIn(group_12)
        )
        self.wait(60)
        self.play(
            FadeOut(group_12_box), 
            FadeOut(group_12)  
        )
        #end of example 12
        
        #example 13
        group_13 = create_group(
            "At most one",
            r"\forall x \forall y ((P(x) \land P(y)) \to x = y) ",
            "At most one student failed",
            r"\forall x\:  \forall y\: ((Failed(X) \land Failed(y)) \to x = y)",
        )
        group_13_box = add_rectangle("zero student failed: OK, 1 student failed: OK, BUT not 2 student!")
        self.play(
            FadeIn(group_13_box),
            FadeIn(group_13)
        )
        self.wait(60)
        self.play(
            FadeOut(group_13_box), 
            FadeOut(group_13)  
        )
        #end of example 13
        
        #example 14
        group_14 = create_group(
            "At least two",
            r"\exists x \exists y (x != y \land P(x) \land P(y))",
            "At least two students passed",
            r"\exists x\: \exists y\: (Student(x) \land Student(y) \land Passed(x) \land Passed(y) \land x != y)",
        )
        group_14_box = add_rectangle("one is not enough, we need 2 students (not the same person) ")
        self.play(
            FadeIn(group_14_box),
            FadeIn(group_14)
        )
        self.wait(60)
        self.play(
            FadeOut(group_14_box), 
            FadeOut(group_14)  
        )
        #end of example 14
        
        end = Text("The End!")
        disclaimer_1 = MarkupText(f'<span fgcolor="{RED}">This video does not replace the lecture or tutorials</span>', font_size=28)
        disclaimer_2 = Text("Its purpose is simply to show students some tips to help them write first-order logic", font_size=26)
        disclaimer_3 = MarkupText(f'Questions? Use the <span fgcolor="{GREEN}">form</span>', font_size=28)
        
        disclaimer = VGroup(end, disclaimer_1, disclaimer_2, disclaimer_3).arrange(DOWN, buff=0.5)
        self.play(
            Write(disclaimer)
        )
        self.wait(60)