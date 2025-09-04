# Nobel Laureates Knowledge Graph

A knowledge graph project representing Nobel Prize laureates and their associated information using semantic web technologies.

## Overview

This project creates a knowledge graph that models Nobel Prize laureates from various categories (Physics, Chemistry, Medicine, Literature, Peace, and Economics) along with their biographical information, achievements, and relationships. The project demonstrates the application of semantic web technologies including RDF, OWL ontologies, and SHACL validation.

## Project Structure

```
KG_Nobel_Laureates/
├── Nobel_Prize.csv              # Source data containing Nobel laureate information
├── Nobel_rdflib.py             # Python script to generate RDF from CSV data
├── Nobel_Prize.ttl             # Generated RDF knowledge graph in Turtle format
├── Ontology_Nobel.graphml      # Visual ontology representation (GraphML format)
└── Shacl_test.ttl             # SHACL shapes for data validation
```

## Data Model

### Core Classes

- **`myOnto:Person`**: Represents Nobel Prize laureates
  - Subclass of `schema:Person`
  - Contains biographical and award information

- **`myOnto:NobelPrize`**: Represents different Nobel Prize categories
  - Subclass of `dbo:NobelPrize`
  - Six distinct prize categories

### Key Properties

#### Object Properties
- `myOnto:prizeCategory`: Links laureates to their Nobel Prize category
- `myOnto:birthCountry`: Links laureates to their birth country
- `myOnto:organizationName`: Links laureates to their affiliated organization
- `myOnto:gender`: Specifies the gender of laureates

#### Datatype Properties
- `myOnto:prizeYear`: Year the prize was awarded
- `myOnto:laureateID`: Unique identifier for each laureate
- `myOnto:prizeShare`: Prize share allocation
- `myOnto:motivation`: Official citation for the award
- `myOnto:birthDate`: Date of birth
- `myOnto:birthCountryCode`: ISO country code for birth country

### Nobel Prize Categories

The knowledge graph includes all six Nobel Prize categories:
1. **Physics** (`mySemantics:Nobel_Prize_in_Physics`)
2. **Chemistry** (`mySemantics:Nobel_Prize_in_Chemistry`)
3. **Medicine** (`mySemantics:Nobel_Prize_in_Physiology_or_Medicine`)
4. **Literature** (`mySemantics:Nobel_Prize_in_Literature`)
5. **Peace** (`mySemantics:Nobel_Peace_Prize`)
6. **Economics** (`mySemantics:Nobel_Memorial_Prize_in_Economic_Sciences`)

## Technical Implementation

### Technologies Used
- **Python 3.x** with RDFLib for RDF generation
- **RDF/Turtle** for knowledge representation
- **OWL** for ontology modeling
- **SHACL** for data validation
- **Schema.org** and **DBpedia** vocabularies for interoperability

### Namespaces
- `myOnto:` - Custom ontology namespace (`http://www.mysemantics.com/ontology/`)
- `mySemantics:` - Resource namespace (`http://www.mysemantics.com/resource/`)
- `dbr:` - DBpedia resources (`http://dbpedia.org/resource/`)
- `dbo:` - DBpedia ontology (`http://dbpedia.org/ontology/`)
- `schema:` - Schema.org vocabulary

## Usage

### Prerequisites
```bash
pip install rdflib pandas
```

### Generate RDF Knowledge Graph
```bash
python Nobel_rdflib.py
```


### Data Validation
The project includes SHACL shapes (`Shacl_test.ttl`) for validating the generated RDF data, ensuring:
- Required properties are present
- Data types are correct
- Cardinality constraints are satisfied

## Data Sources

The CSV file contains information about Nobel laureates including:
- Personal information (name, birth date, birth country, gender)
- Prize details (category, year, prize share, motivation)
- Institutional affiliations
- DBpedia resource mappings for linked data integration

## Features

### Semantic Integration
- **DBpedia Alignment**: Resources are linked to corresponding DBpedia entities using `owl:sameAs`
- **Schema.org Compatibility**: Uses standard vocabularies for better interoperability
- **Linked Data Principles**: URIs are dereferenceable and follow best practices


## Visualization

The `Ontology_Nobel.graphml` file provides a visual representation of the ontology structure, which can be opened in graph visualization tools like yEd or Gephi.

## Documentation

For detailed information about the project methodology, ontology design decisions, and evaluation results, please refer to the `Final_Project_Report.pdf`.

## License

This project is created for educational purposes as part of a Semantic Web course. The Nobel Prize data is publicly available in Kaggle.
