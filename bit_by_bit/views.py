# -*- coding: utf-8 -*-
# Since there are non-ascii symbols in this file specify it in the first line


# Import function to render given html page
from django.shortcuts import render


# Create a class representing an article
class Article:
    # Constructor has been using to create a new instance of the class
    def __init__(self, title, content):
        self.title = title
        self.content = content


# Create a function to process accessing to the index page
# request here is an object came with a client's request
def index(request):

    # Create three instances of Article class providing initial data
    article1 = Article(
        title='Matryoshka doll',
        # You can use three quotes to create multiline strings
        content=''' A matryoshka doll (Russian: матрёшка; IPA: [mɐˈtrʲɵʂkə] ( listen), matrëška), also known as a Russian nesting doll, or Russian doll,[1] is a set of wooden dolls of decreasing size placed one inside another. The name "matryoshka" (матрёшка), literally "little matron", is a diminutive form of Russian female first name "Matryona" (Матрёна) or "Matriosha".[2]
                    A set of matryoshkas consist of a wooden figure which separates, top from bottom, to reveal a smaller figure of the same sort inside, which has, in turn, another figure inside of it, and so on.
                    The first Russian nested doll set was made in 1890 by Vasily Zvyozdochkin from a design by Sergey Malyutin, who was a folk crafts painter at Abramtsevo. Traditionally the outer layer is a woman, dressed in a sarafan, a long and shapeless traditional Russian peasant jumper dress. The figures inside may be of either gender; the smallest, innermost doll is typically a baby turned from a single piece of wood. Much of the artistry is in the painting of each doll, which can be very elaborate. The dolls often follow a theme; the themes may vary, from fairy tale characters to Soviet leaders. Matryoshka dolls are often referred to as "babushka dolls", babushka meaning "grandmother" or "elderly woman".'''
        )

    article2 = Article(
        title='Gusli',
        content=''' Gusli (Russian: гу́сли; IPA: [ˈɡuslʲɪ]) is the oldest Russian multi-string plucked instrument. Its exact history is unknown. It may have derived from a Byzantine form of the Greek kythare, which in turn derived from the ancient lyre. It has its relatives throughout the world: kantele in Finland, kannel in Estonia, kanklės, or kokle in Lithuania and Latvia. Furthermore, the kanun has been found in Arabic countries, and the autoharp, in the United States. It is also related to such ancient instruments as Chinese gu zheng, which has a thousand-year history, and its Japanese relative koto.'''
        )

    article3 = Article(
        title='Kokoshnik',
        content=''' The kokoshnik (Russian: коко́шник; IPA: [kɐˈkoʂnʲɪk]) is a traditional Russian headdress worn by women and girls to accompany the sarafan, primarily worn in the northern regions of Russia in the 16th to 19th centuries.
                    Historically a kokoshnik is a headdress worn by married women, though maidens wore a headdress very similar to a kokoshnik, but open in the back, named a povyazka.[1] The word kokoshnik describes a great variety of headdresses worn throughout Russia, including the cylindrical hats of Veliky Novgorod, two-pointed nimbus kika of Vladimir, triangular kika of Kostroma, small pearl hats of Kargopol, and scarlet kokoshniks of Moscow.
                    While in the past kokoshnik styles varied greatly, currently a kokoshnik is generally associated with a tall, nimbus or crest shaped headdress which is tied at the back of the head with long thick ribbons in a large bow. The crest can be embroidered with pearls and goldwork or simple applique, usually using plant and flower motifs. The forehead area is frequently decorated with pearl netting. While wearing a kokoshnik the woman usually wears her hair in a plait. It resembles the French hood worn in Tudor England, but without the black veil.'''
        )

    # Create a dictionary passed to html page
    # In our case we pass three Article instanses to render it on the page
    context = {
        'article1': article1,
        'article2': article2,
        'article3': article3
    }

    # 2nd parameter is a name of html template to send context dictionary to
    return render(request, 'bit_by_bit/index.html', context)
