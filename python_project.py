from flask import Flask, render_template, request



import sqlite3
from readDB import addDogs, readDogs


app = Flask(__name__)

@app.route('/')
def home_page():
    page = """
            <html>
            <head>
            <title>dogs lovers</title>
            <style> body{
                background-color: lightblue;

                </style>

            </head>
            <body>
           <h1> <center>Welcome to dogs lovers   &#128021;</center></h1>

            <p> <h2>This page was made to help you to know more about dogs and there kinds</h2></p>
            <P>   </p>

            <p><h2>here you can find kind that you need and see information about</h2> </p>

                <p>   </p>
                <style>
                a:link, a:visited {
                background-color: #f44336;
                color: black;
                padding: 14px 25px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                }

                a:hover, a:active {
                background-color: yellow;
                }
                </style>
                <body>

                <p>click here to choose:</p>

                </body>
             <h2><a href="inf"> <front c0l0r="black"size="5">Click here to choose kind</front></a></h2>
             <p><h2>here you can add kind to us</h2> </p>
             <h2> <a href="addDogs" target="blank"> here you can add new kind </a></h2>
             <h2> here all kind that another people added</h2>
             <h2> <a href="allDogs" target="blank"> alldogs </a></h2>
            </body>
            </html>
             """
    return page

@app.route('/inf')
def information():
        return"""

        <!DOCTYPE html>
            <html>
            <head>
            <title>dogs lovers</title>
            </head>
            <body>
            <h1 style="background-color:yellow;">Here you can choose the kind that you need know information about </h1>
            <h2> <a href="German shepherd" target="blank"> 1-German shepherd </a></h2>
            <h2> <a href="Husky siberian" target="blank"> 2-Husky siberian </a></h2>
            <h2> <a href="American Leopard Hound" target="blank"> 3-American Leopard Hound </a></h2>
            <h2> <a href="Bolognese" target="blank"> 4-Bolognese </a></h2>
            <h2> <a href="Brittany" target="blank"> 5-Brittany </a></h2>
            <h2> <a href="Bull-Pei" target="blank"> 6-Bull-Pei </a></h2>
            <h2> <a href="Chion" target="blank"> 7-Chion </a></h2>
            <h2> <a href="Dalmatian" target="blank"> 8-Dalmatian </a></h2>
            <h2> <a href="Bichon Frise" target="blank"> 9-Bichon Frise </a></h2>
            <h2> <a href="Bocker" target="blank"> 10-Bocker </a></h2>
            <h1><br><a href='/'>Back to home bage</a></h1>
            </body>
            </html>

        """




@app.route('/German shepherd')
def dogs_kind():
        return render_template("homepage.html")



@app.route('/Husky siberian')
def dogs_kind2():

    return"""
<html>
<head>
<title>dogs kind</title>
</head>
<body>


 <h1> <center>Husky siberian  &#128021;</center></h1>

<p> <h2> This dog has been around for more than 3000 years, and its original place is the Siberian.
 It was used to drag goods for distances of up to 400 miles, which means more than 650 kilometers.
  This dog went to America in the 20th century and entered World War II with the American army. It i
  s a medium-sized dog and its weight.  The male is from 29 centimeters to 34 centimeters, and the
   female is from 27 centimeters to 32 centimeters, the length of the male is from 58 centimeters to
    61 centimeters, and the length of the female is from 55 centimeters to 57 centimeters, and the li
    fe expectancy of this dog is from 10 years to 12 years, and the most beautiful thing about this d
    og  His eye now has many colors, all degrees of blue and brown, and sometimes each eye is differen
    t from the other eye, for example, one eye is blue and the other is brown.  Easy to train </h2></p>


    </body>

"""

@app.route('/American Leopard Hound')
def dogs_kind3():

    return"""
<h1> <center>  American Leopard Hound &#128021;</center></h1>


     <h2>The American Leopard Hound is a purebred dog whose ancestors came from Mexico by
    way of Spanish conquistadors who sailed to North America. They are energetic, sociable,
     and intelligent pooches who possess all-around great traits.

    The American Leopard Hound goes by other names, such as the Leopard Cur, American Leopard,
    and American Leopard Cur. You can look for this pure breed by checking your local shelters
    or rescues. Remember its best to adopt and not shop!
    These sweet pups are natural hunting dogs and have very high energy.

     That means they do best in homes with big yards to run around in. They’re
      able to bond strongly with humans, which makes them well-suited for households
      of all types, from single pet parents to families with children. If you want an
       energetic dog who loves to run and keep you on your toes, alerts you to any dangers,
        and adores you completely, then this may be the right dog breed for you!</h2>
    """

