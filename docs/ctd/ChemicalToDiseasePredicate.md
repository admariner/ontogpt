

# Class: ChemicalToDiseasePredicate


_A predicate for chemical to disease relationships_





URI: [drug:ChemicalToDiseasePredicate](http://w3id.org/ontogpt/drug/ChemicalToDiseasePredicate)



```mermaid
erDiagram
ChemicalToDiseasePredicate {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * [RelationshipType](RelationshipType.md)
        * **ChemicalToDiseasePredicate**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) | [predicate](predicate.md) | range | [ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md) |






## Comments

* for the purposes of evaluation against BC5CDR, any predicate other than INDUCES is ignored.

## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | drug:ChemicalToDiseasePredicate |
| native | drug:ChemicalToDiseasePredicate |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalToDiseasePredicate
description: A predicate for chemical to disease relationships
comments:
- for the purposes of evaluation against BC5CDR, any predicate other than INDUCES
  is ignored.
from_schema: http://w3id.org/ontogpt/ctd
is_a: RelationshipType

```
</details>

### Induced

<details>
```yaml
name: ChemicalToDiseasePredicate
description: A predicate for chemical to disease relationships
comments:
- for the purposes of evaluation against BC5CDR, any predicate other than INDUCES
  is ignored.
from_schema: http://w3id.org/ontogpt/ctd
is_a: RelationshipType
attributes:
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    identifier: true
    alias: id
    owner: ChemicalToDiseasePredicate
    domain_of:
    - NamedEntity
    - Publication
    range: string
    required: true
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/ctd
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: ChemicalToDiseasePredicate
    domain_of:
    - NamedEntity
    range: string

```
</details>