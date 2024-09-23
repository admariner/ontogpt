

# Slot: categories


_the categories to which this entity belongs._



URI: [oc:categories](http://w3id.org/ontogpt/ontology-class-templatecategories)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyClass](OntologyClass.md) |  |  no  |







## Properties

* Range: [OntologyClass](OntologyClass.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of categories to which the entity belongs. These may be taken from an upper level ontology such as COB, BioLink, or UMLS semantic types. |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_class




## LinkML Source

<details>
```yaml
name: categories
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of categories to which the entity belongs. These
      may be taken from an upper level ontology such as COB, BioLink, or UMLS semantic
      types.
description: the categories to which this entity belongs.
from_schema: https://w3id.org/ontogpt/ontology_class
rank: 1000
multivalued: true
alias: categories
owner: OntologyClass
domain_of:
- OntologyClass
range: OntologyClass

```
</details>