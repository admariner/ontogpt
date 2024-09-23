

# Class: ChemicalToDiseaseRelationship


_A triple where the subject is a chemical and the object is a disease._





URI: [drug:ChemicalToDiseaseRelationship](http://w3id.org/ontogpt/drug/ChemicalToDiseaseRelationship)



```mermaid
erDiagram
ChemicalToDiseaseRelationship {
    string qualifier  
}
NamedEntity {
    string id  
    string label  
}
Disease {
    string id  
    string label  
}
ChemicalToDiseasePredicate {
    string id  
    string label  
}
Chemical {
    string id  
    string label  
}

ChemicalToDiseaseRelationship ||--|o Chemical : "subject"
ChemicalToDiseaseRelationship ||--|o ChemicalToDiseasePredicate : "predicate"
ChemicalToDiseaseRelationship ||--|o Disease : "object"
ChemicalToDiseaseRelationship ||--|o NamedEntity : "subject_qualifier"
ChemicalToDiseaseRelationship ||--|o NamedEntity : "object_qualifier"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * [Triple](Triple.md)
        * **ChemicalToDiseaseRelationship**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 0..1 <br/> [Chemical](Chemical.md) | The chemical substance, drug, or small molecule | [Triple](Triple.md) |
| [predicate](predicate.md) | 0..1 <br/> [ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md) | The relationship type, e | [Triple](Triple.md) |
| [object](object.md) | 0..1 <br/> [Disease](Disease.md) | The disease or condition that is being treated or induced by the chemical | [Triple](Triple.md) |
| [qualifier](qualifier.md) | 0..1 <br/> [String](String.md) | A qualifier for the statements, e | [Triple](Triple.md) |
| [subject_qualifier](subject_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the chemical, e | [Triple](Triple.md) |
| [object_qualifier](object_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the disease, e | [Triple](Triple.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md) | [triples](triples.md) | range | [ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | drug:ChemicalToDiseaseRelationship |
| native | drug:ChemicalToDiseaseRelationship |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalToDiseaseRelationship
description: A triple where the subject is a chemical and the object is a disease.
from_schema: http://w3id.org/ontogpt/ctd
is_a: Triple
slot_usage:
  subject:
    name: subject
    description: 'The chemical substance, drug, or small molecule.  For example: Lidocaine,
      Monosodium Glutamate, Imatinib.'
    domain_of:
    - Triple
    range: Chemical
  object:
    name: object
    description: The disease or condition that is being treated or induced by the
      chemical. For example, asthma, cancer, covid-19, cardiac asystole, Hypotension,
      Headache.
    domain_of:
    - Triple
    range: Disease
  predicate:
    name: predicate
    description: The relationship type, e.g. INDUCES, TREATS.
    domain_of:
    - Triple
    range: ChemicalToDiseasePredicate
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the chemical, e.g. "high dose"
      or "intravenously administered"
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the disease, e.g. "severe"
      or "with additional complications"
    domain_of:
    - Triple
    range: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: ChemicalToDiseaseRelationship
description: A triple where the subject is a chemical and the object is a disease.
from_schema: http://w3id.org/ontogpt/ctd
is_a: Triple
slot_usage:
  subject:
    name: subject
    description: 'The chemical substance, drug, or small molecule.  For example: Lidocaine,
      Monosodium Glutamate, Imatinib.'
    domain_of:
    - Triple
    range: Chemical
  object:
    name: object
    description: The disease or condition that is being treated or induced by the
      chemical. For example, asthma, cancer, covid-19, cardiac asystole, Hypotension,
      Headache.
    domain_of:
    - Triple
    range: Disease
  predicate:
    name: predicate
    description: The relationship type, e.g. INDUCES, TREATS.
    domain_of:
    - Triple
    range: ChemicalToDiseasePredicate
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the chemical, e.g. "high dose"
      or "intravenously administered"
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the disease, e.g. "severe"
      or "with additional complications"
    domain_of:
    - Triple
    range: NamedEntity
attributes:
  subject:
    name: subject
    description: 'The chemical substance, drug, or small molecule.  For example: Lidocaine,
      Monosodium Glutamate, Imatinib.'
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    alias: subject
    owner: ChemicalToDiseaseRelationship
    domain_of:
    - Triple
    range: Chemical
  predicate:
    name: predicate
    description: The relationship type, e.g. INDUCES, TREATS.
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    alias: predicate
    owner: ChemicalToDiseaseRelationship
    domain_of:
    - Triple
    range: ChemicalToDiseasePredicate
  object:
    name: object
    description: The disease or condition that is being treated or induced by the
      chemical. For example, asthma, cancer, covid-19, cardiac asystole, Hypotension,
      Headache.
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    alias: object
    owner: ChemicalToDiseaseRelationship
    domain_of:
    - Triple
    range: Disease
  qualifier:
    name: qualifier
    description: A qualifier for the statements, e.g. "NOT" for negation
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    alias: qualifier
    owner: ChemicalToDiseaseRelationship
    domain_of:
    - Triple
    range: string
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the chemical, e.g. "high dose"
      or "intravenously administered"
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    alias: subject_qualifier
    owner: ChemicalToDiseaseRelationship
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the disease, e.g. "severe"
      or "with additional complications"
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    alias: object_qualifier
    owner: ChemicalToDiseaseRelationship
    domain_of:
    - Triple
    range: NamedEntity

```
</details>