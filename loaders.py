from google.appengine.ext import webapp

WSJ = {"site": {
		"label":"Wall Street Journal",
		"url":"http://online.wsj.com/home-page",
		"feeds": [
			{
				"label":"Home US",
				"url": "http://online.wsj.com/xml/rss/3_7011.xml"
			},
			{
				"label":"U.S. News",
				"url": "http://online.wsj.com/xml/rss/3_8068.xml"
			},
			{
				"label":"Politics and Campaign",
				"url": "http://online.wsj.com/xml/rss/3_7087.xml"
			},
			{
				"label":"Journal Reports",
				"url": "http://online.wsj.com/xml/rss/3_7435.xml"
			},
			{
				"label":"World News",
				"url": "http://online.wsj.com/xml/rss/3_7085.xml"
			},
			{
				"label":"Asia: What's News",
				"url": "http://online.wsj.com/xml/rss/3_7013.xml"
			},
			{
				"label":"Eurpoe: What's News",
				"url": "http://online.wsj.com/xml/rss/3_7012.xml"
			},
			{
				"label":"World Markets News",
				"url": "http://online.wsj.com/xml/rss/3_7432.xml"
			},
			{
				"label":"Home Asia News",
				"url": "http://online.wsj.com/xml/rss/3_7480.xml"
			},
			{
				"label":"China News",
				"url": "http://online.wsj.com/xml/rss/3_7441.xml"
			},
			{
				"label":"India News",
				"url": "http://online.wsj.com/xml/rss/3_8147.xml"
			},
			{
				"label":"India Journal",
				"url": "http://online.wsj.com/xml/rss/3_7656.xml"
			},
			{
				"label":"Managing in Asia",
				"url": "http://online.wsj.com/xml/rss/3_7448.xml"
			},
			{
				"label":"Weekend Asia",
				"url": "http://online.wsj.com/xml/rss/3_7444.xml"
			},
			{
				"label":"Home Europe News",
				"url": "http://online.wsj.com/xml/rss/3_7481.xml"
			},
			{
				"label":"U.K. News",
				"url": "http://online.wsj.com/xml/rss/3_7440.xml"
			},
			{
				"label":"Weekend Europe",
				"url": "http://online.wsj.com/xml/rss/3_7443.xml"
			},
			{
				"label":"Middle East News",
				"url": "http://online.wsj.com/xml/rss/3_7701.xml"
			},
			{
				"label":"Africa News",
				"url": "http://online.wsj.com/xml/rss/3_7736.xml"
			}
		]
}}