@app.route('/Bolognese')
def dogs_kind4():
    return"""
    <h1> <center>  Bolognese &#128021;</center></h1>

    <h2>A true companion dog, the Bolognese dog breed loves to be at
    their family’s side. However, they also loves getting their
     way and can be quite crafty about it, so be careful — you
     could find yourself being manipulated by a ten-pound furball.
    Even though these are purebred dogs, you may find them in the care
    of shelters or rescue groups. Remember to adopt! Don’t shop if you want to bring a dog home.
    Sensitive and loving, Bologness are true companion dogs.
    They pack a lot of personality in a tiny body, and they’ll
    readily take to apartment life. These pups don’t much care
     for being left alone for long hours of the day. Instead, they’ll
     prefer to join you wherever you go. But even though these pups adore their humans,
      they also have a stubborn side when it comes to training. Teach these dogs with plenty of
       positive reinforcement and avoid harsh rebukes.
       If you do, you’ll have a loving, well behaved family member who won’t leave your side.</h2>

    """
@app.route('/Brittany')
def dogs_kind5():
    return"""
    <h1> <center>  Brittany &#128021;</center></h1>
    <h2>Brittanys were bred as gundogs, and they definitely have birds on the brain
    . Although they’re often called Brittany Spaniels, the American Kennel Club dropped the word
     “spaniel” from this pointing breed’s name in 1982.
These energetic dogs are versatile family companions and hunting dogs who work more closely
 to hunters than other pointing breeds. If you can satisfy their high energy and exercise needs,
  this may be the breed for you!
</h2>
    """

@app.route('/Bull-Pei')
def dogs_kind6():
    return"""
    <h1> <center>  Bull-Pei &#128021;</center></h1>
<h2>The Bull-Pei is a mixed breed dog–a cross between the Chinese Shar-Pei and English Bulldog breeds
. Medium in size, loving, and loyal, these pups inherited some of the best traits from both of their parents.

Despite their unfortunate status as a designer breed, you may find these pups in shelters and breed
 specific rescues, so remember to adopt! Don’t shop!
ull-Peis make excellent companions and guard dogs without being too large or requiring much exercise.
They’re striking to look at because of their wrinkles. Just make sure that you have the time to keep
your pup clean and dry, as they are prone to getting skin infections between the wrinkles.

These dogs can live in apartments or houses. If you’re looking for a chill companion dog who looks
 quite distinguished, the Bull-Pei may be perfect for you.</h2>
"""

