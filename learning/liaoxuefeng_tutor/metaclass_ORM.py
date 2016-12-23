#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2016-12-23 Fri 15:17:28 Shaikh>
"""
Metaclass application in ORM.

Object Relational Mapping.
"""
class Field(object):
    """
    Base class Field.

    Used for the SQL table field.
    """
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        # return the class name and instance name.
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    """
    Subclass for fields whose column type is str.
    """
    def __init__(self, name):
        # equivalent to 'super().__init__(name, 'varchar(100)')
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    """
    Subclass for fields whose column type is int.
    """
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# define the metaclass
class ModelMetaclass(type):
    """
    Customize the creation of class Model, especially its subclass User.

    Must inherit from 'type' and have the method __new__.
    """
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            # do not alter the Model class
            # the customization is applied to User(Model)
            return type.__new__(mcs, name, bases, attrs)
        # print the subclass of Model, e.g. User
        print('Found model: %s' % name)
        mappings = dict()
        # scan the attributes for Field-type instances
        # like IntegerField or StringField defined above
        # then print them and add them to mappings variable.
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ===> %s' % (k, v))
                mappings[k] = v
        # remove all scanned Field-type attributes
        # since instance attributes will override the class attributes
        for k in mappings.keys():
            attrs.pop(k)
        # save the scanned mappings to a new attribute '__mappings__'
        attrs['__mappings__'] = mappings
        # define the SQL table a name, here same as the class.
        attrs['__table__'] = name
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    """
    Base Class Model with keyword argument metaclass.

    From the definition of ModelMetaclass, this metaclass does not affect
    this base class Model but for its subclass.
    """
    # this init is defined according to its base class 'dict'.
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    # dynamically get the attributes of the instance
    # note that it inherits from 'dict' class.
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        """
        A method used to save all the attributes into a table
        and generate the SQL command.
        """
        fields = []
        params = []
        args = []
        # __mappings__ is added in metaclass ModelMetaclass
        # it is a dict and the value's type is Field instance.
        # __mappings__ does not save values information from instances
        # but only keys, so args can be get with these keys.
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?') # why '?' maybe related to SQL.
            args.append(getattr(self, k, None))
        sql = 'insert into {} ({}) values ({})'.format(
            self.__table__, ','.join(fields), ','.join(params))
        print('SQL: {}'.format(sql))
        print('ARGS: {}'.format(str(args)))


# test ORM
class User(Model):
    """
    This definition creates four Field-type variable with corresponding names.

    They will firstly be used to construct __mappings__ attribute in metaclass ModelMetaclass.
    Then be 'poped' since they may be overridden by the creation of a instance."""
    ids = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('passwd')


testuser = User(ids=12345, name='Bill', email='a@b.com', password='secret')
testuser.save()