NYT = {"site": {
        "label": "New York Times",
        "url": "http://www.nytimes.com/",
        "feeds": [
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml",
                "label": "NYTimes.com Home Page (U.S.)"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml",
                "label": "NYTimes.com Home Page (Global Edition)"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/World.xml",
                "label": "World"
            },
            {
                "url": "http://atwar.blogs.nytimes.com/feed/",
                "label": "At War Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Africa.xml",
                "label": "Africa"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Americas.xml",
                "label": "Americas"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml",
                "label": "Asia Pacific"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Europe.xml",
                "label": "Europe"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
                "label": "Middle East"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/US.xml",
                "label": "U.S."
            },
            {
                "url": "http://bayarea.blogs.nytimes.com/feed",
                "label": "The Bay Area Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Education.xml",
                "label": "Education"
            },
            {
                "url": "http://thechoice.blogs.nytimes.com/feed",
                "label": "The Choice Blog"
            },
            {
                "url": "http://learning.blogs.nytimes.com/feed",
                "label": "The Learning Network Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Politics.xml",
                "label": "Politics"
            },
            {
                "url": "http://thecaucus.blogs.nytimes.com/feed/",
                "label": "The Caucus Blog"
            },
            {
                "url": "http://thelede.blogs.nytimes.com/feed/",
                "label": "The Lede Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml",
                "label": "N.Y./Region"
            },
            {
                "url": "http://cityroom.blogs.nytimes.com/feed/",
                "label": "City Room Blog"
            },
            {
                "url": "http://fort-greene.blogs.nytimes.com/feed",
                "label": "Fort Greene, NY Blog"
            },
            {
                "url": "http://maplewood.blogs.nytimes.com/feed",
                "label": "Maplewood, NJ Blog"
            },
            {
                "url": "http://feeds.nytimes.com/nyt/rss/Business",
                "label": "Business"
            },
            {
                "url": "http://executivesuite.blogs.nytimes.com/feed/",
                "label": "Executive Suite Blog"
            },
            {
                "url": "http://norris.blogs.nytimes.com/feed/",
                "label": "Floyd Norris: Notions on High and Low Finance Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml",
                "label": "Energy & Environment"
            },
            {
                "url": "http://greeninc.blogs.nytimes.com/feed/",
                "label": "Green Inc. Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/GlobalBusiness.xml",
                "label": "Global Business"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml",
                "label": "Small Business"
            },
            {
                "url": "http://boss.blogs.nytimes.com/feed",
                "label": "You're the Boss Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Economy.xml",
                "label": "Economy"
            },
            {
                "url": "http://economix.blogs.nytimes.com/feed/",
                "label": "Economix Blog"
            },
            {
                "url": "http://dealbook.blogs.nytimes.com/feed/",
                "label": "DealBook"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml",
                "label": "Media & Advertising"
            },
            {
                "url": "http://mediadecoder.blogs.nytimes.com/feed",
                "label": "Media Decoder Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/YourMoney.xml",
                "label": "Your Money"
            },
            {
                "url": "http://bucks.blogs.nytimes.com/feed",
                "label": "Bucks Blog"
            },
            {
                "url": "http://feeds.nytimes.com/nyt/rss/Technology",
                "label": "Technology"
            },
            {
                "url": "http://bits.blogs.nytimes.com/feed/",
                "label": "Bits Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/business-computing.xml",
                "label": "Business Computing"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/companies.xml",
                "label": "Companies"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/internet.xml",
                "label": "Internet"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/PersonalTech.xml",
                "label": "Personal Tech"
            },
            {
                "url": "http://gadgetwise.blogs.nytimes.com/feed/",
                "label": "Gadgetwise Blog"
            },
            {
                "url": "http://pogue.blogs.nytimes.com/feed/",
                "label": "Pogue's Posts Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/start-ups.xml",
                "label": "Start-Ups"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Sports.xml",
                "label": "Sports"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/GlobalSports.xml",
                "label": "Global Sports"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Baseball.xml",
                "label": "Baseball"
            },
            {
                "url": "http://bats.blogs.nytimes.com/feed/",
                "label": "Bats Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/CollegeBasketball.xml",
                "label": "College Basketball"
            },
            {
                "url": "http://thequad.blogs.nytimes.com/feed/",
                "label": "The Quad Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/CollegeFootball.xml",
                "label": "College Football"
            },
            {
                "url": "http://thequad.blogs.nytimes.com/feed/",
                "label": "The Quad Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Golf.xml",
                "label": "Golf"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Hockey.xml",
                "label": "Hockey"
            },
            {
                "url": "http://slapshot.blogs.nytimes.com/feed/",
                "label": "Slapshot Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/ProBasketball.xml",
                "label": "Pro-Basketball"
            },
            {
                "url": "http://offthedribble.blogs.nytimes.com/feed",
                "label": "Off the Dribble Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/ProFootball.xml",
                "label": "Pro-Football"
            },
            {
                "url": "http://fifthdown.blogs.nytimes.com/feed/",
                "label": "Fifth Down Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Soccer.xml",
                "label": "Soccer"
            },
            {
                "url": "http://goal.blogs.nytimes.com/feed/",
                "label": "Goal Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Tennis.xml",
                "label": "Tennis"
            },
            {
                "url": "http://straightsets.blogs.nytimes.com/feed",
                "label": "Straight Sets Blog"
            },
            {
                "url": "http://gambit.blogs.nytimes.com/feed/",
                "label": "Gambit Blog"
            },
            {
                "url": "http://formulaone.blogs.nytimes.com/feed/",
                "label": "Formula One Blog"
            },
            {
                "url": "http://therail.blogs.nytimes.com/feed",
                "label": "The Rail Blog"
            },
            {
                "url": "http://www.nytimes.com/pages/sports/olympics/index.html",
                "label": "Olympics"
            },
            {
                "url": "http://vancouver2010.blogs.nytimes.com/feed/",
                "label": "Rings Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Science.xml",
                "label": "Science"
            },
            {
                "url": "http://tierneylab.blogs.nytimes.com/feed",
                "label": "TierneyLab Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Environment.xml",
                "label": "Environment"
            },
            {
                "url": "http://greeninc.blogs.nytimes.com/feed/",
                "label": "Green Inc. Blog"
            },
            {
                "url": "http://dotearth.blogs.nytimes.com/feed/",
                "label": "Dot Earth Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Space.xml",
                "label": "Space & Cosmos"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Health.xml",
                "label": "Health"
            },
            {
                "url": "http://well.blogs.nytimes.com/feed/",
                "label": "Well Blog"
            },
            {
                "url": "http://newoldage.blogs.nytimes.com/feed/",
                "label": "The New Old Age Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Research.xml",
                "label": "Research"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Nutrition.xml",
                "label": "Fitness & Nutrition"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/HealthCarePolicy.xml",
                "label": "Money & Policy"
            },
            {
                "url": "http://prescriptions.blogs.nytimes.com/feed",
                "label": "Prescriptions Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Views.xml",
                "label": "Views"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Arts.xml",
                "label": "Arts"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/ArtandDesign.xml",
                "label": "Art & Design"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Books.xml",
                "label": "Books"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/SundayBookReview.xml",
                "label": "Sunday Book Review"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/BestSellers.xml",
                "label": "Best Sellers"
            },
            {
                "url": "http://papercuts.blogs.nytimes.com/feed/",
                "label": "Paper Cuts Blog"
            },
            {
                "url": "http://readingroom.blogs.nytimes.com/feed/",
                "label": "Reading Room Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Dance.xml",
                "label": "Dance"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Movies.xml",
                "label": "Movies"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Music.xml",
                "label": "Music"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml",
                "label": "Television"
            },
            {
                "url": "http://mediadecoder.blogs.nytimes.com/feed",
                "label": "Media Decoder Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Theater.xml",
                "label": "Theater"
            },
            {
                "url": "http://artsbeat.blogs.nytimes.com/feed",
                "label": "Artsbeat Blog"
            },
            {
                "url": "http://carpetbagger.blogs.nytimes.com/feed",
                "label": "Carpetbagger Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml",
                "label": "Fashion & Style"
            },
            {
                "url": "http://runway.blogs.nytimes.com/feed/",
                "label": "On the Runway Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/GlobalStyle.xml",
                "label": "Global Style"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/DiningandWine.xml",
                "label": "Dining & Wine"
            },
            {
                "url": "http://thepour.blogs.nytimes.com/feed",
                "label": "The Pour Blog"
            },
            {
                "url": "http://bitten.blogs.nytimes.com/feed",
                "label": "Bitten Blog"
            },
            {
                "url": "http://dinersjournal.blogs.nytimes.com/feed",
                "label": "Diners Journal Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/HomeandGarden.xml",
                "label": "Home & Garden"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Weddings.xml",
                "label": "Weddings/Celebrations"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/tmagazine.xml",
                "label": "T Magazine"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Travel.xml",
                "label": "Travel"
            },
            {
                "url": "http://globespotters.blogs.nytimes.com/feed/",
                "label": "Globespotters Blog"
            },
            {
                "url": "http://intransit.blogs.nytimes.com/feed",
                "label": "In Transit Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Escapes.xml",
                "label": "Escapes"
            },
            {
                "url": "http://frugaltraveler.blogs.nytimes.com/feed/",
                "label": "Frugral Traveler Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Magazine.xml",
                "label": "Magazine"
            },
            {
                "url": "http://ethicist.blogs.nytimes.com/feed/",
                "label": "The Ethicist Blog"
            },
            {
                "url": "http://parenting.blogs.nytimes.com/feed/",
                "label": "Motherlode Blog"
            },
            {
                "url": "http://themedium.blogs.nytimes.com/feed/",
                "label": "The Medium Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/JobMarket.xml",
                "label": "Jobs"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/RealEstate.xml",
                "label": "Real Estate"
            },
            {
                "url": "http://realestateqa.blogs.nytimes.com/feed/",
                "label": "Real Estate Q&A Blog"
            },
            {
                "url": "http://raisingtheroof.blogs.nytimes.com/feed/",
                "label": "Raising the Roof Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Commercial.xml",
                "label": "Commercial"
            },
            {
                "url": "http://wheels.blogs.nytimes.com/feed/",
                "label": "Wheels Blog"
            },
            {
                "url": "http://formulaone.blogs.nytimes.com/feed",
                "label": "Formula One Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/WeekinReview.xml",
                "label": "Week in Review"
            },
            {
                "url": "http://ideas.blogs.nytimes.com/feed/",
                "label": "Idea of the Day Blog"
            },
            {
                "url": "http://laughlines.blogs.nytimes.com/feed",
                "label": "Laughlines Blog"
            },
            {
                "url": "http://lens.blogs.nytimes.com/feed/",
                "label": "Lens Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Obituaries.xml",
                "label": "Obituaries"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/pop_top.xml",
                "label": "Most E-Mailed"
            },
            {
                "url": "http://nytimes.com/timeswire/feeds/",
                "label": "Times Wire"
            },
            {
                "url": "http://timestraveler.blogs.nytimes.com/feed",
                "label": "TimesTraveler Blog"
            },
            {
                "url": "http://topics.blogs.nytimes.com/feed",
                "label": "Topics Blog"
            },
            {
                "url": "http://wordplay.blogs.nytimes.com/feed",
                "label": "Wordplay Blog"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/Opinion.xml",
                "label": "Opinion"
            },
            {
                "url": "http://feeds2.feedburner.com/freakonomicsblog",
                "label": "Freakonomics Blog"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/feed/",
                "label": "The Opinionator Blog"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/allison-arieff/feed/",
                "label": "Allison Arieff"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/dick-cavett/feed/",
                "label": "Dick Cavett"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/william-d-cohan/feed/",
                "label": "William D. Cohan"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/timothy-egan/feed/",
                "label": "Timothy Egan"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/stanley-fish/feed/",
                "label": "Stanley Fish"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/doug-glanville/feed/",
                "label": "Doug Glanville"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/linda-greenhouse/feed/",
                "label": "Linda Greenhouse"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/olivia-judson/feed/",
                "label": "Olivia Judson"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/errol-morris/feed/",
                "label": "Errol Morris"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/steven-strogatz/feed/",
                "label": "Steven Strogatz"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/robert-wright/feed/",
                "label": "Robert Wright"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/the-conversation/feed/",
                "label": "The Conversation with David Brooks and Gail Collins"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/home-fires/feed/",
                "label": "Home Fires"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/the-score/feed/",
                "label": "The Score"
            },
            {
                "url": "http://opinionator.blogs.nytimes.com/category/the-thread/feed/",
                "label": "The Thread"
            },
            {
                "url": "http://schott.blogs.nytimes.com/feed/",
                "label": "Schott's Vocab Blog"
            },
            {
                "url": "http://roomfordebate.blogs.nytimes.com/feed",
                "label": "Room for Debate: A Running Commentary on the News"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/index.html?rss=1",
                "label": "Columnists"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/charles_m_blow/index.html?rss=1",
                "label": "Charles M. Blow"
            },
            {
                "url": "http://blow.blogs.nytimes.com/feed/",
                "label": "By the Numbers Blog"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/davidbrooks/index.html?rss=1",
                "label": "David Brooks"
            },
            {
                "url": "http://topics.nytimes.com/top/news/international/columns/rogercohen/index.html?rss=1",
                "label": "Roger Cohen"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/gailcollins/index.html?rss=1",
                "label": "Gail Collins"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/maureendowd/index.html?rss=1",
                "label": "Maureen Dowd"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/thomaslfriedman/index.html?rss=1",
                "label": "Thomas L. Friedman"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/bobherbert/index.html?rss=1",
                "label": "Bob Herbert"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/nicholasdkristof/index.html?rss=1",
                "label": "Nicholas D. Kristof"
            },
            {
                "url": "http://kristof.blogs.nytimes.com/feed/",
                "label": "On the Ground Blog"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/paulkrugman/index.html?rss=1",
                "label": "Paul Krugman"
            },
            {
                "url": "http://krugman.blogs.nytimes.com/feed/",
                "label": "The Conscience of a Liberal Blog"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/frankrich/index.html?rss=1",
                "label": "Frank Rich"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/columnists/rossdouthat/index.html?rss=1",
                "label": "Ross Douthat"
            },
            {
                "url": "http://douthat.blogs.nytimes.com/feed/",
                "label": "Evaluations Blog"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/oped/contributors/index.html?rss=1",
                "label": "Contributors"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/thepubliceditor/index.html?rss=1",
                "label": "The Public Editor"
            },
            {
                "url": "http://publiceditor.blogs.nytimes.com/feed/",
                "label": "The Public Editor's Journal"
            },
            {
                "url": "http://www.nytimes.com/services/xml/rss/nyt/GlobalOpinion.xml",
                "label": "Global Opinion"
            },
            {
                "url": "http://topics.nytimes.com/top/opinion/editorialsandoped/editorials/index.html?rss=1",
                "label": "Editorials"
            }
        ]
    }
}

