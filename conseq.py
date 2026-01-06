from manim import *

class Logic(Scene):
    def construct(self):
        lines = VGroup(
            MarkupText("When we say Formula 1 (F1) is a logical consequence of Formula 2 (2) we write:",  font_size=24),
            MarkupText("F2 ⊢ F1", font_size=24),
            MarkupText("Then we prove that:", font_size=24),
            MarkupText("F2 → F1 is a tautology (it means, it's always true)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.add(lines)
        