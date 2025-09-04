import os

from rdflib import Graph, Literal, RDF, URIRef, BNode
from rdflib.namespace import RDF, RDFS, OWL, XSD, SDO
from rdflib.namespace import Namespace
import pandas as pd


# Read the CSV file
df = pd.read_csv("Nobel_Prize.csv")

# Replace missing values with empty strings
df = df.fillna("")

# Create an RDF graph
g = Graph()

# Define the namespace
myOnto = Namespace("http://www.mysemantics.com/ontology/")
mySemantics = Namespace("http://www.mysemantics.com/resource/")
dbr = Namespace("http://dbpedia.org/resource/")
dbo = Namespace("http://dbpedia.org/ontology/")

# Bind prefixes
g.bind("myOnto", myOnto)
g.bind("rdf", RDF)
g.bind("mySemantics", mySemantics) # Adding prefix mysemantics
g.bind("dbr", dbr)
g.bind("dbo", dbo)
g.bind("", mySemantics) # Adding default prefix

# Add ontology declaration statements
OntologyIRI = URIRef(myOnto)
g.add((OntologyIRI, RDF.type, OWL.Ontology))
g.add((OntologyIRI, RDFS.comment, Literal("An ontology for Semantic Web course final project"))) 

# Declaration of external classes & properties
g.add((SDO.Person, RDF.type, OWL.Class))
g.add((SDO.Organization, RDF.type, OWL.Class))
g.add((SDO.GenderType, RDF.type, OWL.Class))
g.add((dbo.NobelPrize, RDF.type, OWL.Class))
g.add((dbo.Country, RDF.type, OWL.Class))

g.add((SDO.birthPlace, RDF.type, OWL.ObjectProperty))
g.add((SDO.givenName, RDF.type, OWL.DatatypeProperty))
g.add((SDO.familyName, RDF.type, OWL.DatatypeProperty))
g.add((SDO.gender, RDF.type, OWL.DatatypeProperty))
g.add((SDO.birthDate, RDF.type, OWL.DatatypeProperty))
g.add((SDO.name, RDF.type, OWL.DatatypeProperty))


######## Define class below ########

## Class Person

Person = myOnto.Person  # IRI for class myOnto:Person 

g.add((Person, RDF.type, OWL.Class))
g.add((Person, RDFS.subClassOf, SDO.Person))

_resBirthCountry = BNode()
g.add((Person, RDFS.subClassOf, _resBirthCountry))
g.add((_resBirthCountry, RDF.type, OWL.Restriction))
g.add((_resBirthCountry, OWL.onProperty, myOnto.birthCountry))
g.add((_resBirthCountry, OWL.qualifiedCardinality, Literal("1", datatype=XSD.nonNegativeInteger)))
g.add((_resBirthCountry, OWL.onClass, dbo.Country))

_resLaureateID = BNode()
g.add((Person, RDFS.subClassOf, _resLaureateID))
g.add((_resLaureateID, RDF.type, OWL.Restriction))
g.add((_resLaureateID, OWL.onProperty, myOnto.laureateID))
g.add((_resLaureateID, OWL.cardinality, Literal("1", datatype=XSD.nonNegativeInteger)))

_resPrizeShare = BNode()
g.add((Person, RDFS.subClassOf, _resPrizeShare))
g.add((_resPrizeShare, RDF.type, OWL.Restriction))
g.add((_resPrizeShare, OWL.onProperty, myOnto.prizeShare))
g.add((_resPrizeShare, OWL.minCardinality, Literal("1", datatype=XSD.nonNegativeInteger)))
g.add((_resPrizeShare, OWL.maxCardinality, Literal("3", datatype=XSD.nonNegativeInteger)))

_resBirthDate = BNode()
g.add((Person, RDFS.subClassOf, _resBirthDate))
g.add((_resBirthDate, RDF.type, OWL.Restriction))
g.add((_resBirthDate, OWL.onProperty, myOnto.birthDate))
g.add((_resBirthDate, OWL.cardinality, Literal("1", datatype=XSD.nonNegativeInteger)))

_resOrganizationName = BNode()
g.add((Person, RDFS.subClassOf,_resOrganizationName))
g.add((_resOrganizationName, RDF.type, OWL.Restriction))
g.add((_resOrganizationName, OWL.onProperty, myOnto.organizationName))
g.add((_resOrganizationName, OWL.maxCardinality, Literal("1", datatype=XSD.nonNegativeInteger)))