SFC = {
    "site": {
        "label": "San Francisco Chronicle",
        "url": "http://www.sfgate.com/",
        "feeds": [
            {
                "label": "Page One News",
                "url": "http://www.sfgate.com/rss/feeds/news_pageone.xml"
            },
            {
                "label": "Top News Stories",
                "url": "http://www.sfgate.com/rss/feeds/news.xml"
            },
            {
                "label": "Bay Area News",
                "url": "http://www.sfgate.com/rss/feeds/bayarea.xml"
            },
            {
                "label": "Top Sports Stories",
                "url": "http://www.sfgate.com/rss/feeds/sports.xml"
            },
            {
                "label": "Business & Technology",
                "url": "http://www.sfgate.com/rss/feeds/business.xml"
            },
            {
                "label": "Entertainment",
                "url": "http://www.sfgate.com/rss/feeds/entertainment.xml"
            },
            {
                "label": "The Daily Dish!",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/dailydish/index_rss2.xml"
            },
            {
                "label": "Food & Dining",
                "url": "http://www.sfgate.com/rss/feeds/food.xml"
            },
            {
                "label": "Mark Morford - Notes & Errata",
                "url": "http://www.sfgate.com/rss/feeds/morford.xml"
            },
            {
                "label": "Jon Carroll",
                "url": "http://www.sfgate.com/rss/feeds/jcarroll.xml"
            },
            {
                "label": "Mark Fiore",
                "url": "http://www.sfgate.com/rss/feeds/mfiore.xml"
            },
            {
                "label": "San Francisco Giants",
                "url": "http://www.sfgate.com/rss/feeds/giants.xml"
            },
            {
                "label": "Oakland A's",
                "url": "http://www.sfgate.com/rss/feeds/athletics.xml"
            },
            {
                "label": "Page One News",
                "url": "http://www.sfgate.com/rss/feeds/news_pageone.xml"
            },
            {
                "label": "Top News Stories",
                "url": "http://www.sfgate.com/rss/feeds/news.xml"
            },
            {
                "label": "Bay Area News",
                "url": "http://www.sfgate.com/rss/feeds/bayarea.xml"
            },
            {
                "label": "City Insider Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/cityinsider/index_rss2.xml"
            },
            {
                "label": "Bronstein At Large",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/bronstein/index_rss2.xml"
            },
            {
                "label": "Education",
                "url": "http://www.sfgate.com/rss/feeds/education.xml"
            },
            {
                "label": "Weird News / The Bondage File",
                "url": "http://www.sfgate.com/rss/feeds/bondage.xml"
            },
            {
                "label": "Politics Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/nov05election/index_rss2.xml"
            },
            {
                "label": "ChronicleWatch",
                "url": "http://www.sfgate.com/rss/feeds/chroniclewatch.xml"
            },
            {
                "label": "Crime Scene",
                "url": "http://www.sfgate.com/rss/feeds/crime.xml"
            },
            {
                "label": "Chip Johnson",
                "url": "http://www.sfgate.com/rss/feeds/cjohnson.xml"
            },
            {
                "label": "Inside Iran Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/persianality/index_rss2.xml"
            },
            {
                "label": "Matier & Ross",
                "url": "http://www.sfgate.com/rss/feeds/matierandross.xml"
            },
            {
                "label": "Matier & Ross Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/matierandross/index_rss2.xml"
            },
            {
                "label": "C.W. Nevius",
                "url": "http://www.sfgate.com/rss/feeds/cnevius.xml"
            },
            {
                "label": "The Scavenger Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/scavenger/index_rss2.xml"
            },
            {
                "label": "World News",
                "url": "http://www.sfgate.com/rss/feeds/news_world.xml"
            },
            {
                "label": "National News",
                "url": "http://www.sfgate.com/rss/feeds/news_nation.xml"
            },
            {
                "label": "Politics",
                "url": "http://www.sfgate.com/rss/feeds/news_politics.xml"
            },
            {
                "label": "Dead By Mistake",
                "url": "http://feeds.feedburner.com/DeadByMistakeFull"
            },
            {
                "label": "Chronicle Op-Ed",
                "url": "http://www.sfgate.com/rss/feeds/opinion.xml"
            },
            {
                "label": "Mark Morford - Notes & Errata",
                "url": "http://www.sfgate.com/rss/feeds/morford.xml"
            },
            {
                "label": "Opinion Shop Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/opinionshop/index_rss2.xml"
            },
            {
                "label": "Debra J. Saunders",
                "url": "http://www.sfgate.com/rss/feeds/dsaunders.xml"
            },
            {
                "label": "Top Sports Stories",
                "url": "http://www.sfgate.com/rss/feeds/sports.xml"
            },
            {
                "label": "San Francisco Giants",
                "url": "http://www.sfgate.com/rss/feeds/giants.xml"
            },
            {
                "label": "Giants Splash Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/giants/index_rss2.xml"
            },
            {
                "label": "Oakland A's",
                "url": "http://www.sfgate.com/rss/feeds/athletics.xml"
            },
            {
                "label": "A's Drumbeat Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/athletics/index_rss2.xml"
            },
            {
                "label": "San Francisco 49ers",
                "url": "http://www.sfgate.com/rss/feeds/49ers.xml"
            },
            {
                "label": "Niner Insider Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/ninerinsider/index_rss2.xml"
            },
            {
                "label": "Oakland Raiders",
                "url": "http://www.sfgate.com/rss/feeds/raiders.xml"
            },
            {
                "label": "Raiders Silver & Black Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/raiders/index_rss2.xml"
            },
            {
                "label": "Golden State Warriors Blog",
                "url": "http://www.sfgate.com/rss/feeds/warriors.xml"
            },
            {
                "label": "Golden State Warriors",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/warriors/index_rss2.xml"
            },
            {
                "label": "San Jose Sharks",
                "url": "http://www.sfgate.com/rss/feeds/sharks.xml"
            },
            {
                "label": "High School Sports",
                "url": "http://www.sfgate.com/rss/feeds/preps.xml"
            },
            {
                "label": "Bruce Jenkins",
                "url": "http://www.sfgate.com/rss/feeds/bjenkins.xml"
            },
            {
                "label": "Bruce Jenkin's Three Dot Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/threedotblog/index_rss2.xml"
            },
            {
                "label": "Gwen Knapp",
                "url": "http://www.sfgate.com/rss/feeds/gknapp.xml"
            },
            {
                "label": "Scott Ostler",
                "url": "http://www.sfgate.com/rss/feeds/sostler.xml"
            },
            {
                "label": "Ray Ratto",
                "url": "http://www.sfgate.com/rss/feeds/rratto.xml"
            },
            {
                "label": "And The Horse You Rode In On",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/ratto/index_rss2.xml"
            },
            {
                "label": "John Shea",
                "url": "http://www.sfgate.com/rss/feeds/jshea.xml"
            },
            {
                "label": "Tom Stienstra - Outdoors",
                "url": "http://www.sfgate.com/rss/feeds/tstienstra.xml"
            },
            {
                "label": "Business & Technology",
                "url": "http://www.sfgate.com/rss/feeds/business.xml"
            },
            {
                "label": "Bay Area Biz Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/bayareabiz/index_rss2.xml"
            },
            {
                "label": "The Bottom Line",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/bottomline/index_rss2.xml"
            },
            {
                "label": "Cars",
                "url": "http://www.sfgate.com/rss/feeds/cars.xml"
            },
            {
                "label": "Dollars & Sense Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/dollarsandsense/index_rss2.xml"
            },
            {
                "label": "Get To Work - Employment Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/gettowork/index_rss2.xml"
            },
            {
                "label": "Technology",
                "url": "http://www.sfgate.com/rss/feeds/technology.xml"
            },
            {
                "label": "Tech Chronicles Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/techchron/index_rss2.xml"
            },
            {
                "label": "Tech Talk",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/cat_tech_talk_rss2.xml"
            },
            {
                "label": "On The Job",
                "url": "http://www.sfgate.com/rss/feeds/onthejob.xml"
            },
            {
                "label": "On The Record",
                "url": "http://www.sfgate.com/rss/feeds/ontherecord.xml"
            },
            {
                "label": "Real Estate",
                "url": "http://www.sfgate.com/rss/feeds/realestate.xml"
            },
            {
                "label": "On The Block - Real Estate Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/ontheblock/index_rss2.xml"
            },
            {
                "label": "Top Down Cars Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/topdown/index_rss2.xml"
            },
            {
                "label": "David Einstein - Computing Q & A",
                "url": "http://www.sfgate.com/rss/feeds/deinstein.xml"
            },
            {
                "label": "Kenneth Harney - Nation's Housing",
                "url": "http://www.sfgate.com/rss/feeds/harney.xml"
            },
            {
                "label": "Kathleen Pender - Net Worth",
                "url": "http://www.sfgate.com/rss/feeds/kpender.xml"
            },
            {
                "label": "Kathleen Pender - Net Worth Plus Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/pender/index_rss2.xml"
            },
            {
                "label": "Entertainment",
                "url": "http://www.sfgate.com/rss/feeds/entertainment.xml"
            },
            {
                "label": "The Daily Dish!",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/dailydish/index_rss2.xml"
            },
            {
                "label": "11 Things",
                "url": "http://www.sfgate.com/rss/feeds/11things.xml"
            },
            {
                "label": "Asian Pop",
                "url": "http://www.sfgate.com/rss/feeds/asianpop.xml"
            },
            {
                "label": "Art",
                "url": "http://www.sfgate.com/rss/feeds/art.xml"
            },
            {
                "label": "Books",
                "url": "http://www.sfgate.com/rss/feeds/books.xml"
            },
            {
                "label": "Classical Music",
                "url": "http://www.sfgate.com/rss/feeds/classical.xml"
            },
            {
                "label": "Culture Blog!",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/culture/index_rss2.xml"
            },
            {
                "label": "Movie Reviews",
                "url": "http://www.sfgate.com/rss/feeds/moviereviews.xml"
            },
            {
                "label": "Mick LaSalle - Movies",
                "url": "http://www.sfgate.com/rss/feeds/mlasalle.xml"
            },
            {
                "label": "Mick LaSalle - Movies Podcast",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/cat_movies_with_mick_lasalle_rss2.xml"
            },
            {
                "label": "Mick LaSalle Blog - Maximum Strength Mick",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/mlasalle/index_rss2.xml"
            },
            {
                "label": "Off The Record - Local Bands",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/offtherecord/index_rss2.xml"
            },
            {
                "label": "Kenneth Baker - Art",
                "url": "http://www.sfgate.com/rss/feeds/kbaker.xml"
            },
            {
                "label": "Jon Carroll",
                "url": "http://www.sfgate.com/rss/feeds/jcarroll.xml"
            },
            {
                "label": "Leah Garchik",
                "url": "http://www.sfgate.com/rss/feeds/lgarchik.xml"
            },
            {
                "label": "Tim Goodman - Television",
                "url": "http://www.sfgate.com/rss/feeds/tgoodman.xml"
            },
            {
                "label": "Tim Goodman Blog - The Bastard Machine",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/tgoodman/index_rss2.xml"
            },
            {
                "label": "Peter Hartlaub - Playing Games",
                "url": "http://www.sfgate.com/rss/feeds/phartlaub.xml"
            },
            {
                "label": "John King - Urban Design",
                "url": "http://www.sfgate.com/rss/feeds/jking.xml"
            },
            {
                "label": "Tim Goodman's TV Talk Machine",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/cat_tim_goodmans_tv_talk_machine_rss2.xml"
            },
            {
                "label": "Gaming",
                "url": "http://www.sfgate.com/rss/feeds/gaming.xml"
            },
            {
                "label": "Food & Dining",
                "url": "http://www.sfgate.com/rss/feeds/food.xml"
            },
            {
                "label": "Wine",
                "url": "http://www.sfgate.com/rss/feeds/wine.xml"
            },
            {
                "label": "The Cellarist",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/wine/index_rss2.xml"
            },
            {
                "label": "Michael Bauer - Between Meals",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/mbauer/index_rss2.xml"
            },
            {
                "label": "Janet Fletcher - The Cheese Course",
                "url": "http://www.sfgate.com/rss/feeds/jfletcher.xml"
            },
            {
                "label": "Inside Scoop restaurant news",
                "url": "http://www.sfgate.com/rss/feeds/insidescoop.xml"
            },
            {
                "label": "The Working Cook",
                "url": "http://www.sfgate.com/rss/feeds/theworkingcook.xml"
            },
            {
                "label": "Bargain Bites",
                "url": "http://www.sfgate.com/rss/feeds/bargainbites.xml"
            },
            {
                "label": "Bar Bites",
                "url": "http://www.sfgate.com/rss/feeds/barbites.xml"
            },
            {
                "label": "Tasters Choice",
                "url": "http://www.sfgate.com/rss/feeds/tasterschoice.xml"
            },
            {
                "label": "Food Matters",
                "url": "http://www.sfgate.com/rss/feeds/foodmatters.xml"
            },
            {
                "label": "The Accidental Vegetarian",
                "url": "http://www.sfgate.com/rss/feeds/theaccidentalvegetarian.xml"
            },
            {
                "label": "Chronicle Wine Selections",
                "url": "http://www.sfgate.com/rss/feeds/wineselections.xml"
            },
            {
                "label": "The Cocktailian",
                "url": "http://www.sfgate.com/rss/feeds/cocktailian.xml"
            },
            {
                "label": "Pairings",
                "url": "http://www.sfgate.com/rss/feeds/pairings.xml"
            },
            {
                "label": "The Tasting Room",
                "url": "http://www.sfgate.com/rss/feeds/tastingroom.xml"
            },
            {
                "label": "Dining Out - Restaurant Reviews",
                "url": "http://www.sfgate.com/rss/feeds/diningout.xml"
            },
            {
                "label": "Ask The Bugman",
                "url": "http://www.sfgate.com/rss/feeds/askthebugman.xml"
            },
            {
                "label": "Benefits",
                "url": "http://www.sfgate.com/rss/feeds/benefits.xml"
            },
            {
                "label": "Violet Blue",
                "url": "http://www.sfgate.com/rss/feeds/vblue.xml"
            },
            {
                "label": "The City Exposed",
                "url": "http://www.sfgate.com/rss/feeds/cityexposed.xml"
            },
            {
                "label": "Day In Pictures",
                "url": "http://www.sfgate.com/rss/feeds/dayinpictures.xml"
            },
            {
                "label": "The Dirt",
                "url": "http://www.sfgate.com/rss/feeds/thedirt.xml"
            },
            {
                "label": "The Fishing Report",
                "url": "http://www.sfgate.com/rss/feeds/fishingreport.xml"
            },
            {
                "label": "Gay & Lesbian",
                "url": "http://www.sfgate.com/rss/feeds/gay.xml"
            },
            {
                "label": "The Thin Green Line",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/green/index_rss2.xml"
            },
            {
                "label": "Home & Garden",
                "url": "http://www.sfgate.com/rss/feeds/homeandgarden.xml"
            },
            {
                "label": "Hot Stuff",
                "url": "http://www.sfgate.com/rss/feeds/hotstuff.xml"
            },
            {
                "label": "David Miller - Finding My Religion",
                "url": "http://www.sfgate.com/rss/feeds/dmiller.xml"
            },
            {
                "label": "The Mommy Files Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/sfmoms/index_rss2.xml"
            },
            {
                "label": "On The Couch",
                "url": "http://www.sfgate.com/rss/feeds/onthecouch.xml"
            },
            {
                "label": "On The Town",
                "url": "http://www.sfgate.com/rss/feeds/onthetown.xml"
            },
            {
                "label": "Parties",
                "url": "http://www.sfgate.com/rss/feeds/parties.xml"
            },
            {
                "label": "Pick of the Week",
                "url": "http://www.sfgate.com/rss/feeds/pickoftheweek.xml"
            },
            {
                "label": "The Poop Parenting Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/parenting/index_rss2.xml"
            },
            {
                "label": "SF Unzipped",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chronstyle/index_rss2.xml"
            },
            {
                "label": "Bill and Kevin Burnett - Sweat Equity",
                "url": "http://www.sfgate.com/rss/feeds/bburnett.xml"
            },
            {
                "label": "Tails Of The City",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/pets/index_rss2.xml"
            },
            {
                "label": "The Wallflower - Home & Design Blog",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/wallflower/index_rss2.xml"
            },
            {
                "label": "Sam Whiting",
                "url": "http://www.sfgate.com/rss/feeds/swhiting.xml"
            },
            {
                "label": "Your Whole Pet",
                "url": "http://www.sfgate.com/rss/feeds/yourwholepet.xml"
            },
            {
                "label": "Travel News and Features",
                "url": "http://www.sfgate.com/rss/feeds/travel.xml"
            },
            {
                "label": "Aloha Friday",
                "url": "http://www.sfgate.com/rss/feeds/alohafriday.xml"
            },
            {
                "label": "Budget Travel",
                "url": "http://www.sfgate.com/rss/feeds/budgettravel.xml"
            },
            {
                "label": "Cruise Briefing",
                "url": "http://www.sfgate.com/rss/feeds/cruisebriefing.xml"
            },
            {
                "label": "Departures",
                "url": "http://www.sfgate.com/rss/feeds/departures.xml"
            },
            {
                "label": "Hawaii Insider",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/hawaii/index_rss2.xml"
            },
            {
                "label": "In Gear",
                "url": "http://www.sfgate.com/rss/feeds/ingear.xml"
            },
            {
                "label": "John Flinn",
                "url": "http://www.sfgate.com/rss/feeds/johnflinn.xml"
            },
            {
                "label": "Just Back From",
                "url": "http://www.sfgate.com/rss/feeds/justbackfrom.xml"
            },
            {
                "label": "Mexico Mix",
                "url": "http://www.sfgate.com/rss/feeds/mexicomix.xml"
            },
            {
                "label": "On Travel",
                "url": "http://www.sfgate.com/rss/feeds/ontravel.xml"
            },
            {
                "label": "Street Date",
                "url": "http://www.sfgate.com/rss/feeds/streetdate.xml"
            },
            {
                "label": "Travelers' Checks",
                "url": "http://www.sfgate.com/rss/feeds/travelerschecks.xml"
            },
            {
                "label": "Travel Troubleshooter",
                "url": "http://www.sfgate.com/rss/feeds/traveltroubleshooter.xml"
            },
            {
                "label": "Urban Outings",
                "url": "http://www.sfgate.com/rss/feeds/urbanoutings.xml"
            },
            {
                "label": "Don Asmussen - Bad Reporter",
                "url": "http://www.sfgate.com/rss/feeds/dasmussen.xml"
            },
            {
                "label": "Mark Fiore",
                "url": "http://www.sfgate.com/rss/feeds/mfiore.xml"
            },
            {
                "label": "Meyer's Take",
                "url": "http://www.sfgate.com/rss/feeds/tmeyer.xml"
            },
            {
                "label": "Paul Madonna - All Over Coffee",
                "url": "http://www.sfgate.com/rss/feeds/pmadonna.xml"
            },
            {
                "label": "All Podcasts",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/index_rss2.xml"
            },
            {
                "label": "Chronicle Radio",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/cat_chronicle_radio_rss2.xml"
            },
            {
                "label": "Mick LaSalle - Movies Podcast",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/cat_movies_with_mick_lasalle_rss2.xml" 
            },
            {
                "label": "Tech Talk",
                "url": "http://www.sfgate.com/rss/feeds/blogs/sfgate/chroncast/cat_tech_talk_rss2.xml"
            }
        ] 
    }
}