@app.route('/Chion')
def dogs_kind7():
    return"""
    <h1><center> Chion &#128021; </center></h1>
<h2>The Chion is a mixed breed dog — a cross between the Chihuahua and Papillon dog breeds.
 Petite, playful, and loyal, these pups inherited some of the best qualities from both of their parents

Chions go by several names, including Papihuahua, Pap-Chi, and Chi-a-Pap. Despite their
 unfortunate status as a designer breed, you can find these mixed breed dogs in shelters
  and breed specific rescues, so remember to adopt! Don’t shop!
These adorable pups make great apartment dogs for active metropolitan
 dwellers, though they’re best suited to small or single-person households.
  They also have a tendency to be yappy. If you are looking for a silly,
   small dog with a big personality who will keep you on your toes, act
    as an alert dog, and stick to you like glue, this may be the right dog for you!</h2>
"""
@app.route('/Dalmatian')
def dogs_kind8():
    return"""
<h1><center> Dalmatian &#128021; </center></h1>
<h2>Best known as the star of Disney’s 101 Dalmatians,
 this sleek and athletic Dalmatian dog breed has a
 history that goes back several hundred years. They
  started out as a coach dog but also served in many
   other capacities, including hunter, firehouse dog, and circus performer.

Even though these are purebred dogs, you may find them
in the care of shelters or rescue groups. Remember to adopt! Don’t
 shop if you want to bring a dog home.
As charming in life as in film, Dalmatians go
 from gallant to goofy to gallant again in the
  blink of an eye. They love to be a part of everything
   their family does. That said, they have high energy levels and need plenty of exercise. If you’re
   looking for a jogging partner and friend who’ll love you unconditionally, this may be the breed for you!</h2>
"""
@app.route('/Bichon Frise')
def dogs_kind9():
    return"""
<h1><center> Bichon Frise &#128021; </center></h1>
<h2>The Bichon Frise (pronounced BEE-shawn FREE-say; the plural is Bichons Frises) is a cheerful,
 small dog breed with a love of mischief and a lot of love to give. With their black eyes and fluffy white coat
 , the Bichon looks almost like a child’s toy.
Even though these are purebred dogs, you may find them in the care of shelters or rescue groups. Remember to adopt! Don’t
 shop if you want to bring a dog home.
 t doesn’t take long to realize that the Bichon can be your happiest and most enthusiastic companion.
  They’re super playful and intelligent, and even novice pet parents and apartment dwellers will get
   along great with these dogs. However, they do need plenty of playtime and activity, and they don’t
    care for being left home alone for long hours of the day. If you can give your dog lots of attention and love,
     you’ll get it back tenfold from an adoring Bichon.</h2>
"""
@app.route('/Bocker')
def dogs_kind10():
    return"""
<h1><center> Bocker &#128021; </center></h1>
<h2>The Bocker is a mixed breed dog — a cross between the Cocker Spaniel and Beagle dog breeds.
 Small, affectionate, and curious by nature, these pups inherited some of the best qualities
  from both of their parents.
The Cocker Spaniel and Beagle mixes we call Bockers also go by the names Beakers or Beagle Spaniel.
 Despite their unfortunate status as a designer breed, you can find these mixed breed dogs in shelters
 and breed-specific rescues, so remember to adopt! Don’t shop!
These adorable pups do well in apartments and houses with fenced yards, whether it’s with single seniors or households with children. Just make sure the yard is secure, as they have a tendency to track and follow scents. Their wanderlust could lead them into dangerous situations, like traffic. So be careful and take extra precautions.

Bockers love endless play sessions and activity.
 They should not be left alone for long periods.
  Multiple pet families would be ideal. Isolation is their biggest enemy.
"""

@app.route('/addDogs', methods=["GET","POST"])
def home():
    if request.method == "GET":
        page = """<form method='post'>
        <form action="/action_page.php">
  <fieldset>
    <legend>Thanks for sharing :</legend>
            <label for="name">name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="description">description:</label><br>
            <input type="text" id="description" name="description"><br>
            <label for="link">link of photo:</label><br>
            <input type="text" id="link" name="link">
            <input type="submit" value="Submit">
               <p>    </p>
              <p>    </p>
              <h1><br><a href='/'>Back to home bage</a></h1>
              </fieldset>
</form>
            </form>"""
        return page


    elif request.method=="POST":

            name = request.form['name']
            description = request.form['description']
            link = request.form['link']
            con = sqlite3.connect('dogs.db')
            status = addDogs(con,name, description, link)
            con.close()
            if status:
                msg = "<h1>   THANKS     </h1>"
            else:
                msg = "error"
            page = f""" your dog name : {name}
            <p>    </P>
               description  :{description}
             <p>    </p>
             Link of photo : {link}

             """
            link = "<br> <a href='/'>Back to home bage </a>"
            return msg+"    <p>    </p>   "+page+  "    <p>    </p>   "   +link



@app.route("/allDogs")
def allStudent():
    con = sqlite3.connect('dogs.db')

    data = readDogs(con)
    con.close()
    page = str()
    num=1
    page2=" <h1><br><a href='/'>Back to home bage</a></h1>"
    for n in data:
        page +=f"{num}-<h2> dog name : {n[1]}</h3>"
        page +=f"<h3> description : {n[2]}</h5>"
        page +=f"<h3> Link :  {n[3]}</h5>"
        num+=1
    return page + page2

