from music import *
# theme has some repetition, so break it up to maximize economy
# (also notice how we line up corresponding pitches and durations)
EliseScore = Score("For Elise",120)

主旋律
pitches1   = [E5, DS5, E5, DS5, E5, B4, D5, C5]
durations1 = [EN, EN,  EN, EN,  EN, EN, EN, EN]
pitches2   = [A4, REST, C4, E4, A4, B4, REST, E4]
durations2 = [QN, EN,   EN, EN, EN, QN, EN,   EN]
pitches3   = [GS4, B4, C5, REST, E4]
durations3 = [EN,  EN, QN, EN, EN]
pitches4   = [C5, B4, A4]
durations4 = [EN, EN, QN]
pitches5   = [REST, B4, C5, D5, E5]
durations5 = [EN,   EN, EN, EN, DQN]
pitches6   = [G4, F5, E5, D5]
durations6 = [EN, EN, EN, DQN]
pitches7   = [F4, E5, D5, C5]
durations7 = [EN, EN, EN, DQN]
pitches8   = [E4, D5, C5, B4,REST]
durations8 = [EN, EN, EN, DQN,EN]
pitches9   = [E4,E5,E4,E5,E5,E6,DS5,E5,DS5,E5,DS5,E5,DS5]
durations9 = [EN,EN,EN,EN,EN,EN,EN,EN,EN,EN,EN,EN,EN]
合唱
pitches01 = [A2,E3,A3,Rest,Rest]
durations01 = [EN,EN,EN,EN,QN]
pitches02 = [E2,E3,GS3,Rest,Rest]
durations02 = [EN,EN,EN,EN,QN]
pitches03 = [C3,G3,C4,Rest,Rest]
durations03 = [EN,EN,EN,EN,QN]
pitches04 = [G2,G3,B3,Rest,Rest]
durations04 = [EN,EN,EN,EN,QN]
pitches05 = [E2,E3,E4,Rest,Rest]
durations05 = [EN,EN,EN,EN,QN]
# create an empty phrase, and construct theme from the above motifs
theme = Phrase()
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches3, durations3)
theme.addNoteList(pitches1, durations1)  # again
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches4, durations4)
theme.addNoteList(pitches5, durations5)
theme.addNoteList(pitches6, durations6)
theme.addNoteList(pitches7, durations7)
theme.addNoteList(pitches8, durations8)
theme.addNoteList(pitches9, durations9)
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches3, durations3)
theme.addNoteList(pitches1, durations1)  # again
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches4, durations4)
theme.addNoteList(pitches5, durations5)
theme.addNoteList(pitches6, durations6)
theme.addNoteList(pitches7, durations7)
theme.addNoteList(pitches8, durations8)
theme.addNoteList(pitches9, durations9)
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches3, durations3)
theme.addNoteList(pitches1, durations1)  # again
theme.addNoteList(pitches2, durations2)
theme.addNoteList(pitches4, durations4)
合唱
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches02, durations02)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches02, durations02)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches03, durations03)
theme.addNoteList(pitches04, durations04)
theme.addNoteList(pitches05, durations05)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches02, durations02)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches01, durations01)
theme.addNoteList(pitches02, durations02)
theme.addNoteList(pitches01, durations01)


# play it
Play.midi(theme)