WP = {
    "site": {
        "label": "Washington Post",
        "url": "http://www.washingtonpost.com/",
        "feeds": [
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400102.xml",
                "label": "Top News" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/print/index.xml",
                "label": "Today's Washington Post - Front Page" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/sitemap/linkset/2009/03/30/LI2009033001401-mrss.xml",
                "label": "Top Video" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/politics/fedpage/index.xml",
                "label": "Federal Page" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/44/index",
                "label": "44: The Obama Presidency" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/ezra-klein/index",
                "label": "Ezra Klein" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/politics/elections/index.xml",
                "label": "Elections" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/politics/congress/index.xml",
                "label": "Congress" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/politics/administration/index.xml",
                "label": "Bush Administration" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400643.xml",
                "label": "Stephen Barr - Federal Page" 
            },
            {
                "url": "http://blog.washingtonpost.com/thefix/index.xml",
                "label": "Chris Cillizza - The Fix" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402404.xml",
                "label": "Al Kamen - In the Loop" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032501825.xml",
                "label": "Dana Milbank - Washington Sketch" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402430.xml",
                "label": "Judy Sarasohn - Special Interests" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/nation/index.xml",
                "label": "Nation" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/nation/nationalsecurity/index.xml",
                "label": "National Security" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/securityfix/index",
                "label": "Security Fix" 
            },
            {
                "url": "http://voices.washingtonpost.com/washingtonpostinvestigations/index.xml",
                "label": "Investigations" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400143.xml",
                "label": "Intelligence" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2007/07/20/LI2007072001213.xml",
                "label": "Military" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/nation/science/index.xml",
                "label": "Science" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401272.xml",
                "label": "Howard Kurtz - Media Notes" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/index.xml",
                "label": "World" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/mideast/index.xml",
                "label": "Middle East" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/asia/index.xml",
                "label": "Asia/Pacific" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/europe/index.xml",
                "label": "Europe" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2007/07/05/LI2007070500831.xml",
                "label": "Iraq" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/africa/index.xml",
                "label": "Africa" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/southamerica/index.xml",
                "label": "South America" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/centralamerica/index.xml",
                "label": "Central America" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/world/northamerica/index.xml",
                "label": "North America" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401639.xml",
                "label": "David Ignatius" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401628.xml",
                "label": "Jim Hoagland" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401674.xml",
                "label": "Robert Kagan" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/index.xml",
                "label": "Metro" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/education/index.xml",
                "label": "Schools" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/crime/index.xml",
                "label": "Crime" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/capitalweathergang/index",
                "label": "Capital Weather Gang" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/lottery/index.xml",
                "label": "Lottery" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/obituaries/index.xml",
                "label": "Obituaries" 
            },
            {
                "url": "http://newsweek.washingtonpost.com/onfaith/atom.xml",
                "label": "Religion: On Faith" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/dc/index.xml",
                "label": "The District" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/md/index.xml",
                "label": "Maryland" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/metro/va/index.xml",
                "label": "Virginia" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/print/style/index.xml",
                "label": "Style" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/09/26/LI2005092600765.xml",
                "label": "Amy Argetsinger and Roxanne Roberts - The Reliable Source" 
            },
            {
                "url": "http://voices.washingtonpost.com/comic-riffs/index.xml",
                "label": "Michael Cavna - Comic Riffs" 
            },
            {
                "url": "http://voices.washingtonpost.com/postrock/index.xml",
                "label": "J. Freedom du Lac and David Malitz - Post Rock" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402809.xml",
                "label": "Carolyn Hax - Tell Me About It" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032501837.xml",
                "label": "Miss Manners" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032502344.xml",
                "label": "Names and Faces" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/index.xml",
                "label": "Business" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400543.xml",
                "label": "Keith L. Alexander: Business Class" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400122.xml",
                "label": "Warren Brown: On Wheels" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/government/index.xml",
                "label": "Business Policy" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/economy/index.xml",
                "label": "Economy" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/04/18/LI2005041800997.xml",
                "label": "Financial Industry News" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/28/LI2005032800718.xml",
                "label": "Investing" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400526.xml",
                "label": "Roger K. Lewis: Shaping the City" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/localbusiness/index.xml",
                "label": "Metro Business" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/special/3/index.xml",
                "label": "Oil and Gas Prices" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400138.xml",
                "label": "Steven Pearlstein" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/special/5/index.xml",
                "label": "Pentagon Procurement News" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/business/personalfinance/index.xml",
                "label": "Personal Finance" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400142.xml",
                "label": "Michelle Singletary: Color of Money" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2006/04/19/LI2006041901286.xml",
                "label": "Lily Garcia: How to Deal" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/04/29/LI2005042900378.xml",
                "label": "Kenneth Bredemeier: On the Job" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400329.xml",
                "label": "Allan Sloan: Deals" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/28/LI2005032800573.xml",
                "label": "Week in Stocks" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/technology/index.xml",
                "label": "Technology" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/technology/washtech/index.xml",
                "label": "WashTech - D.C. Technology News" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/technology/techpolicy/index.xml",
                "label": "Tech Policy" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032502645.xml",
                "label": "HELP File" 
            },
            {
                "url": "http://blog.washingtonpost.com/securityfix/index.xml",
                "label": "Brian Krebs - Security Fix" 
            },
            {
                "url": "http://projects.washingtonpost.com/staff/rss/articles/ellen+mccarthy/",
                "label": "Ellen McCarthy: The Download" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402859.xml",
                "label": "Rob Pegoraro - Fast Forward" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/technology/personaltech/index.xml",
                "label": "Personal Tech" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/health/index.xml",
                "label": "Health" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2008/10/14/LI2008101401092.xml",
                "label": "Eat, Drink and Be Healthy" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2007/05/02/LI2007050201281.xml",
                "label": "The Misfits" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032500698.xml",
                "label": "Quick Study" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/education/index.xml",
                "label": "Education" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/class-struggle/index",
                "label": "Jay Mathews - Class Struggle" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/realestate/index.xml",
                "label": "Real Estate" 
            },
            {
                "url": "http://feeds.pheedo.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400113_xml",
                "label": "Scott Aker - Digging In" 
            },
            {
                "url": "http://feeds.pheedo.com/wp-dyn/rss/linkset/2005/03/25/LI2005032500644_xml",
                "label": "Barbara Damrosch - A Cook's Garden" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400436.xml",
                "label": "Kenneth R. Harney: The Nation's Housing" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400517.xml",
                "label": "Benny L. Kass: Housing Counsel" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032500646.xml",
                "label": "Joel Lerner - Green Scene" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/05/30/LI2005053000331.xml",
                "label": "Editorials" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402329.xml",
                "label": "Op-Eds" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402345.xml",
                "label": "Letters to the Editor" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/print/outlook/index.xml",
                "label": "Sunday Outlook" 
            },
            {
                "url": "http://blog.washingtonpost.com/achenblog/index.xml",
                "label": "Joel Achenbach's Achenblog" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401432.xml",
                "label": "Anne Applebaum" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401502.xml",
                "label": "David S. Broder" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401528.xml",
                "label": "Richard Cohen" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401551.xml",
                "label": "Jackson Diehl" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/04/22/LI2005042201099.xml",
                "label": "E.J. Dionne Jr." 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2007/05/30/LI2007053001159.xml",
                "label": "Michael Gerson" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401615.xml",
                "label": "Fred Hiatt" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401628.xml",
                "label": "Jim Hoagland" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401639.xml",
                "label": "David Ignatius" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401674.xml",
                "label": "Robert Kagan" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402404.xml",
                "label": "Al Kamen - In the Loop" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401680.xml",
                "label": "Colbert I. King" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401687.xml",
                "label": "Michael Kinsley" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401690.xml",
                "label": "Charles Krauthammer" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/local-opinions/index",
                "label": "Local Opinions" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401702.xml",
                "label": "Sebastian Mallaby" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2006/05/04/LI2006050400962.xml",
                "label": "Ruth Marcus" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032500977.xml",
                "label": "Harold Meyerson" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032501825.xml",
                "label": "Dana Milbank" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032401706.xml",
                "label": "Courtland Milloy" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032500838.xml",
                "label": "Ombudsman" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2008/10/20/LI2008102001816.xml",
                "label": "Kathleen Parker" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400138.xml",
                "label": "Steven Pearlstein" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/postpartisan/index",
                "label": "PostPartisan" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402899.xml",
                "label": "Eugene Robinson" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402276.xml",
                "label": "Robert Samuelson" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402294.xml",
                "label": "George F. Will" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/index.xml",
                "label": "Sports" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/dcsportsbog/index",
                "label": "D.C. Sports Bog" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/index/nfl/index.xml",
                "label": "NFL" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/redskins/index.xml",
                "label": "Redskins" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/ravens/index.xml",
                "label": "Ravens" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/index/nba/index.xml",
                "label": "NBA" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/wizards/index.xml",
                "label": "Wizards" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/index/mlb/index.xml",
                "label": "MLB" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/orioles/index.xml",
                "label": "Orioles" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/nationals/index.xml",
                "label": "Nationals" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/dcunited/index.xml",
                "label": "DC United" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/index/nhl/index.xml",
                "label": "NHL" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/capitals/index.xml",
                "label": "Capitals" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/mystics/index.xml",
                "label": "Mystics" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/colleges/football/index.xml",
                "label": "College Football" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/sports/highschools/index.xml",
                "label": "DC Area High School Sports" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032400073.xml",
                "label": "Michael Wilbon" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402520.xml",
                "label": "Thomas Boswell" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402723.xml",
                "label": "Mike Wise" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/04/20/LI2005042001235.xml",
                "label": "Les Carpenter's MLB Insider" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/print/style/index.xml",
                "label": "Style" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/reliable-source/index",
                "label": "Amy Argetsinger and Roxanne Roberts - The Reliable Source" 
            },
            {
                "url": "http://feeds.voices.washingtonpost.com/wp/shortstack/index",
                "label": "Books" 
            },
            {
                "url": "http://voices.washingtonpost.com/celebritology/index.xml",
                "label": "Celebritology" 
            },
            {
                "url": "http://voices.washingtonpost.com/goingoutgurus/index.xml",
                "label": "Going Out Gurus" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/24/LI2005032402809.xml",
                "label": "Carolyn Hax - Tell Me About It" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-srv/artsandliving/horoscopes/rss.xml",
                "label": "Horoscopes" 
            },
            {
                "url": "http://projects.washingtonpost.com/staff/rss/aggregate/tom+sietsema/",
                "label": "Tom Sietsema - Dining" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/print/washpostmagazine/index.xml",
                "label": "Washington Post Magazine" 
            },
            {
                "url": "http://www.washingtonpost.com/wp-dyn/rss/linkset/2005/03/25/LI2005032501927.xml",
                "label": "Gene Weingarten: Below the Beltway" 
            } 
        ] 
    }
}

import models


class LoadSiteFeeds(webapp.RequestHandler):
	def get(self, sitecode):
		if sitecode == "wsj":
			feedset = WSJ
		elif sitecode == "nyt":
			feedset = NYT
		elif sitecode == "sfc":
			feedset = SFC
		elif sitecode == "wp":
			feedset = WP
		self.response.out.write(feedset['site']['label'] + "<br />")
		self.response.out.write(feedset['site']['url'] + "<br /><br />")
		site = models.Site.get_or_insert(sitecode, code=sitecode, url=feedset['site']['url'], label=feedset['site']['label'])
		for feed in feedset['site']['feeds']:
			self.response.out.write(feed['label'] + "<br />")
			self.response.out.write(feed['url'] + "<br /><hr />")
			models.Feed.get_or_insert(feed['url'], site=site, url=feed['url'], label=feed['label'])
			