g.add((Person, RDFS.label, Literal("Person", lang="en")))
g.add((Person, RDFS.comment, Literal("A class defining a Person.", lang="en")))

## Class NobelPrize

NobelPrize = myOnto.NobelPrize  # IRI for class myOnto:NobelPrize

g.add((NobelPrize, RDF.type, RDFS.Class))
g.add((NobelPrize, RDFS.subClassOf, dbo.NobelPrize))

_reshasPrizeName = BNode()
g.add((Person, RDFS.subClassOf, _reshasPrizeName))
g.add((_reshasPrizeName, RDF.type, OWL.Restriction))
g.add((_reshasPrizeName, OWL.onProperty, myOnto.hasPrizeName))
g.add((_reshasPrizeName, OWL.minCardinality, Literal("1", datatype=XSD.nonNegativeInteger)))

g.add((NobelPrize, RDFS.label, Literal("Nobel Prize", lang="en")))
g.add((NobelPrize, RDFS.comment, Literal("A class defining a Nobel Prize.", lang="en")))


######## Define properties below ########

## Define Object Properties

prize_category = myOnto.prizeCategory
g.add((prize_category, RDF.type, OWL.ObjectProperty))
g.add((prize_category, RDF.type, OWL.FunctionalProperty))
g.add((prize_category, RDFS.domain, Person))
g.add((prize_category, RDFS.range, NobelPrize))
g.add((prize_category, RDFS.label, Literal("Nobel Prize Category", lang="en")))
g.add((prize_category, RDFS.comment, Literal("The Nobel Prize category of a person.",lang="en")))

birth_country = myOnto.birthCountry
g.add((birth_country, RDF.type, OWL.ObjectProperty))
g.add((birth_country, RDF.type, OWL.FunctionalProperty))
g.add((birth_country, RDFS.domain, Person))
g.add((birth_country, RDFS.range, dbo.Country))
g.add((birth_country, RDFS.label, Literal("Birth Country", lang="en")))
g.add((birth_country, RDFS.comment, Literal("The country where a person was born.", lang="en")))

organization_name = myOnto.organizationName
g.add((organization_name, RDF.type, OWL.ObjectProperty))
g.add((organization_name, RDFS.domain, Person))
g.add((organization_name, RDFS.range, SDO.Organization))
g.add((organization_name, RDFS.label, Literal("Organization Name", lang="en")))
g.add((organization_name, RDFS.comment, Literal("The organization which a person belongs to.", lang="en")))

gender = myOnto.gender
g.add((gender, RDF.type, OWL.ObjectProperty))
g.add((gender, RDF.type, OWL.FunctionalProperty))
g.add((gender, RDFS.subPropertyOf, SDO.gender))
g.add((gender, RDFS.domain, Person))
g.add((gender, RDFS.range, SDO.GenderType))
g.add((gender, RDFS.label, Literal("Gender", lang="en")))
g.add((gender, RDFS.comment, Literal("The gender of a person", lang="en")))


## Define Datatype Properties

prize_year = myOnto.prizeYear
g.add((prize_year, RDF.type, OWL.DatatypeProperty))
g.add((prize_year, RDFS.domain, Person))
g.add((prize_year, RDFS.range, XSD.gYear))
g.add((prize_year, RDFS.label, Literal("Prize Year", lang="en")))
g.add((prize_year, RDFS.comment, Literal("The year a person won a Nobel Prize.", lang="en")))

laureate_ID = myOnto.laureateID
g.add((laureate_ID, RDF.type, OWL.DatatypeProperty))
g.add((laureate_ID, RDF.type, OWL.InverseFunctionalProperty))
g.add((laureate_ID, RDFS.domain, Person))
g.add((laureate_ID, RDFS.range, XSD.integer))
g.add((laureate_ID, RDFS.label, Literal("Laureate ID", lang="en")))
g.add((laureate_ID, RDFS.comment, Literal("The unique identifier assigned to each Nobel laureate.", lang="en")))

