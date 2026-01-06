from manim import *

class Deduction(Scene):
    def construct(self):
        KEYWORD_CLR = YELLOW_D  
        BG_CLR = WHITE
        TXT_CLR = BLACK
        
        """to create a group (keyword, pattern, example, solution)
        arrange them DOWN, color for keyword nd pattern are global, change 
        it in global variable
        """
        def create_group(k):
            keyword = MarkupText(k, color=KEYWORD_CLR)
            return keyword.shift(DOWN)
        
        # create rectangle box, to explain
        def add_rectangle(text, bg_clr=BG_CLR, text_clr=TXT_CLR, opacity=1, rectangle_radius=0.15, padding=0.4):
            t = MarkupText(text, color=text_clr)
            t.set_width(12)
            bgRectangle = BackgroundRectangle(
                t,
                fill_color=bg_clr,
                fill_opacity=opacity,
                corner_radius = rectangle_radius,
                buff = padding
            )
            
            box = VGroup(bgRectangle, t).to_edge(UP)
            return box
        
        # add example 1 and its animation
        group_1 = create_group(
            "(A ∧ B) ∧ C,   C ∧ D ⊢ ... ",
        )
        group_1_box = add_rectangle("C∧D;    (A∧B)∧C are premises (they appear before ⊢), so they may be used directly in the proof (put each term after ⊢)")
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
            "     ⊢ A → (B → A ∧ B)"
        )
        group_2_box = add_rectangle("Here you are asked to prove A → (B → A ∧ B), but there are no premises! In this case, for each →; you assume its first part (axiom = something true without proof), meaning you put A, B on the premises side")
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
            "A ⊢ B → A ∧ B",
        )
        group_3_box = add_rectangle("Before the final step of proving A → (B → A ∧ B), you are obviously going to use the →i to add →; Remember: you MUST remove the first term of the → from the premises (here remove A when you apply →i)")
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
            "2- A → B , A → ¬B , A ⊢ A → B (axiom)\n3- A → B , A → ¬B , A ⊢ A (axiom)\n4- A → B , A → ¬B , A ⊢ B  MP(2,3)"
        )
        group_4_box = add_rectangle("MP rule is simple, if you proved A → B and  A (which means they are true); you can deduce using MP rule that B is also true")
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
            "....\n6- A → B , A → ¬B , A ⊢ B ∧ ¬B    ∧i sur (4,5)\n7- A → B , A → ¬B ⊢ ¬A     ¬i sur 6"
        )
        group_5_box = add_rectangle("To prove ¬A is true, you need to find A → ⊥ in your deduction, which means A implies something absurd like B ∧ ¬B; after finding this pattern, you use ¬i rule; Remember: delete A from the premises side; Important: you apply the same idea if you want to prove that A is true")
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
            "Σ ⊢ A   (hypothesis)",
        )
        group_6_box = add_rectangle("We don't know what formulas were used in Σ, so you just put A as hypothesis (meaning it was already proven previously using that Σ)")
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
            "1. Σ ⊢ A  (hypothesis)\n2. Σ, A → B ⊢ A  (AP sur 1)"
        )
        group_7_box = add_rectangle("You can use AP rule here since you need A → B on the premise side to prove ¬(A → B); Remember A is still true before and after you apply AP rule, that's why you can add premises using AP rule!")
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
            "1. ¬D ⊢ (D ∨ ¬A) → (A ∨ D)\n2. A → C ⊢ (B → C) → (A ∨ B → C)\n3.    ⊢ C → (B → C ∧ B)"
        )
        group_8_box = add_rectangle("Your turn! Prove the following sequents")
        
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
        
        end = Text("The End!")
        disclaimer_1 = MarkupText(f'<span fgcolor="{RED}">This video does not replace the lecture or tutorials</span>', font_size=28)
        disclaimer_2 = Text("Its purpose is simply to show students some tips to help them write first-order logic", font_size=26)
        disclaimer_3 = MarkupText(f'Questions? Use the <span fgcolor="{GREEN}">form</span>', font_size=28)
        
        disclaimer = VGroup(end, disclaimer_1, disclaimer_2, disclaimer_3).arrange(DOWN, buff=0.5)
        self.play(
            Write(disclaimer)
        )
        self.wait(60)