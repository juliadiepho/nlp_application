import csv
import pandas as pd

data_header = ["Date", "Content"]

data_content = ["JUNE 02, 2022", """Dear Diary, it’s currently quoter befor two but I’m still awake. 
My mom is working on document for changing my little sister’s disabilities pension. Her level has been changing heavier. 
And umm my mom needs to write detailed information on the document. That’s why she read my sisters school grade/life records after ten years from they were written. I read some of her teachers comments. Each of them were so cute. But my favorite was from her science class in her 4th grade. It was about her first veggie crop harvesting. Her plant was green pepper and the comment said she seemed so delighted of her first crop from her plant. so that she chose pink to express the happiness to draw it on her observation diary. And her teacher had to tell her to choose green or something. How beautiful this story is. I am so proud of her. 
But she isn’t like that anymore. The characteristic of down syndrome is appearing more and I can feel how hard is the mold of her way of thinking became. 
It’s hard to watch my closest person changing. I know it’s for everyone’s problem. Most of us must experience our parents getting weaker. But still I feel like it’s only for our family at this moment. Oh the reason is, I just found out by the way, that im in my 20s and my friends rarely think about it yet. So that’s why it’s only for me for now. 
No need to be afraid that much. I Stil got time to gradually accept this as she gradually changes. I want to be with / focus on her happy moment together even after realized it doesn’t last forever. Nothing lasts forever.and it’s scary. Especially it was about something we love and cherish. 
One funny? example is T lex. They probably were the strongest being on the earth!! But how now? They were gone and we go to see the bone! 
Cherry blossom last less than a month or less after the full bloom.  
Remember the Beatles’ song. “It is not dying” tomorrow never knows
Dream is not living it says. I take this line as “we dont need to worry too much about something not happened yet” 
play the game “existence” to the end 
Yes I would love to. But I can’t decide which token I would be yet. I’m still thinking. 
I am not really sure if I can fit in this society. My parents say it’s not scary as we hear but you know…
There are bunch of unkind people in the society. They are always seeking for their victims. I understand that I don’t need to care about their shit but I need to deal with my bad tendency of capture myself in their cage. 
I need to watch Adams family movie again."""]

with open("test.csv", "a") as file:
    writer = csv.writer(file)

    writer.writerow(data_header)
    writer.writerow(data_content)