prize_share = myOnto.prizeShare
g.add((prize_share, RDF.type, OWL.DatatypeProperty))
g.add((prize_share, RDFS.domain, Person))
g.add((prize_share, RDFS.range, XSD.integer))
g.add((prize_share, RDFS.label, Literal("Prize Share", lang="en")))
g.add((prize_share, RDFS.comment, Literal("The allocation of the Nobel Prize award money among the recipients of a particular Nobel Prize category.", lang="en")))

motivation = myOnto.motivation
g.add((motivation, RDF.type, OWL.DatatypeProperty))
g.add((motivation, RDFS.domain, Person))
g.add((motivation, RDFS.range, XSD.string))
g.add((motivation, RDFS.label, Literal("Motivation", lang="en")))
g.add((motivation, RDFS.comment, Literal("The official statement or explanation for awarding a Nobel Prize to a particular individual or group.", lang="en")))

birth_date = myOnto.birthDate
g.add((birth_date, RDF.type, OWL.DatatypeProperty))
g.add((birth_date, RDF.type, OWL.FunctionalProperty))
g.add((birth_date, RDFS.subPropertyOf, SDO.birthDate))
g.add((birth_date, RDFS.domain, Person))
g.add((birth_date, RDFS.range, XSD.date))
g.add((birth_date, RDFS.label, Literal("Date", lang="en")))
g.add((birth_date, RDFS.comment, Literal("The date of birth of a person", lang="en")))

code = myOnto.birthCountryCode
g.add((code, RDF.type, OWL.DatatypeProperty))
g.add((code, RDF.type, OWL.FunctionalProperty))
g.add((code, RDFS.domain, Person))
g.add((code, RDFS.range, XSD.string))
g.add((code, RDFS.label, Literal("Birth Country Code", lang="en")))
g.add((code, RDFS.comment, Literal("The code of a person's birth country", lang="en")))

prize_name = myOnto.hasPrizeName
g.add((prize_name, RDF.type, OWL.DatatypeProperty))
g.add((prize_name, RDF.type, OWL.InverseFunctionalProperty))
g.add((prize_name, RDFS.subPropertyOf, SDO.name))
g.add((prize_name, RDFS.domain, NobelPrize))
g.add((prize_name, RDFS.range, XSD.string))
g.add((prize_name, RDFS.label, Literal("Prize Name", lang="en")))
g.add((prize_name, RDFS.comment, Literal("The name of a Nobel prize category", lang="en")))


######## Define resources below ########

## Nobel Prize resources

chemistry = mySemantics.Nobel_Prize_in_Chemistry
g.add((chemistry, RDF.type, myOnto.NobelPrize))
g.add((chemistry, OWL.sameAs, URIRef(dbr["Nobel_Prize_in_Chemistry"])))
g.add((chemistry, myOnto.hasPrizeName, Literal("Nobel Prize in Chemistry", datatype=XSD.string)))

economics = mySemantics.Nobel_Memorial_Prize_in_Economic_Sciences
g.add((economics, RDF.type, myOnto.NobelPrize))
g.add((economics, OWL.sameAs, URIRef(dbr["Nobel_Memorial_Prize_in_Economic_Sciences"])))
g.add((economics, myOnto.hasPrizeName, Literal("Nobel Memorial Prize in Economic Sciences", datatype=XSD.string)))
g.add((economics, OWL.differentFrom, chemistry))

medicine = mySemantics.Nobel_Prize_in_Physiology_or_Medicine
g.add((medicine, RDF.type, myOnto.NobelPrize))
g.add((medicine, OWL.sameAs, URIRef(dbr["Nobel_Prize_in_Physiology_or_Medicine"])))
g.add((medicine, myOnto.hasPrizeName, Literal("Nobel Prize in Physiology or Medicine", datatype=XSD.string)))
g.add((medicine, OWL.differentFrom, chemistry))
g.add((medicine, OWL.differentFrom, economics))

literature = mySemantics.Nobel_Prize_in_Literature
g.add((literature, RDF.type, myOnto.NobelPrize))
g.add((literature, OWL.sameAs, URIRef(dbr["Nobel_Prize_in_Literature"])))
g.add((literature, myOnto.hasPrizeName, Literal("Nobel Prize in Literature", datatype=XSD.string)))
g.add((literature, OWL.differentFrom, chemistry))
g.add((literature, OWL.differentFrom, economics))
g.add((literature, OWL.differentFrom, medicine))

