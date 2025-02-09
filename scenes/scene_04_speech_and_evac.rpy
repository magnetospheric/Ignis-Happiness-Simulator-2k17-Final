#Scene 04
#Speech and Evac

#contains labels:
    # lunas_speech
    # ask_about_prince
    # ask_again_about_prince
    # keep_quiet_about_prince
    # change_subject_from_prince
    # niffs_arrive_on_the_scene
    # ask_about_prince


# covers luna's speech and evac of those in the plaza


label lunas_speech:

    $ renpy.music.set_volume(0.2, delay=1, channel='foley')
    $ renpy.music.set_volume(0.09, delay=1, channel='foley2')

    play foley2 plaza_crowd

    show bg yureilplaza crowd with Dissolve(1.5)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(1.0)

    narrator1 "You and Ignis both make your way to the back of the plaza."

    # sound effect crowd buzzing

    narrator1 "The crowd is abuzz with conversation."

    narrator1 "Everyone's making small talk — it's much too big an event to get into deep conversation — and they all seem tense, hiding anticipation behind their smiling faces."

    show ignis neutral at left
    with dissolve

    narrator1 "You glance at Ignis. He seems calm enough, although you recognise the offhand gaze with which he scans the audience."

    narrator1 "He's checking for discrepancies and dissent as much as you are. His keen eyes rove the crowd, before settling on the multi-spired, domed towers of the palace."

    ignis "It's a beautiful piece of architecture. Rather strategically-designed, too."

    you "How so?"

    ignis "The domed structures are a good shape to protect against assault or natural disaster."

    ignis "And the plaza itself is long and narrow - see where it bottlenecks quite naturally before these points they've got us guarding? It's exceedingly good for crowd control."

    you "Should make our job much easier, then."

    ignis "Indeed."

    narrator1 "You turn back to the crowd. They're still restless, still chatty."

    show noctis silhouette at right with Dissolve(1.0)

    narrator1 "Before long, you catch sight of a black-haired individual making his way through the crowd. He's moving irregularly, and as a guard, this is a cause for concern."

    narrator1 "But there's something about him that looks familiar..."

    narrator1 "And then you place it. It's a figure you've seen countless times on news reports before."

    narrator1 "The Crown Prince of Insomnia: Noctis Lucis Caelum."

    narrator1 "What's he doing here? It's odd to see him dressed so casually, and without bodyguards flanking him."

    narrator1 "Especially as, last you heard, the wedding between him and Lady Lunafreya had been called off."

    hide noctis silhouette with dissolve

    narrator1 "Ignis catches your gaze, and holds a finger to his lips softly. Oh. You should have guessed sooner."

    you "Is he with you?"

    ignis "Indeed he is."

    narrator1 "Ignis is watching the young Prince carefully, like a protective older brother would. You're itching to know more, because it feels like there's a part of this plan you're missing."

    menu:
        "Press Ignis about why the Prince is here":
            jump ask_about_prince
        "Nod in understanding and say no more":
            jump keep_quiet_about_prince
        "Steer the conversation tactfully away from the Prince":
            jump change_subject_from_prince



label ask_about_prince:

    you "I didn't expect to see the Lucian Prince here. I thought the... I thought the wedding was called off?"

    $ show_happiness = True

    $ happiness -= 1

    show screen happiness_text(title="Happiness decreased")
    with dissolve
    pause 0.5
    hide screen happiness_text
    with dissolve

    show ignis unimpressed openmouth with dissolve
    ignis "It has been, thanks to our friends from Niflheim."
    show ignis unimpressed

    narrator1 "His tone is as stiff as his posture has suddenly become, and you get the sense you have put him on a back foot here. The way he talks, there's no love lost for the Empire. But more than that — he seems uncomfortable discussing this in such a public space."

    menu:
        "Press Ignis once again about Prince Noctis":

            jump ask_again_about_prince

        "Backtrack":

            you "Sorry. I shouldn't really be asking at a time like this."

            show ignis neutral openmouth
            ignis "It's quite all right. Curiosity is natural, although I would prefer you kept your focus on the task at hand."
            show ignis neutral

            jump niffs_arrive_on_the_scene



label ask_again_about_prince:

    narrator1 "But you've started now, so you continue, albeit hesitantly."

    you "So, uh, why {i}is{/i} he here?"

    $ show_happiness = True

    $ happiness -= 1

    show screen happiness_text(title="Happiness decreased")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    show ignis unimpressed openmouth with dissolve
    ignis "Please, [your_name], some decorum. Lest our aforementioned 'friends' take a shining to our conversation."
    show ignis unimpressed

    jump niffs_arrive_on_the_scene



label keep_quiet_about_prince:

    narrator1 "You decide not to press him for details. It's not really the time nor the place, out in the open like this where anyone could be listening."

    narrator1 "Is it really necessary for you to know, anyway? You're just a guard, after all. You only get told things that are mission-critical."

    narrator1 "So you nod, and return to watching the crowd."

    show ignis smile

    narrator1 "Ignis seems to appreciate your discretion."

    pause 1.0

    $ show_happiness = True

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis ""

    jump niffs_arrive_on_the_scene



