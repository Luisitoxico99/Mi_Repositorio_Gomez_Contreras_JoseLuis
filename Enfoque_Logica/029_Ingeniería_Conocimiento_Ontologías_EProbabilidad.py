
from rdflib import Graph, Namespace, RDF, RDFS, OWL

# Creamos un grafo RDF para representar la ontología
g = Graph()

# Definimos los namespaces
onto = Namespace("http://www.example.org/ontology/")
ex = Namespace("http://www.example.org/resource/")

# Definimos clases y propiedades en la ontología
g.add((onto.Person, RDF.type, OWL.Class))
g.add((onto.Employee, RDF.type, OWL.Class))
g.add((onto.WorksFor, RDF.type, OWL.ObjectProperty))
g.add((onto.hasName, RDF.type, OWL.DatatypeProperty))

# Definimos relaciones entre clases y propiedades
g.add((onto.Employee, RDFS.subClassOf, onto.Person))
g.add((onto.WorksFor, RDFS.domain, onto.Employee))
g.add((onto.WorksFor, RDFS.range, onto.Organization))
g.add((onto.hasName, RDFS.domain, onto.Person))
g.add((onto.hasName, RDFS.range, RDFS.Literal))

# Añadimos instancias de las clases
g.add((ex.John, RDF.type, onto.Person))
g.add((ex.John, onto.hasName, "John Smith"))
g.add((ex.John, RDF.type, onto.Employee))
g.add((ex.John, onto.WorksFor, ex.Acme))

# Serializamos el grafo en formato RDF/XML
print(g.serialize(format="xml").decode("utf-8"))
