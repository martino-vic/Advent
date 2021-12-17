Gave up after 2.5hrs without a silver star, I think I'm not even close. My first anwer was accidentally someone else's (1490), so at least my solution must be in a reasonable range. The problem is hard to conceptualise. At first I made a formula how FAR the probe will go. While the actual question is: Will one of the steps the probe makes be within the target area? The second misconception I had was not connecting x and y. They have to be in the target area at the same time. Next time I need a bulletproof concept and scheme before I start cowboy coding. If the logic and concept is flawed you can't write the code.  
Update: found a solution on reddit that is only 3 lines?! Wow, also just learned about the double slash operator for divisions :O how cool!

```
x1,x2,y1,y2=map(int,re.findall('-?\d+', "target area: x=206..250, y=-105..-57"))
ymax=-y1-1
(ymax*(ymax+1))//2
```
Also a good experience to see where my own programming boundaries are: maths, mathematical thinking, formalising problems