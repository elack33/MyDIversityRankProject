INSERT INTO MyDiRa_demographics (DemoGraphic)
VALUES ('White'), ('Hispanic or Latino'), ('Black or African American'),
('Native American or American Indian'), ('Asian / Pacific Islander'), ('Some combination of options'), ('Other');
 

INSERT INTO MyDiRa_yearofbirth (year)
VALUES ('1899'), ('1900'), ('1901'), ('1902'), ('1903'), ('1904'), ('1905'), ('1906'), 
	('1907'), ('1908'), ('1909'), ('1910'), ('1911'), ('1912'), ('1913'), ('1914'), 
	('1915'), ('1916'), ('1917'), ('1918'), ('1919'), ('1920'), ('1921'), ('1922'), 
	('1923'), ('1924'), ('1925'), ('1926'), ('1927'), ('1928'), ('1929'), ('1930'), 
	('1931'), ('1932'), ('1933'), ('1934'), ('1935'), ('1936'), ('1937'), ('1938'), 
	('1939'), ('1940'), ('1941'), ('1942'), ('1943'), ('1944'), ('1945'), ('1946'), 
	('1947'), ('1948'), ('1949'), ('1950'), ('1951'), ('1952'), ('1953'), ('1954'), 
	('1955'), ('1956'), ('1957'), ('1958'), ('1959'), ('1960'), ('1961'), ('1962'), 
	('1963'), ('1964'), ('1965'), ('1966'), ('1967'), ('1968'), ('1969'), ('1970'), 
	('1971'), ('1972'), ('1973'), ('1974'), ('1975'), ('1976'), ('1977'), ('1978'), 
	('1979'), ('1980'), ('1981'), ('1982'), ('1983'), ('1984'), ('1985'), ('1986'), 
	('1987'), ('1988'), ('1989'), ('1990'), ('1991'), ('1992'), ('1993'), ('1994'), 
	('1995'), ('1996'), ('1997'), ('1998'), ('1999'), ('2000'), ('2001'), ('2002'), 
	('2003'), ('2004'), ('2005'), ('2006'), ('2007'), ('2008'), ('2009'), ('2010'), 
	('2011'), ('2012'), ('2013'), ('2014'), ('2015'); 

INSERT INTO MyDiRa_genders (gender)
VALUES ('Female'), ('Male'), ('Non-binary'), ('Genderfluid'), ('Other');
  

INSERT INTO MyDiRa_interests (interest)
VALUES ('Reading'), ('Technology'), ('Gardening'), ('Health'), ('Travel'), ('Food'), ('Automotive'), 
('Fashion'), ('Home Living'), ('Exercise/Fitness'), ('Collecting'), ('Crafts'), ('Radio'), 
('Outdoors'), ('Visual Arts'), ('Genealogy'),  ('Parenting'), ('Tabletop Gaming'), 
('Video Games'), ('Dancing'), ('Square Dancing'), ('Geekdom'), ('Music'), ('Learning'), 
('Movies'), ('TV'), ('Other');

INSERT INTO MyDiRa_orientations (orientation)
VALUES ('Gay'), ('Lesbian'), ('Straight'), ('Bi'), ('Other');

INSERT INTO MyDiRa_careers (career)
VALUES ('Accounting'), ('General Business'), ('Software Development')
, ('Admin & Clerical'), ('General Labor'), ('Pharmaceutical')
, ('Automotive'), ('Government'), ('Professional Services')
, ('Banking'), ('Grocery'), ('Purchasing-Procurement')
, ('Biotech'), ('Health Care'), ('QA-Quality Control')
, ('Journalism'), ('Hotel-Hospitality'), ('Real Estate')
, ('Business Development'), ('Human Resources'), ('Research')
, ('Construction'), ('Information Technology'), ('Restaurant-Food Service')
, ('Consultant'), ('Installation-Repair'), ('Retail')
, ('Customer Service'), ('Insurance'), ('Sales')
, ('Design'), ('Inventory'), ('Science')
, ('Distribution-Shipping'), ('Legal'), ('Skilled Labor-Trades')
, ('Education-Teaching'), ('Legal Admin'), ('Strategy Planning')
, ('Engineering'), ('Management'), ('Supply Chain')
, ('Entry Level'), ('Manufacturing'), ('Telecommunications')
, ('Executive'), ('Marketing'), ('Training')
, ('Facilities'), ('Media'), ('Newspaper'), ('Transportation')
, ('Finance'), ('Nonprofit'), ('Social Services'), ('Warehouse')
, ('Other');

INSERT INTO MyDiRa_questions (question)
VALUES ('What does diversity mean to you?'), ('What does it mean to be fearless to you?'),
	('What does break down barriers mean to you?'), ('What does build communities mean to you?');

INSERT INTO MyDiRa_relationship (status)
VALUES ('Single'), ('Living with Partner or Spouse'), ('Dating'), ('Married'), 
('Divorced'), ('Separated'), ('Nah'), ('Other');

INSERT INTO MyDiRa_ogamy (title)
VALUES ('Monogamy'), ('Open'), ('Swinging'), ('Monogamish'), ('Polyamory'), ('Other');

INSERT INTO MyDiRa_surveyresponses (author_id, career01_id, career02_id, demographic_id, gender_id,
	orientation_id, relationship_id, year_of_birth_id, 
    interest01_id, interest02_id, interest03_id, interest04_id, interest05_id, 
    interest06_id, interest07_id, interest08_id, interest09_id, interest10_id)
VALUES 
	(2, 57, 56, 7, 5, 5, 8, 99, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18),
    (2, 34, 43, 3, 1, 1, 5, 56, 23, 11, 12, 13, 14, 15, 16, 17, 18, 19),
	(2, 11, 13, 2, 2, 4, 8, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)





















