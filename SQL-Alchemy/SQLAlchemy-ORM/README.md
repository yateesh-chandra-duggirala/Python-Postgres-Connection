# ORM Mapped Class Configuration
## ORM Mapping Styles
- The original mapping API is commonly referred to as classical style whereas the more automated style of mapping is known as declarative style. There are two mapping styles : 
    1. Imperative Mapping
    2. Declarative Mapping

- All ORM Mappings originate from a single object known as registry, which is a registry of mapped classes.
- Using this registry, a set of mapper configurations can be finalized as a group, and classes within a particular registry may refer to each other by name within the configurational process.

### a. Declarative Mapping : 
- It is the typical way that mappings are constructed in modern SQL Alchemy. 
- The most common patterns is to first construct a base class using the DeclarativeBase superclass.
- The resulting base class, when subclasses will apply the declarative mapping to process to all subclasses that derive from it, relative to a particular registry that is local to the new base by default.
- The example below illustrates the use of a declarative base which is then used in a declarative table mapping.
- The DeclarativeBase class is used to generate a new base class from which new classes to be mapped may inherit from, as above a new mapped class User is constructed.
- The base class refers to a registry object that maintains a collection of related mapped classes. as well as to a Metadata object that retains a collection of Table objects to which the classes are mapped.
- The major Declarative mapping styles are further detailed in the following sections.
    a. Using a Declarative Base Class - declarative mapping use a base class
    b. Declarative Mapping using a Decorator - a declarative mapping using a decorator, rather than a base class.
- Within the scope of a Declarative Mapped class, there are also two varieties of how the Table metadata may be declared.

### b. Imperative Mapping : 
- An Imperative mapping or classical mapping refers to the configuration of a mapped class using the registry.map_imperatively() method, where the target class does not include any declarative class attributes.
- The classes which are mapped imperatively are fully interchangeable with those mapped with the Declarative approach.
- Both systems ultimately create the same configuration, consisting of a table, user-defined class, linked together with a mapper object.
- When we talk about the behavior of Mapper.
- This includes when using the Declarative systems as well.

### Runtime introspection of Mapped Classes, instances and Mappers
- A class that is mapped using registry will also feature a few attributes that are common to all mappings
- the __mapper__ attribute will refer to the Mapper that is associated with the class
- This Mapper is also what is returned when using the inspect() function against the mapping class.

```
    from sqlalchemy import inspect
    mapper = inspect(user)
```
- we can get the columns by using list(insp.columns) or list(insp.column_attrs)