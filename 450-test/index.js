var app = new Vue({
  el: "#app",
  data: {
    state: {
      latestcommit: null,
      modalData: null,
      maps: null,
    },
    events: {
      1: {
        title: "Food market",
        body: `<p>Food stalls run by London's Community Kitchen will be serving a vast array of food and drink along the High Street between Moretons and Bradbys boarding houses.<p>
        <p><ul>
        <li>The Kind Café</li>
        <li>Chipsy (Grilled burgers and loaded chips)</li>
        <li>Brat Bros Catering (Bratwurst, hot dogs, schnitzels)</li>
        <li>Sugo Kitchen (Italian Street Food, focaccia sandwiches, handmade pasta bowls)</li>
        <li>Gully (Indian Street Food) </li>
        <li>The Cheese Toaster (Gourmet cheese toasties)</li>
        <li>Social Dhaba (Punjabi Street Food)</li>
        <li>Paella Shack (Paella)</li>
        <li>Letterbox Cookie (Handmade cookies)</li>
        <li>Lilibet’s of Windsor (Traditional Old-Fashioned sweets)</li>
        <li>1218 Plant Based Cuisine (Vegan Street Food, salad boxes, BBQ and vegan sweet treats)</li>
        <li>Ben’s Bakery (Artisan Cakes)</li>
        </ul></p>`,
        times: "noon – 6pm", //could be an array of datetimes later
        location: 17,
        classification: "Food",
      },
      2: {
        title: "Free Range Jane",
        body: `<p>Free Range Jane specialises in luxury free-range fried chicken burgers and hand cut chips. We make all our sauces in house and conscientiously source our free-range chicken from a small butcher in Wiltshire. We will be in situ on Grove Hill next to Miriam's Munchies, and will be serving delicious free-range fried chicken all afternoon.</p>
        `,
        times: "noon – 6pm", //could be an array of datetimes later
        location: 100,
        classification: "Food",
      },
      3: {
        title: "Miriam's Munchies",
        body: `<p>Miriam's Munchies is a women led artisan bakery and coffee van, based locally in Harrow. Since 2007, we have been baking delicious cakes using high quality, seasonal and locally sourced ingredients. On our mobile coffee van, we’ll be serving  a range of our cakes alongside coffee sourced and roasted by Monmouth Coffee Company, Birchall teas, and homemade iced teas and chai. <a href="https://www.miriamsmunchies.co.uk/coffee-van/">www.miriamsmunchies.co.uk/coffee-van/</a></p>`,
        times: "noon – 6pm", //could be an array of datetimes later
        location: 100,
        classification: "Food",
      },
      4: {
        title: "WI Cake Stall",
        body: `<p>A selection of wonderful home-made cakes for sale.</p>`,
        times: "noon – 6pm", //could be an array of datetimes later
        location: 12,
        classification: "Food",
      },
      5: {
        title: "Archery",
        body: ``,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 11,
        classification: "Event",
      },
      6: {
        title: "ArtPerUk Peruvian Dance",
        body: `<img src="./assets/media/ArtPerUk.jpeg" width=100% height=auto> <p>ArtPerÚK is a Peruvian folkloric dance academy that promotes Peruvian traditional dances from the Coast, the Andes and the Jungle of Peru, enhancing people to explore the diversity, music and rhythms of Latin American culture with the wider community in London. Allowing them to appreciate the artistic richness of culture. Our main goal is to continue promoting our traditions and heritage in the UK.</p>`,
        times: "2pm – 3pm", //could be an array of datetimes later
        location: 7,
        classification: "Event",
      },
      7: {
        title: "Art, Photography and Sculpture Exhibitions",
        body: `<p>Work by local schools and adult art groups</p>`,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 14,
        classification: "Event",
      },
      8: {
        title: "Art Workshop",
        body: `<p><strong>Queen Elizabeth I and John Lyon Figures</strong></p>
        <p>Our two prestigious life-size figures need your help to decorate them and make them look as glorious as possible! Just drop by, and spend as long or as little as you like.</p>
        <p><strong>Stained-Glass Windows</strong></p>
        <p>Inspired by the John Lyon window, decorate your own historical window to take home and make your windows glow!</p>
        <p><strong>Victorian Photographic Studio</strong></p>
        <p>Thinking of Harrow School in Victorian times, and create your own photo studio... with a difference!</p>`,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 12,
        classification: "Event",
      },
      9: {
        title: "Barefoot Dance",
        body: ``,
        times: "2.45pm, 4.15pm", //could be an array of datetimes later
        location: 10,
        classification: "Event",
      },
      10: {
        title: "Basketball",
        body: `<p>Harrow school and the local community Basketball clubs will play a 3 vs 3 competition in the Harrow school sports hall, culminating in a final between the top two teams. Following this, Harrow schools current senior first team will play a recent leavers OH team in an exciting exhibition match.</p>`,
        times: "2pm – 4.30pm", //could be an array of datetimes later
        location: 20,
        classification: "Event",
      },
      11: {
        title: "Bollywood Dance by Quainton Hall",
        body: ``,
        times: "3.15pm – 3.45pm", //could be an array of datetimes later
        location: 7,
        classification: "Event",
      },
      12: {
        title: "Cara Gael Irish Dance Group",
        body: ``,
        times: "3.15pm, 4.45pm", //could be an array of datetimes later
        location: 10,
        classification: "Event",
      },
      13: {
        title: "Community Production: Noye's Fludde",
        body: `<p>A flood is coming, but Noah is building a boat, in the hope that a new world will be waiting on the other side.</p>
        <p>As part of Harrow School's Community Day, members of the Drama and Music departments direct a joyous new production of Benjamin Britten's community opera, combining the talents of more than a hundred children from four primary schools: Byron Court, Norbury, St Anselm's and St Jerome's from across the borough, and Bishopshalt School.</p>
        `,
        times: "2pm, 5pm", //could be an array of datetimes later
        location: 6,
        classification: "Event",
      },
      14: {
        title: "Costume-themed Streets",
        body: `<p>Victorian West Street, Edwardian High Street, Elizabethan Old Schools, and the Church. With many thanks to the members of the Harrow on the Hill Women's Institute for the more than 600m of wonderful handmade bunting and to the boys of Harrow School for all the flags.</p>
        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 21,
        classification: "Event",
      },
      15: {
        title: "Cricket Festival",
        body: `<p>Youth cricket teams: Harrow CC, Harrow Town CC, Harrow St Mary’s CC, Newton Farm Primary School, Byron Court Primary School, Pinner Park Primary School, Whitchurch Primary School, and West Lodge Primary School.</p>
        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 22,
        classification: "Event",
      },
      16: {
        title: "Edwardian Harrow Beak Reads Virgil",
        body: ``,
        times: "2.40pm – 3pm", //could be an array of datetimes later
        location: 3,
        classification: "Event",
      },
      17: {
        title: "Fives",
        body: `<p>On the main fives courts, initial celebrations will start with an exciting exhibition match between the top seeded players in the school. On the others courts, highly qualified coaches and some senior boys will run a taster session for all those who wish to trial the game. The afternoon will then conclude with a festival style tournament between the Harrow boys and some community players.</p>`,
        times: "2pm – 4pm", //could be an array of datetimes later
        location: 28,
        classification: "Event",
      },
      18: {
        title: "Harrow Community Gospel Choir",
        body: `<p><a href="https://harrowcommunitygospelchoir.com">Harrow Community Gospel Choir</a> is a performing choir singing a mixture of contemporary gospel songs and spirituals. The choir is directed by CeCelia Wickham-Anderson, a member of the internationally acclaimed acapella singing group <a href="http://blackvoices.co.uk">Black Voices</a></p>
        `,
        times: "3.30pm, 5.15pm", //could be an array of datetimes later
        location: 11,
        classification: "Event",
      },
      19: {
        title: "Harrow Hill Trust Guided Walk",
        body: `<p>The Harrow Hill Trust will hold a guided tour of the Hill led by Jonathan Edwards. The walk will take in some of the events, people and buildings that helped shape the Hill, from Tudor times through to the 21st Century.</p>
        <p>Please register for this walk, for which there is no charge, with Robert Lemon  07836 638620 <a href="mailto:robertlemon@live.co.uk">robertlemon@live.co.uk</a></p>
        `,
        times: "3pm – 4pm", //could be an array of datetimes later
        location: 19,
        classification: "Event",
      },
      20: {
        title: "Harrow Steel Band",
        body: `<p>Harrow Steel was formed in 1992 and provides an opportunity for gifted and talented young musicians aged 8-21 to learn challenging music aurally within a steel band. We support the engagement of musical talent, in a multicultural environment across Harrow and NW London. Weekly rehearsals are held at Whitmore High School in Harrow.</p>
        <p>We have performed at Notting Hill Carnival on three occasions, where we were voted ‘Best Band on the road’. Other notable performances have been for BBC programmes such as Blue Peter, Record Breakers, and You and Me. The Band have also toured Europe and performed in Barcelona, Salzburg, Paris, Lake Garda, Venice, Ostend, and Amsterdam.</p>
        <p>We are very proud of our Alumni, many of whom still perform and help voluntarily within the band, our trustees include ex band members and their parents. Others have gone on to be teachers, leaders of arts organisations and practising musicians.</p> <p>Our funders include: John Lyon's Charity, Harrow Giving, and the Young Harrow Foundation.</p> 
        <p>Please get in touch for further info: <a href="mailto:bandmanager@harrowsteel.org.uk">bandmanager@harrowsteel.org.uk</a></p>
        `,
        times: "2pm, 3.45pm, 5pm", //could be an array of datetimes later
        location: 4,
        classification: "Event",
      },
      21: {
        title: "The Hill Players",
        body: `<p>"Banter" by Robert Scott. John and Angie are having a quiet conversation before breakfast – or so it would seem. Luckily for us, they each have an interpreter on hand so we can understand what they are really saying.</p>
        <p>The Hill Players is an ever-growing amateur dramatics group founded in 2007 and based around Harrow on the Hill. We are passionate about community theatre and pride ourselves on putting on great productions, including an annual Christmas Panto at Harrow School's Ryan Theatre. We welcome new members! Please see our website <a href="https://www.hillplayers.co.uk">hillplayers.co.uk</a> for more information.</p>
        `,
        times: "2pm – 6pm, every half hour", //could be an array of datetimes later
        location: 101,
        classification: "Event",
      },
      22: {
        title: "Indie Choir",
        body: `<p>Harrow's very own Indie Choir sings a wide range of alternative and contemporary rock and pop songs, from the Beatles to Bowie to Bastille. Launched in September 2017, the choir has performed live at Rickmansworth Festival, Harrow's Heroes, Headstone Manor, and at pubs, bars, venues, and parties in Harrow and Hillingdon.</p>
        <p>Indie Choir meets upstairs at Trinity Bar in central Harrow on Thursday nights, and more details can be found on the web (<a href="https://www.indiechoir.com">indiechoir.com</a>), Facebook (<a href="https://www.facebook.com/indiechoir">@indiechoir</a>) and Instagram (<a href="https://www.instagram.com/indiechoiruk/">@indiechoiruk</a>).</p>
        `,
        times: "2.45pm, 4.15pm, 5.30pm", //could be an array of datetimes later
        location: 4,
        classification: "Event",
      },
      23: {
        title: "John Lyon School Drama",
        body: `<p>A showcase of material from John Lyon’s upcoming modern interpretation of Shakespeare’s The Tempest, adapted for the Harrow and Hill Community Day.</p>`,
        times: "2pm – 2.30pm", //could be an array of datetimes later
        location: 3,
        classification: "Event",
      },
      24: {
        title: "Kidology",
        body: `<p>Kidology Dance Co was established in 2010 by Nicky Rutter and Lauren O'Connell. We have a passion for performing, teaching and helping young people to realise their talents and progress within their future in dance. We specialise in street/Hip-Hop dance, contemporary, musical theatre and have directed and produced a number of sold-out shows, competed in competitions throughout the country and had dancers go on to do remarkable things. Our aim is to work with dancers to enhance their talents, draw on their strengths and build their confidence. We are very fortunate to work with a thriving and well-presented group of young and talented students. We encourage everyone to take part in as many performance opportunities as they can throughout the year especially if dance is something they wish to pursue later in life. <a href="http://www.kidologydance.co.uk">www.kidologydance.co.uk</a></p>
        `,
        times: "3pm, 4.15pm", //could be an array of datetimes later
        location: 11,
        classification: "Event",
      },
      25: {
        title: "Maypole Dance",
        body: `<p>Vaughn Primary School</p>`,
        times: "2.30pm – 2.45pm, 4.00pm – 4.15pm", //could be an array of datetimes later
        location: 5,
        classification: "Event",
      },
      26: {
        title: "Merrydowners Morris",
        body: `<p>Founded in 1990 as a fun entry in a local Church Fete (St. Alban, North Harrow), we practised in secret as, at the time, one of the team was the vicar of the church, so you can imagine the gasps of surprise at our debut! We enjoyed the experience so much that several of the original church members are still performing. During the past 31 years we have performed across London, in France and Germany, the highlights being: The Guildhall, City of London, for the inaugural Dinner of the 1996 European football championships; representing England at The Hong Kong Chinese New Year parade in 2004; La Fetes du Gayants, Douai Pas de Calais in 2001 and 2003; Recklinghausen Germany for the annual Concert of The Akkordeonklaenge von Recklinghausen Westfallen in 2005. We took part many times in London’s New Year’s Day parade and have also appeared in a pop music video and, albeit briefly, on the BBC’s Strictly Come Dancing and also on The One Show! We were also honoured to be included in Harrow’s Diamond Jubilee celebrations and performed for HRH The Duke of Edinburgh.</p>
        `,
        times: "2pm, 3pm, 4pm, 5pm", //could be an array of datetimes later
        location: 1,
        classification: "Event",
      },
      27: {
        title: "Music at the Bandstand",
        body: `<p>Enjoy a full programme of traditional bandstand entertainment including brass, wind and concert bands.</p>
        <table>
        <tr><td>2.00pm</td><td>Orley Farm (Year 8 Rock Band, String Quartet and Chamber Choir)</td></tr>
        <tr><td>2.30pm</td><td>John Lyon and Quainton Hall</td></tr>
        <tr><td>3.00pm</td><td>Traditional Irish Music</td></tr>
        <tr><td>3.30pm</td><td>The Aftercare (Harrow School)</td></tr>
        <tr><td>4.00pm</td><td>Traditional Irish Music</td></tr>
        <tr><td>4.30pm</td><td>ohn Lyon and Quainton Hall</td></tr>
        <tr><td>5.00pm</td><td>Traditional Irish Music</td></tr>
        <tr><td>5.30pm</td><td>The Aftercare (Harrow School)</td></tr>
        </table>
        <p>The London Irish Music School was established in 1999 under the direction of Colette Keaveney (TTCT) who is a qualified teacher of Traditional Irish Music registered with Comhaltas Ceoltoiri Eireann in Dublin, Ireland.</p>
        <p>The aim of Comhaltas Ceoltoiri Eireann is to promote the Music, Culture and Arts of Ireland at Home and Abroad. The London Irish Music School’s main objective is to fulfil this aim and to be able to reach as many children as possible.</p>
        <p>Weekly classes take place during term time at a community venue in Brent and at two schools in Harrow as part of their music curriculum.</p>
        <p>Workshops are held regularly with different tutors in a small group or individual setting to give more in-depth tuition, once children have passed the beginner stage and progressed onto a second instrument.</p>
        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 2,
        classification: "Event",
      },
      28: {
        title: "Old Speech Room Gallery 450 Exhibition",
        body: `<p>Harrow 1572-2022: from the time of Elizabeth I to the present day, this exhibition is a visual tour through time, full of local legend and newly researched revelations.</p>
        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 23,
        classification: "Event",
      },
      29: {
        title: "Punch and Judy Show and Magician",
        body: ``,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 24,
        classification: "Event",
      },
      30: {
        title: "Rayleigh Observatory",
        body: `<p>Find out about the observation of planets, galaxies and other astronomical phenomena.</p>        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 25,
        classification: "Event",
      },
      31: {
        title: "Roystonjax",
        body: `<p>RoystonJax are a trio with a difference. They use stripped down to bass/drum backing tracks and play live guitars with fabulous three-part harmonies. It feels like a full band but one that can play at any volume in any venue!</p>
        `,
        times: "3.15pm, 5.30pm", //could be an array of datetimes later
        location: 4,
        classification: "Event",
      },
      32: {
        title: "Stagecoach Irish Dance Group",
        body: `<p>Stagecoach Harrow is in its 29th Year and was one of the first Stagecoach schools to open based at Rooks Heath College. Emmy Hamilton has been Principal for 15 of those years and is proud to be at the head of this energetic and creative Performing Arts School in the borough. At this event are dedicated students from Stagecoach Harrow's Dance Troupe (performing some street and musical theatre) and our 15+ year group 'Further Stages' who will be performing some of their Performance Arts Awards Exam work, based on life in 1940s. There are two other Stagecoach centres in the borough: Stagecoach Harrow on the Hill and Stagecoach Harrow Weald, all three providing quality, nurturing environments in part time performing arts lessons for our students to thrive in, from 4-19 years, with lots of opportunities for students to be themselves, develop skills and confidence, make new friends, and have a chance to shine. Professional work and West End opportunities along with added value in LAMDA lessons are also available. Enquire at <a href="https://www.stagecoach.co.uk/harrow">www.stagecoach.co.uk/harrow</a> 0203 5040100.</p>
        `,
        times: "2.15pm, 3.45pm", //could be an array of datetimes later
        location: 10,
        classification: "Event",
      },
      33: {
        title: "St Mary's",
        body: `<p>After listening to the bellringing opening the Community Day why not climb the tower and go onto the flat roof (weather permitting) to see the stunning views of the Hill and London.  Come and meet Elizabeth I and John Lyon, who founded the School and other characters in costume who will tell you some of the history of the School and church. Visit the church where boys worshipped before the chapel was built, including prime ministers Robert Peel and Spencer Percival and authors Lord Byron, Sheridan, and Anthony Trollope. Go on our churchyard trail or have a cuppa at our Spire Cafe.</p>
        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 19,
        classification: "Event",
      },
      34: {
        title: "String Quartet and Brass Trio",
        body: ``,
        times: "3.30pm – 4.30pm", //could be an array of datetimes later
        location: 3,
        classification: "Event",
      },
      35: {
        title: "Tai Chi",
        body: `<p>We are a community tai chi group called Harrow Tai Chi for Health. We offer free tai chi sessions at Harrow Recreation Ground every Friday 9.30 to 10.30am for health and general well-being. For more information please email <a href="mailto:info@harrowrec.org.uk">info@harrowrec.org.uk</a></p>
        `,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 11,
        classification: "Event",
      },
      36: {
        title: "Tours of Harrow School",
        body: `<p>Public tours of Harrow School's historic venues on the hour, every hour. Our expert guides will share an insight into Harrow's 450-year history. This is an exciting opportunity for members of the public to visit some of the most spectacular and historic buildings at Harrow School. Tours last 30–40 minutes.</p>

        <p>To register your attendance please email Victoria Perry on <a href="mailto:tours@harrowschool.org.uk">tours@harrowschool.org.uk</a> with your name, contact number and the number of places you would like to book, and your preferred tour time.</p>
        `,
        times: "12pm, 1pm, 2pm, 3pm, 4pm, 5pm", //could be an array of datetimes later
        location: 11,
        classification: "Event",
      },
      37: {
        title: "Veteran Cars",
        body: ``,
        times: "2pm – 6pm", //could be an array of datetimes later
        location: 26,
        classification: "Event",
      },
      38: {
        title: "The Pie Stall",
        body: `<p>We will be selling delicious pies from across the centuries, both savoury and sweet. Come and select a filling of your choice! Proceeds from sales will be donated to Paws for Cause.</p>`,
        times: "noon – 6pm", //could be an array of datetimes later
        location: 11,
        classification: "Food",
      },
      39: {
        title: "Spire Cafe",
        body: `<p><ul>
        <li>Homemade soup and fresh rolls</li>
        <li>Hot filled rolls</li>
        <li>Cream teas featuring Spire Cafe's famous scones, fresh from the oven</li>
        <li>Home-baked cakes</li>
        <li>Fairtrade teas and coffees</li>
        <li>Cold drinks including our homemade mango lassi</li>
        </ul></p>
        <p>For updates, find us <a href="https://tinyurl.com/spirecafeharrow">on the web</a> and <a href="https://twitter.com/SpireCafe">on Twitter @SpireCafe.</a></p>`,
        times: "noon – 6pm", //could be an array of datetimes later
        location: 19,
        classification: "Food",
      },
      40: {
        title: "Athletics",
        body: `<p>Harrow School and Harrow Athletics Club will combine to compete in an afternoon of athletics. This festival will see 48 Harrow athletes compete against Harrow AC in a refined range of events, highlighting the key disciplines within the sport and strengthening the connection between the school and local community.</p>`,
        times: "2.15pm – 4.45pm", //could be an array of datetimes later
        location: 27,
        classification: "Event",
      },
      41: {
        title: "Judo",
        body: `<p>The judo celebrations will begin with an exhibition training session at 2pm. Boys will demonstrate the main elements of judo training, including traditional warm-up and agility exercises, breakfalls, uchi-komi (technical drills) for standing and groundwork, contest technique, and randori (sparring). The session will conclude with some inter-house exhibition contests. At 3:30pm there will then be an expert demonstration of Nage-no-kata, which is one of the main katas (formal demonstrations) of Kodokan Judo. It is intended as an illustration of the various concepts of throwing that exist in judo and is used both as a training method and as a demonstration of understanding. From 4-5pm there will be a taster session for anyone who would like to try judo.</p>`,
        times: "2pm – 5pm", //could be an array of datetimes later
        location: 28,
        classification: "Event",
      },
      42: {
        title: "Rackets",
        body: `<p>On the main rackets court there will be an exciting exhibition match between the top seeded players in the school. On the second court, highly qualified coaches will run a taster session for all those who wish to trial the game and gain experience of the pace of the ball and play. All are welcome and kit and equipment will be provided.</p>`,
        times: "2.15pm – 4.30pm", //could be an array of datetimes later
        location: 28,
        classification: "Event",
      },
      43: {
        title: "Squash",
        body: `<p> A sport invented at Harrow School, this squash event will feature exhibition matches between the School’s first and second seed (former number 1 in Asia U16 and current top 40 U18 UK), and members of the Harrow Leisure Centre Squash Club. On the second glass back court, the captain and vice captain (Ilyas Qureshi and Hanno Sie) will offer a taster session and training for all that wish to come and take part.</p>`,
        times: "1pm – 4pm", //could be an array of datetimes later
        location: 28,
        classification: "Event",
      },
    },
    locations: {
      100: {
        title: "UNKNOWN - GROVE HILL",
        coords: {
          lat: 0,
          lng: 0,
        },
        icon: "./assets/icons/food.png",
      },
      101: {
        title: "UNKNOWN - The Old Well",
        coords: {
          lat: 0,
          lng: 0,
        },
        icon: "./assets/icons/drama.png",
      },
      1: {
        title: "The Castle",
        coords: {
          lat: 51.5721,
          lng: -0.34,
        },
        icon: "./assets/icons/music.png",
      },
      2: {
        title: "The Band Stand",
        coords: {
          lat: 51.570709547070194,
          lng: -0.33953382679834193,
        },
        icon: "./assets/icons/music.png",
      },
      3: {
        title: "The Park Drive",
        coords: {
          lat: 51.57107799697978,
          lng: -0.33864699551627864,
        },
        icon: "./assets/icons/drama.png",
      },
      4: {
        title: "The Roof Terrace",
        coords: {
          lat: 51.572615028201376,
          lng: -0.3381793112539503,
        },
        icon: "./assets/icons/music.png",
      },
      5: {
        title: "The Old House",
        coords: {
          lat: 51.572306622419745,
          lng: -0.337707242462523,
        },
        icon: "./assets/icons/drama.png",
      },
      6: {
        title: "Speech Room",
        coords: {
          lat: 51.57388032088066,
          lng: -0.3365924234147868,
        },
        icon: "./assets/icons/drama.png",
      },
      7: {
        title: "Vaughan Library “Forecourt”",
        coords: {
          lat: 51.5729784615626,
          lng: -0.33683114001183134,
        },
        icon: "./assets/icons/drama.png",
      },
      8: {
        title: "Behind the Vaughan",
        coords: {
          lat: 51.57288677430271,
          lng: -0.3364073509924032,
        },
        icon: "./assets/icons/drama.png",
      },
      9: {
        title: "The Head Master’s Yard",
        coords: {
          lat: 51.57256920155196,
          lng: -0.33677481362631606,
        },
        icon: "./assets/icons/drama.png",
      },
      10: {
        title: "War Memorial Building Forecourt",
        coords: {
          lat: 51.57334270818231,
          lng: -0.3370028013856397,
        },
        icon: "./assets/icons/drama.png",
      },
      11: {
        title: "Bill Yard",
        coords: {
          lat: 51.57317433825023,
          lng: -0.3374212259876906,
        },
        maplocation: {
          x: (2706 / 4365) * 100,
          y: (921 / 4932) * 100,
        },
        icon: "./assets/icons/music.png",
      },
      12: {
        title: "Druries Steps",
        coords: {
          lat: 51.572975960994754,
          lng: -0.3373541707638017,
        },
        icon: "./assets/icons/drama.png",
      },
      13: {
        title: "Art Schools",
        coords: {
          lat: 51.57465043293017,
          lng: -0.33585118104491185,
        },
        icon: "./assets/icons/arts.png",
      },
      14: {
        title: "Passmore Gallery",
        coords: {
          lat: 51.5741953456611,
          lng: -0.3362347369255564,
        },
        icon: "./assets/icons/arts.png",
      },
      15: {
        title: "Grove Hill Portaloos",
        coords: {
          lat: 51.573988106438506,
          lng: -0.33615847667901955,
        },
        icon: "./assets/icons/wc.png",
      },
      16: {
        title: "Harrow Park Portaloos",
        coords: {
          lat: 51.56982528515575,
          lng: -0.3391569089820675,
        },
        icon: "./assets/icons/wc.png",
      },
      17: {
        title: "Food Stalls",
        coords: {
          lat: 51.57150259260376,
          lng: -0.33864416430660427,
        },
        icon: "./assets/icons/food.png",
      },
      18: {
        title: "Picnic Area",
        coords: {
          lat: 51.572578688703,
          lng: -0.3376919801021046,
        },
        icon: "./assets/icons/picnic.png",
      },
      19: {
        title: "St Mary's",
        coords: {
          lat: 51.574059316831075,
          lng: -0.3371416801004325,
        },
        icon: "./assets/icons/arts.png",
      },
      20: {
        title: "Sports Centre",
        coords: {
          lat: 51.57284119432785,
          lng: -0.33363183575090516,
        },
        icon: "./assets/icons/basketball.png",
      },
      21: {
        title: "High St Central",
        coords: {
          lat: 51.57300373087044,
          lng: -0.3370087369049427,
        },
        icon: "./assets/icons/drama.png",
      },
      22: {
        title: "Cricket Pitches",
        coords: {
          lat: 51.57312466150709,
          lng: -0.34379332137733504,
        },
        icon: "./assets/icons/cricket.png",
      },
      23: {
        title: "The OSRG",
        coords: {
          lat: 51.573293900355104,
          lng: -0.3372359341674162,
        },
        icon: "./assets/icons/arts.png",
      },
      24: {
        title: "Outside Bradbys",
        coords: {
          lat: 51.571293418778446,
          lng: -0.3389576839538226,
        },
        icon: "./assets/icons/drama.png",
      },
      25: {
        title: "The Rayleigh Observatory (Maths and Physics Schools)",
        coords: {
          lat: 51.57349321757922,
          lng: -0.3348936927102774,
        },
        icon: "./assets/icons/arts.png",
      },
      26: {
        title: "The Old King's Head (The Gantry)",
        coords: {
          lat: 51.570454847756,
          lng: -0.339785273378362,
        },
        icon: "./assets/icons/arts.png",
      },
      27: {
        title: "Athletics Ground",
        coords: {
          lat: 51.57228024078023,
          lng: -0.3329113428644686,
        },
        icon: "./assets/icons/athletics.png",
      },
      28: {
        title: "Hundred Steps",
        coords: {
          lat: 51.57317711287312,
          lng: -0.33851045418652276,
        },
        icon: "./assets/icons/steps.png",
      },
    },
  },
  methods: {
    dateformat(input) {
      return new Date(input).toLocaleDateString("en-GB", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
      });
    },
    invalidatemap() {
      this.state.maps.invalidateSize();
    },
    modalOpened() {
      if (this.state.maps) {
        this.state.maps.remove();
      }

      if (this.state.glass) {
        this.state.glass = null;

        document.getElementById("inject11").innerHTML = "";
      }

      var button = event.relatedTarget;
      var locationid = button.getAttribute("data-bs-locationid");

      var location = this.locations[locationid];

      this.state.maps = L.map("mainMap" + locationid);

      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZHlsYW5rMTIzIiwiYSI6ImNrajUwMm55NzV0NWwyc2xiNzk0OHFjdXoifQ.cIzWvi9HlI1YfhpY24KbTA",
        {
          maxZoom: 18,
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          id: "dylank123/ckl2u73iy1s5v17tjzyld3nzl",
          tileSize: 512,
          zoomOffset: -1,
        }
      ).addTo(this.state.maps);

      var icon = L.icon({
        iconUrl: location.icon,
        //shadowUrl: 'leaf-shadow.png',

        iconSize: [25, 25], // size of the icon
        // shadowSize:   [50, 64], // size of the shadow
        // iconAnchor:   [12.5, 12.5], // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        // popupAnchor:  [12.5, 12.5] // point from which the popup should open relative to the iconAnchor
      });

      var marker = L.marker([location.coords.lat, location.coords.lng], {
        icon: icon,
      })
        .addTo(this.state.maps)
        .bindPopup(location.title);

      this.state.maps.setView([location.coords.lat, location.coords.lng], 17);

      setTimeout(this.invalidatemap, 500);

      // Create a `Glass` (image) object and inject it into an existing element with the `injectGlass` shorthand
      this.state.glass = injectGlass(
        document.getElementById("inject" + locationid),
        "./assets/450_map.jpg"
      );

      // Add a smaller default Octopus at same location
      // but using percent as unit (given image width of 1000px and height of 667px)
      this.state.glass.addOctopus(
        location.maplocation.x,
        location.maplocation.y,
        {
          radius: 5,
          margin: 2,
          positionUnit: "%",
        }
      );
    },
  },
  mounted() {
    axios
      .get(
        "https://api.github.com/repos/harrowschool/harrowschool.github.io/commits?per_page=1"
      )
      .then((response) => (this.state.latestcommit = response.data[0]));

    var mainMap = L.map("mainMap");

    window.addEventListener("show.bs.modal", this.modalOpened);
    window.addEventListener("hide.bs.modal", (e) => {
      // remove the word "locationModal" from the string to get the location id
      var locationid = e.target.id.replace("locationModal", "");
      document.getElementById("inject" + locationid).innerHTML = "";
    });

    L.tileLayer(
      "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZHlsYW5rMTIzIiwiYSI6ImNrajUwMm55NzV0NWwyc2xiNzk0OHFjdXoifQ.cIzWvi9HlI1YfhpY24KbTA",
      {
        maxZoom: 18,
        attribution:
          'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
          'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: "dylank123/ckl2u73iy1s5v17tjzyld3nzl",
        tileSize: 512,
        zoomOffset: -1,
      }
    ).addTo(mainMap);

    Object.entries(this.locations).forEach((entry) => {
      const [id, location] = entry;
      var icon = L.icon({
        iconUrl: location.icon,
        //shadowUrl: 'leaf-shadow.png',

        iconSize: [25, 25], // size of the icon
        // shadowSize:   [50, 64], // size of the shadow
        // iconAnchor:   [12.5, 12.5], // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        // popupAnchor:  [12.5, 12.5] // point from which the popup should open relative to the iconAnchor
      });

      var marker = L.marker([location.coords.lat, location.coords.lng], {
        icon: icon,
      })
        .addTo(mainMap)
        .bindPopup(
          `
        <button type="button" class="btn btn-danger btn-sm pl-2" data-bs-toggle="modal"
          data-bs-locationid="` +
            id +
            `" data-bs-target="#locationModal` +
            id +
            `">` +
            this.locations[id].title +
            `</button>
      `
        );
    });

    mainMap.setView([51.57281743898807, -0.3371716811246794], 17);

    // shows user's location on map
    // function onLocationFound(e) {
    //     var radius = e.accuracy / 2;

    //     var locationMarker = L.marker(e.latlng).addTo(mymap)
    //         .bindPopup('You are within ' + radius + ' meters from this point').openPopup();

    //     var locationCircle = L.circle(e.latlng, radius).addTo(mymap);
    // }

    // function onLocationError(e) {
    //     alert(e.message);
    // }

    // mymap.on('locationfound', onLocationFound);
    // mymap.on('locationerror', onLocationError);

    // mymap.locate({ setView: true, maxZoom: 16 });
  },
});
