
# Class: Evidence




URI: [reaction:Evidence](http://w3id.org/ontogpt/reaction/Evidence)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[ReactionDocument]-%20has_evidence%200..*>[Evidence&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Evidence],[ReactionDocument])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[ReactionDocument]-%20has_evidence%200..*>[Evidence&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Evidence],[ReactionDocument])

## Identifier prefixes

 * OBI
 * ECO
 * MS

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞has_evidence](reactionDocument__has_evidence.md)*  <sub>0..\*</sub>  **[Evidence](Evidence.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