peace = mySemantics.Nobel_Peace_Prize
g.add((peace, RDF.type, myOnto.NobelPrize))
g.add((peace, OWL.sameAs, URIRef(dbr["Nobel_Peace_Prize"])))
g.add((peace, myOnto.hasPrizeName, Literal("Nobel Peace Prize", datatype=XSD.string)))
g.add((peace, OWL.differentFrom, chemistry))
g.add((peace, OWL.differentFrom, economics))
g.add((peace, OWL.differentFrom, medicine))
g.add((peace, OWL.differentFrom, literature))

physics = mySemantics.Nobel_Prize_in_Physics
g.add((physics, RDF.type, myOnto.NobelPrize))
g.add((physics, OWL.sameAs, URIRef(dbr["Nobel_Prize_in_Physics"])))
g.add((physics, myOnto.hasPrizeName, Literal("Nobel Prize in Physics", datatype=XSD.string)))
g.add((physics, OWL.differentFrom, chemistry))
g.add((physics, OWL.differentFrom, economics))
g.add((physics, OWL.differentFrom, medicine))
g.add((physics, OWL.differentFrom, literature))
g.add((physics, OWL.differentFrom, peace))


## Nobel Laureate resources

# Iterate over the CSV data and add it to the RDF graph
for _, row in df.iterrows(): 
    subject = mySemantics.__getattr__(row["Full_Name"].replace(" ", "_"))
    
    # category
    category_text = row["Category"]
    if category_text == "economics":
        category = economics
    elif category_text == "chemistry":
        category = chemistry
    elif category_text == "medicine":
        category = medicine
    elif category_text == "literature":
        category = literature
    elif category_text == "peace":
        category = peace
    elif category_text == "physics":
        category = physics
    
    # birth country
    birth_country_text = row["Birth_Country"]
    if birth_country_text == "United Kingdom":
        birth_country = URIRef(dbr["United_Kingdom"])
    elif birth_country_text == "USA":
        birth_country = URIRef(dbr["United_States"])
    elif birth_country_text == "USSR":
        birth_country = URIRef(dbr["Soviet_Union"])
    else:
        birth_country = URIRef(dbr[birth_country_text])
    
    # gender
    gender_text = row["Gender"]
    gender = SDO.Male if gender_text == "Male" else SDO.Female

    # bith city
    birth_city = URIRef(dbr[row["Birth_City_dbr"]])

    # organization name
    organization_name = URIRef(dbr[row["Organization_Name_dbr"]])

    # full name
    full_name = URIRef(dbr[row["Full_Name_dbr"]])
    g.add((subject, OWL.sameAs, full_name))

    # add triples
    g.add((subject, RDF.type, myOnto.Person))
    g.add((subject, myOnto.prizeYear, Literal(row["Year"], datatype=XSD.gYear)))
    g.add((subject, myOnto.laureateID, Literal(row["Laureate_Id"], datatype=XSD.integer)))
    g.add((subject, myOnto.prizeCategory, category))
    g.add((subject, myOnto.gender, gender))
    g.add((subject, myOnto.prizeShare, Literal(row["Prize_Share"], datatype=XSD.integer)))
    g.add((subject, myOnto.motivation, Literal(row["Motivation"], datatype=XSD.string)))
    g.add((subject, myOnto.birthDate, Literal(row["Birth_Date"], datatype=XSD.date)))
    g.add((subject, myOnto.birthCountry, birth_country))
    g.add((subject, SDO.givenName, Literal(row["Firstname"], datatype=XSD.string)))
    g.add((subject, SDO.familyName, Literal(row["Lastname"], datatype=XSD.string)))
    g.add((subject, myOnto.birthCountryCode, Literal(row["Birth_Country_Code"], datatype=XSD.string)))

    if row["Birth_City"]:
        g.add((subject, SDO.birthPlace, birth_city))
    if row["Organization_Name"]:
        g.add((subject, myOnto.organizationName, organization_name))


# Save the RDF graph as a Turtle file
current_wdir = os.getcwd()
with open(os.path.join(current_wdir, "Nobel_Prize.ttl"), 'w') as outputFile:
    outputFile.write(g.serialize(format='turtle'))