label change_subject_from_prince:

    narrator1 "While you desperately want to know, you are well aware that you only get told things that are mission-critical for a reason."

    narrator1 "And furthermore, you never know who might be listening in, in this busy place. So you change the subject, as casually as you can."

    you "You know, the palace is actually a lot newer than the rest of Altissia."

    show ignis neutral openmouth
    ignis "Oh?"
    show ignis neutral

    narrator1 "He seems to appreciate the distraction."

    show ignis smile
    with dissolve

    pause 1.0

    $ show_happiness = True

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    you "Yeah. I mean, the Altar of the Tidemother is still older than most things here, but there used to be a different shrine around it. It got destroyed a couple of hundred years ago, during a flood."

    show ignis neutral openmouth
    ignis "Did it now? Mm, I don't suppose it was built from the same material as the altar, then?"
    show ignis neutral

    narrator1 "You shake your head."

    you "Just regular limestone. Not a great idea."

    show ignis neutral openmouth
    ignis "Indeed."
    show ignis neutral

    you "But yeah — a lot of people don't know that, about the palace. People have terrible memories when it comes to floods, though. We forget our histories too quickly."

    show ignis neutral openmouth
    ignis "True enough."
    ignis "Well, I certainly didn't expect to get a personal tour guide on this assignment. But — you ought to know — you do a fine job."
    show ignis smile

    narrator1 "His smile is broad and genuine, and you realise he's not simply humouring you for the sake of distracting any would-be eavesdroppers."

    narrator1 "You're glowing with his compliment, too — people are usually telling you to shut up around now."

    jump niffs_arrive_on_the_scene



label niffs_arrive_on_the_scene:

    # these next few lines you only get if you haven't seriously pissed him off so far.
    if happiness > 4:

        narrator1 "Ignis turns back to survey the scene. Gods above, he cuts a sharp profile against the pastel morning light. You're staring but you don't care. Do all Lucians look this good?"

        narrator1 "One thing stands out above all others, and it's not his looks, nor his demeanour. It's simply this: you're enjoying his company."

        jump discuss_sightseeing

    elif happiness > 3:

        narrator1 "Ignis turns back to survey the scene. You watch him for a short moment — he cuts a striking figure — but you soon turn back, eyes on the audience."

        jump discuss_sightseeing

    elif happiness <= 3:

        narrator1 "You try to think of something to say to fill the gap, but nothing comes."



label discuss_sightseeing:

    narrator1 "Minutes pass, and still the speech has not begun."

    you "Is this your first time in Altissia?"

    show ignis neutral openmouth
    ignis "No ... I came here once as a child. It was a diplomatic visit, however, so there was little time for sightseeing."
    show ignis neutral

    you "Maybe after this, you'll get time to explore."

    show ignis neutral openmouth
    ignis "One can only hope."
    show ignis neutral

    $ ignis_wants_to_sightsee = True

    jump speech_begins



