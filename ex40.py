# All the Code Written By Asif date 27th September 2021
#  Mdule,Class and Object
class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def Something_else(self):
        print("you are done.")        

happy_bday = Song(["Happy birthday to you",
                    "I dont want to get sued",
                    "So I'll stop right there"])

bulls_on_prade = Song(["They really around the family",
                        "with pockets full of shells"])

another_song = Song(["here your another song...."])                        

happy_bday.sing_me_a_song()

bulls_on_prade.sing_me_a_song()

another_song.sing_me_a_song()

another_song.Something_else()