label speech_begins:

    stop ambient fadeout 2.286
    play music shrinemaiden1 fadein 2.286 loop

    show ignis neutral
    with dissolve

    $ renpy.music.set_volume(0.08, delay=0, channel='foley')
    $ renpy.music.set_volume(0.06, delay=1, channel='foley2')
    play foley cheering1 fadein 2.286 noloop

    pause 1.5

    narrator1 "Then, a cheer rises. Up at the steps of the palace, Lady Lunafreya has appeared."

    narrator1 "Even from the back of the plaza, you can see how she walks proudly and confidently. The same stiff-backed, determined attitude your own Captain displays all-too-often."

    narrator1 "Ignis activates his receiver."

    show ignis touching glasses with dissolve

    ignis "{i}Don't forget the plan.{/i}"

    narrator1 "Somewhere further in the crowd, a black head of hair shifts as the call is answered. It sounds like the Prince says something sarcastic then, because Ignis smiles wryly."

    show ignis smile

    ignis "Of course."

    narrator1 "Up at the gates of the palace, Lunafreya begins to speak."

    show ignis neutral
    with dissolve

    narrator1 "Her voice carries far, for someone so slight. She speaks of the coming darkness, of the scourge that plagues the world, and it sounds so foreboding, such mentions of horror and despair from someone so pure."

    narrator1 "But then, she turns to talk of hope. {i}The Gods have not abandoned us,{/i} she says. And she speaks with such gravitas, you want to believe it. You {i}do{/i} believe it."

    narrator1 "Lunafreya, too, makes no mention of Prince Noctis, although her eyes scan the crowd just before she leaves."

    narrator1 "You get the impression her plea to Leviathan will not be made alone, and you can only hope that the Empire does not catch wind of Noctis's presence."

    narrator1 "Then Lady Lunafreya is gone, vanished back into the palace to make her petitions at the Altar of the Tidemother."

    narrator1 "It's time for action."

    you "Okay, everyone!"

    you "Please make your way to the back of the plaza. The boats here will take you to Finangia District, out of the flooding zone."

    narrator1 "You wave the bemused citizens forward."

    you "Please, exit this way."

    narrator1 "You and Ignis both guide them towards the boats."

    narrator1 "You get a few questions — {i}why do we have to evacuate?{/i}, and {i}we want to support the Oracle{/i}, and {i}you can't tell us what to do in our own home!{i}"

    narrator1 "But for the most part, everyone is solemn enough to not cause any trouble."

    $ renpy.music.set_volume(0.1, delay=0, channel='foley')
    $ renpy.music.set_volume(0.2, delay=0, channel='foley3')
    play foley3 dropships_approaching noloop
    play foley [ "<silence 16.0>", engine_bassline] fadein 3.0
    queue foley engine_bassline loop

    narrator1 "A distant hum interrupts your work."

    narrator1 "A sort of ... revving ... and it's getting closer."

    narrator1 "You look up to see Imperial dreadnoughts approaching."

    narrator1 "Altissia has had so many years of peace under Niflheim's rule that you've almost forgotten the sight of these monstrosities."

    narrator1 "It's always been there, that low-rumbling threat in the back of your mind, and it's a shock now to see so many of the massive machines, fencing the city in like this."


    show ignis neutral openmouth
    ignis "Don't draw too much attention to them."
    show ignis neutral

    narrator1 "You nod. You don't want to panic the crowd. You continue herding them as before, hoping the Empire won't be foolish enough to start anything before the citizens reach safety."

    stop music fadeout 2.286
    play ambient shrinemaiden2 fadein 2.286 loop

    narrator1 "In the distance, a lone voice rises on the wind. A heavenly singing."

    narrator1 "Lady Lunafreya. So the rite has begun."

    narrator1 "You pause in your work, enraptured by the sound. Then, joining it, a tremendous splash of water and an unearthly, hallowed voice you cannot make sense of."

    narrator1 "A chill seeds itself through your bones."

    narrator1 "{i}Leviathan.{/i}"

    narrator1 "This is it; this is the moment of legend."

    narrator1 "And the Imperial ships grow ever closer."

    show ignis touching glasses with dissolve

    narrator1 "Ignis has taken to his receiver once again, and is speaking in hushed tones."

    ignis "{i}Noct, do you read me? ... Good. Listen — the Empire has arrived.{/i}"

    ignis "{i}Dropships are closing in on the port. You need to reach the altar before —{/i}"

    hide ignis

    show bg yureilplaza crowd dark with Dissolve(0.3)

    stop ambient

    $ renpy.music.set_volume(0.3, delay=0, channel='foley3')
    play foley3 airship_zoom noloop
    $ renpy.music.set_volume(0.8, delay=0, channel='foley3')
    queue foley3 explosion03 noloop
    $ renpy.music.set_volume(0.2, delay=1, channel='foley')
    $ renpy.music.set_volume(0.2, delay=1, channel='foley2')
    $ renpy.music.set_volume(0.3, delay=0, channel='foley3')
    $ renpy.music.set_volume(0.17, delay=0, channel='foley4')
    queue foley3 explosion04 noloop
    queue foley3 airship_zoom noloop
    queue foley3 explosion02 noloop
    queue foley3 [ "<silence 2.286>", explosion04 ] noloop

    play foley4 [ "<silence 6.286>", gunfire ] noloop
    queue foley4 explosion03 noloop
    queue foley4 airship_zoom noloop
    queue foley4 gunfire noloop
    queue foley4 explosion03 noloop

    narrator1 "With a burst of frenetic energy, the airships hovering above you open fire." with vpunch

    narrator1 "Their focus seems to be on the altar beyond the palace, but they don't seem particularly bothered about catching people in the crossfire, and stray bursts of explosions from small missiles and gunfire erupt in the plaza."

    narrator1 "The few people left in the plaza, and those still being transported away on the boats, begin to scream." with vpunch

    play music lights_out_1 fadein 2.286 loop
    show ignis sidelong openmouth at left with dissolve
    ignis "What the bloody hell does the Empire think they're doing?"

    show ignis sidelong with dissolve

    narrator1 "Now both your receivers crackle into life."

    captain "{i}Everyone in the South sector of the plaza, report back to the palace immediately once the citizens have boarded the boats! I repeat: Report back to the palace immediately once the citizens have boarded.{/i}"

    show ignis sidelong direct
    with dissolve

    narrator1 "The crackling cuts off, and you and Ignis share a worried glance before ushering the last few stragglers onto the boats."

    ignis "That should be the lot."

    narrator1 "You tell the last citizens that everything will be okay, then Ignis claps you briefly on the shoulder and together you race back to the palace."

    you "What's going on?"

    narrator1 "The two of you are running as fast as humanly possible, and Ignis's reply comes in sharp bursts."

    play foley4 explosion03 noloop

    show ignis sidelong direct openmouth
    with dissolve

    ignis "The Empire ... seeks to disrupt ... the ceremony."

    you "And you knew this was going to happen?"

    ignis "Yes."

    play foley4 explosion04 noloop

    narrator1 "You would have liked to have known this beforehand. But there's little point in making a fuss now. You need to focus."

    hide ignis

    jump power_cut
